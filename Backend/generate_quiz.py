# Required libraries: pip install jupyterlab python-dotenv langchain openai

import os
import json
import openai
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

class QuizGenerator:
    def __init__(self):
        # Load API key from the .env file
        load_dotenv()
        my_key = os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(temperature=0, openai_api_key=my_key)
        self.template ="""
        You are an expert quiz maker for technical fields. Let's think step by step and create a quiz with {num_questions} {quiz_type} questions about the following concept/content: {quiz_context}.Only provide JSON code as a response, no other response.

        The format of the quiz could be stored in JSON format as follows:

        - For Multiple-choice questions:
        {{
        "quizType": "Multiple-choice",
        "quizContext": "{{quiz_context}}",
        "questions": [
            {{
            "question": "Question1 text here",
            "options": {{
                "a": "Answer 1",
                "b": "Answer 2",
                "c": "Answer 3",
                "d": "Answer 4"
            }},
            "correctAnswer": "a|b|c|d"
            }},
            {{
            "question": "Question2 text here",
            "options": {{
                "a": "Answer 1",
                "b": "Answer 2",
                "c": "Answer 3",
                "d": "Answer 4"
            }},
            "correctAnswer": "a|b|c|d"
            }}
        ]
        }}
        - For True/false questions:

        {{
        "quizType": "True-False",
        "quizContext": "{{quiz_context}}",
        "questions": [
            {{
            "question": "Question1 text here",
            "correctAnswer": "True|False"
            }},
            {{
            "question": "Question2 text here",
            "correctAnswer": "True|False"
            }}
        ]
        }}
        - For Open-ended questions:

        {{
        "quizType": "Open-ended",
        "quizContext": "{{quiz_context}}",
        "questions": [
            {{
            "question": "Question1 text here",
            "answer": "Detailed answer here"
            }},
            {{
            "question": "Question2 text here",
            "answer": "Detailed answer here"
            }}
        ]
        }}
        - Example for Multiple-choice:

        {{
        "quizType": "Multiple-choice",
        "quizContext": "Binary search tree complexities",
        "questions": [
            {{
            "question": "What is the time complexity of a binary search tree?",
            "options": {{
                "a": "O(n)",
                "b": "O(log n)",
                "c": "O(n^2)",
                "d": "O(1)"
            }},
            "correctAnswer": "b"
            }}
        ]
        }}
        """
        self.prompt_template = PromptTemplate.from_template(self.template)
        self.chain = LLMChain(llm=ChatOpenAI(temperature=0.0), prompt=self.prompt_template)

    def get_response(self, prompt_question):
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful research and programming assistant"},
                      {"role": "user", "content": prompt_question}]
        )
        return response.choices[0].message.content

    def generate_quiz(self, num_questions, quiz_type, quiz_context):
        return self.chain.run(num_questions=num_questions, quiz_type=quiz_type, quiz_context=quiz_context)

    def save_quiz_to_file(self, quiz_response, filename='quiz_data.json'):
        # Save the quiz to a JSON file
        try:
            json_data = json.loads(quiz_response)
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            json_data = None

        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)

    @property
    def get_llm(self):
        return self.llm

    @property
    def get_template(self):
        return self.template
'''
# Example usage
if __name__ == "__main__":
    quiz_gen = QuizGenerator()
    quiz_response = quiz_gen.generate_quiz(5, "multiple-choice", "Data Structures in Python Programming")
    quiz_gen.save_quiz_to_file(quiz_response)
'''