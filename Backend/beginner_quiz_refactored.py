# creating the initial quiz for the user
# focusing on python questions

import random
from string import ascii_lowercase
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = { # storing questions and alternative answers in a dictionary
    "Given a function that does not return any value, what value is shown when executed at the shell": [
        "None", "int", "bool", "void"
    ],
    "Which module in Python supports regular expressions" :[
        "re", "regex", "pyregex", "None of these options"
    ],
    "Which of the following is not a complex number" :[
        "k = 2 + 3l", "k = 2+3j", "k = complex(2, 3)", "k = 2 + 3J"
    ],
    "Given a string s='Welcome', which of the following is incorrect" :[
        "s[1]='r'", "print s[0]", "print s.lower()", "print s.strip()"
    ],
    }

# High level overview of the process
def run_quiz():
    # Preprocess
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    # Process (main loop)
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    # Postprocess
        print(f"\nYou got {num_correct} out of {num} questions")     

# Preprocessing - preparing QUESTIONS data structure for use in main loop
# Here we limit number of questions and make sure they are random

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


# get_answer accepts a question text and a list of alternatives.
# We label the alternatives and ask the user to enter a valid label, before returning their answer

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")
    
    return labeled_alternatives[answer_label]

# ask_question picks out the correct answer from alternatives, shuffles the alternatives
# and prints the q to the screen

def ask_question(question, alternatives):
    correct_answer = alternatives [0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0 # return 1 or 0 to indicate to calling function whether answer was correct
    
if __name__ == "__main__":
    run_quiz()