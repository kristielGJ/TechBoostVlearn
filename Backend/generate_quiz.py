# Required libraries: pip install jupyterlab python-dotenv langchain openai
import os
import json
import openai
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
'''
Authors: Gera Jahja
    Lang chain used here to generate quizzes in json format 
    From this generated quiz, a sentence of educational content is created per question, and fed to course_generator.py to aind in the generation of the course
    It is also used for onboarding skill validation quizes.

    To Do: -  generate content using existing vodafone content
            - add tasks/ programming tasks for technical courses. 

'''

class QuizGenerator:
    """ 
        Initializes the QuizGenerator by setting up the OpenAI API, 
        loading the template for quiz generation, and ensuring the quiz directory exists.
    """
    def __init__(self):
        load_dotenv()
        my_key = os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(temperature=0, openai_api_key=my_key)
        self.template = """
        You are an expert quiz maker and educator for technical fields. Let's think step by step and create a quiz with {num_questions} {quiz_type} questions about the following concept/content: {quiz_context}.
        For each question, provide a brief educational content explaining the topic in detail before presenting the question. This can include visuals.
        Only provide JSON code as a response.

        The format of the quiz should be stored in JSON format as follows:

        - For Multiple-choice questions:
        {{
        "quizType": "Multiple-choice",
        "quizContext": "{quiz_context}",
        "questions": [
            {{
            "education": "Detailed educational content for Question 1 here",
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
            "education": "Detailed educational content for Question 2 here",
            "question": "Question2 text here",
            "options": {{
                "a": "Answer 1",
                "b": "Answer 2",
                "c": "Answer 3",
                "d": "Answer 4"
            }},
            "correctAnswer": "a|b|c|d"
            }}
        ],
        "nextTopic": "{next_topic}"
        }}
        """
        self.prompt_template = PromptTemplate.from_template(self.template)
        self.chain = LLMChain(llm=ChatOpenAI(temperature=0.0), prompt=self.prompt_template)
        self.generated_quizzes = {} 
        self.quiz_dir = "quizzes"  
        os.makedirs(self.quiz_dir, exist_ok=True) 

    """
    Generates a quiz for the given topic if it doesn't already exist. 
        The quiz includes educational content and multiple-choice questions.

        Parameters:
            num_questions (int): Number of questions to generate.
            quiz_type (str): Type of quiz, e.g., "Multiple-choice".
            quiz_context (str): The context or topic for the quiz.
            next_topic (str): The next topic to be addressed in the course.

        Returns:
            str: The generated quiz content in JSON format.
    """
    def generate_quiz(self, num_questions, quiz_type, quiz_context, next_topic):

        quiz_filename = os.path.join(self.quiz_dir, f'{quiz_context.replace(" ", "_")}_quiz.json')
        if os.path.exists(quiz_filename):
            print(f"Quiz for topic '{quiz_context}' already exists. Skipping generation.")
            with open(quiz_filename, 'r') as file:
                return file.read()

        print(f"Generating quiz for topic '{quiz_context}'...")
        quiz_response = self.chain.run(
            num_questions=num_questions, quiz_type=quiz_type, quiz_context=quiz_context, next_topic=next_topic)
        self.save_quiz_to_file(quiz_response, quiz_filename)
        return quiz_response

    """
    Saves the generated quiz to a file in JSON format.

        Parameters:
            quiz_response (str): The quiz content in JSON format.
            filename (str): The name of the file to save the quiz content.
    """
    def save_quiz_to_file(self, quiz_response, filename):
        try:
            json_data = json.loads(quiz_response)
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            json_data = None

        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)


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
        }}'''