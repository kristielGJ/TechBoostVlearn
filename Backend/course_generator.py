from generate_quiz import QuizGenerator
from extract_skills import ExtractSkills
import os
import json

'''
Authors: Gera Jahja
    WIP
    To Do: -  populate content before quiz
'''
class CourseGenerator:
    """
        Initializes the CourseGenerator by setting the quiz generator, course directory,
        and ensuring the course directory exists.

        Parameters:
            quiz_generator (QuizGenerator): An instance of the QuizGenerator class.
            course_directory : The directory where course files will be stored (courses folder in Backend)
    """
    def __init__(self, quiz_generator, course_directory="courses"):
        self.quiz_generator = quiz_generator
        self.course_directory = course_directory
        os.makedirs(self.course_directory, exist_ok=True)

    """
        Creates a course with the given name and layout. If the course already exists,
        it skips generation. It generates content and quizzes for each topic and writes
        them to a Markdown file.

        Parameters:
            course_name : The name of the course.
            course_layout : A dictionary representing the course layout.

        Returns:
            string: The content of the generated course.
    """
    def create_course(self, course_name, course_layout):
        course_filename = os.path.join(self.course_directory, f'{course_name.replace(" ", "_")}_course.md')
        if os.path.exists(course_filename):
            print(f"Course '{course_name}' already exists. Skipping generation.")
            with open(course_filename, 'r') as file:
                return file.read()

        course_content = f"# Course on {course_name}\n\n"
        topics = list(course_layout.keys())

        for i, (topic, sections) in enumerate(course_layout.items()):
            next_topic = "No more topics" if i == len(topics) - 1 else topics[i + 1]
            course_content += f"## {topic}\n\n"
            content_section = sections.get("Content", {})
            for section, content in content_section.items():
                course_content += f"### {section}\n\n{content}\n\n"

            quiz_response = self.quiz_generator.generate_quiz(
                num_questions=2, quiz_type="Multiple-choice", quiz_context=topic, next_topic=next_topic)
            quiz_content = self.parse_quiz_response(quiz_response)
            quiz_title = sections.get("Quiz", f"Quiz on {topic}")
            course_content += f"## {quiz_title}\n\n{quiz_content}\n\n"

        with open(course_filename, 'w') as file:
            file.write(course_content)

        return course_content
    """
        Parses the quiz response JSON and converts it into a Markdown format.

        Parameters:
            quiz_response : The quiz content in JSON format.

        Returns:
            string: The quiz content in Markdown format.
    """
    def parse_quiz_response(self, quiz_response):
        quiz_content = ""
        try:
            quiz_data = json.loads(quiz_response)
            for index, question in enumerate(quiz_data["questions"], start=1):
                quiz_content += f"### Question {index}\n\n"
                quiz_content += f"**Educational Content:** {question['education']}\n\n"
                quiz_content += f"**Question:** {question['question']}\n\n"
                quiz_content += "Options:\n"
                for option, text in question["options"].items():
                    quiz_content += f"- {option}: {text}\n"
                quiz_content += "\n\n"
        except json.JSONDecodeError as e:
            print("Error parsing quiz response:", e)

        return quiz_content
"""
    Example- Creation of a python for beginners course
"""
def main():

    quiz_gen = QuizGenerator()
    course_gen = CourseGenerator(quiz_generator=quiz_gen)

    course_layout = {
        "Introduction to Python": {
            "Content": {
                "Overview": "Python is a versatile and beginner-friendly programming language used for web development, data analysis, artificial intelligence, and more.",
                "Getting Started with Python": "This section covers the basics of Python programming, including installation, setting up the development environment, and writing your first Python program."
            }
        },
        "Working with Variables and Data Types": {
            "Content": {
                "Variables and Assignments": "Variables store data in Python, assigned using the assignment operator (=).",
                "Data Types in Python": "Python supports various data types: integers, floats, strings, lists, tuples, dictionaries, each with its own characteristics and methods."
            }
        },
        "Control Flow and Loops": {
            "Content": {
                "Conditional Statements": "Conditional statements perform actions based on conditions using if, elif, and else.",
                "Looping Constructs": "Loops iterate over a sequence of elements using for and while loops."
            }
        },
        "Functions and Modules": {
            "Content": {
                "Functions": "Functions are reusable code blocks performing specific tasks.",
                "Modules and Packages": "Modules contain Python code, organized into packages for code reuse."
            }
        },
        "Working with Lists and Dictionaries": {
            "Content": {
                "Lists": "Lists are ordered collections of items.",
                "Dictionaries": "Dictionaries are unordered collections of key-value pairs."
            }
        },
        "File Handling": {
            "Content": {
                "Reading from Files": "Python provides functions to read data from files.",
                "Writing to Files": "Python provides functions to write data to files."
            }
        },
        "Exception Handling": {
            "Content": {
                "Handling Errors": "Exception handling manages errors using try, except, else, and finally blocks.",
                "Raising Exceptions": "You can raise custom exceptions to indicate errors."
            }
        },
        "Object-Oriented Programming (OOP)": {
            "Content": {
                "Classes and Objects": "OOP is based on objects, created from classes.",
                "Inheritance and Polymorphism": "Inheritance creates new classes based on existing ones, while polymorphism allows objects to be treated as instances of a superclass."
            }
        },
        "Working with Strings": {
            "Content": {
                "String Operations": "Strings are sequences of characters.",
                "Regular Expressions": "Regular expressions are tools for pattern matching in strings."
            }
        },
        "Working with Sets": {
            "Content": {
                "Sets in Python": "Sets are unordered collections of unique elements.",
                "Set Operations": "Python provides set operations such as union, intersection, difference, and symmetric difference."
            }
        }
    }
    
    course_name = "Python Programming for Beginners"
    course_content = course_gen.create_course(course_name, course_layout)
    print("Generation Complete")

if __name__ == "__main__":
    main()
