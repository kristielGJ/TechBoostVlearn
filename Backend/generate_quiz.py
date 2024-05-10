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
        self.template = """
        You are an expert quiz maker for technical fields. Let's think step by step and create a quiz with {num_questions} {quiz_type} questions about the following concept/content: {quiz_context}. Only provide JSON code as a response, no other response.
        
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
        """
        self.prompt_template = PromptTemplate.from_template(self.template)
        self.chain = LLMChain(llm=ChatOpenAI(temperature=0.0), prompt=self.prompt_template)
        self.generated_quizzes = {}  # Dictionary to store generated quizzes

    def generate_quiz(self, num_questions, quiz_type, quiz_context):
        try:
            # Attempt to use an existing quiz
            quiz_response = self.generated_quizzes[quiz_context]
            print("Using existing quiz for context:", quiz_context)
        except KeyError:
            # If no quiz exists for the context, generate a new one
            print("Generating new quiz for context:", quiz_context)
            quiz_response = self.chain.run(num_questions=num_questions, quiz_type=quiz_type, quiz_context=quiz_context)
            self.generated_quizzes[quiz_context] = quiz_response  # Store the new quiz

        # Save the quiz to a file (always)
        filename = f'{quiz_context.replace(" ", "_")}_quiz.json'
        self.save_quiz_to_file(quiz_response, filename)
        return quiz_response


    def save_quiz_to_file(self, quiz_response, filename):
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


# Example usage
if __name__ == "__main__":
    quiz_gen = QuizGenerator()
    quiz_response = quiz_gen.generate_quiz(5, "multiple-choice", "Data Structures in Java Programming")

''''''
''' - For True/false questions:

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
        '''