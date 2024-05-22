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
    def __init__(self, quiz_generator, course_directory="courses"):
        self.quiz_generator = quiz_generator
        self.course_directory = course_directory
        os.makedirs(self.course_directory, exist_ok=True)  

    def create_course(self, course_name, course_layout):
        course_filename = os.path.join(self.course_directory, f'{course_name.replace(" ", "_")}_course.md')
        if os.path.exists(course_filename):
            with open(course_filename, 'r') as file:
                return file.read()

        # If the course file does not exist, generate the course
        course_content = f"# Course on {course_name}\n\n"

        for topic, sections in course_layout.items():
            course_content += f"## {topic}\n\n"
            content_section = sections.get("Content", {})
            for section, content in content_section.items():
                course_content += f"### {section}\n\n{content}\n\n"
            
            # Generate quiz for the topic
            quiz_response = self.quiz_generator.generate_quiz(
                num_questions=2, quiz_type="Multiple-choice", topic=topic)
            quiz_content = self.parse_quiz_response(quiz_response)

            # Add quiz to course content
            quiz_title = sections.get("Quiz", f"Quiz on {topic}")
            course_content += f"## {quiz_title}\n\n{quiz_content}\n\n"

        # Save the course content to a Markdown file
        with open(course_filename, 'w') as file:
            file.write(course_content)

        return course_content

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


def main():
    quiz_gen = QuizGenerator()
    course_gen = CourseGenerator(quiz_generator=quiz_gen)

    course_layout = {
    "Introduction to Python": {
        "Overview": "Python is a versatile and beginner-friendly programming language used for web development, data analysis, artificial intelligence, and more.",
        "Getting Started with Python": "This section covers the basics of Python programming, including installation, setting up the development environment, and writing your first Python program.",
    },
    "Working with Variables and Data Types": {
        "Variables and Assignments": "Variables store data in Python, assigned using the assignment operator (=).",
        "Data Types in Python": "Python supports various data types: integers, floats, strings, lists, tuples, dictionaries, each with its own characteristics and methods.",
    },
    "Control Flow and Loops": {
        "Conditional Statements": "Conditional statements perform actions based on conditions using if, elif, and else.",
        "Looping Constructs": "Loops iterate over a sequence of elements using for and while loops.",
    },
    "Functions and Modules": {
        "Functions": "Functions are reusable code blocks performing specific tasks.",
        "Modules and Packages": "Modules contain Python code, organized into packages for code reuse.",
    },
    "Working with Lists and Dictionaries": {
        "Lists": "Lists are ordered collections of items.",
        "Dictionaries": "Dictionaries are unordered collections of key-value pairs.",
    },
    "File Handling": {
        "Reading from Files": "Python provides functions to read data from files.",
        "Writing to Files": "Python provides functions to write data to files.",
    },
    "Exception Handling": {
        "Handling Errors": "Exception handling manages errors using try, except, else, and finally blocks.",
        "Raising Exceptions": "You can raise custom exceptions to indicate errors.",
    },
    "Object-Oriented Programming (OOP)": {
        "Classes and Objects": "OOP is based on objects, created from classes.",
        "Inheritance and Polymorphism": "Inheritance creates new classes based on existing ones, while polymorphism allows objects to be treated as instances of a superclass.",
    },
    "Working with Strings": {
        "String Operations": "Strings are sequences of characters.",
        "Regular Expressions": "Regular expressions are tools for pattern matching in strings.",
    },
    "Working with Sets": {
        "Sets in Python": "Sets are unordered collections of unique elements.",
        "Set Operations": "Python provides set operations such as union, intersection, difference, and symmetric difference.",
    },
    # Add more topics
}
    
    # Create course
    course_name = "Python Programming for Beginners"
    course_content = course_gen.create_course(course_name, course_layout)
    print("Generation Complete")

if __name__ == "__main__":
    main()