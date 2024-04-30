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
        "k = 2 + 3l", "k = 2 + 3j", "k = complex(2, 3)", "k = 2 + 3J"
    ],
    "Given a string s = 'Welcome', which of the following is incorrect" :[
        "s[1]='r'", "print s[0]", "print s.lower()", "print s.strip()"
    ],
    }

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions) # randomise order of questions and alternatives

num_correct = 0 # storing number of correct answers
for num, (question, alternatives) in enumerate(questions, start=1): # starting numbering of choices at 1
    print(f"\nQuestion {num}:") # numbering the questions
    print(f"{question}?")
    correct_answer = alternatives[0] # correct answer is always the first alternative

    # changing order of alternatives, using lowercase letters to identify answers 
    # string.ascii_lowercase gets letters that label your answer alternatives. You combine letters and alternatives with zip() and store them in a dictionary
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))) 
    )

    for label, alternative in labeled_alternatives.items(): # labelling the potential 
        print(f" {label}) {alternative}")

# to handle user error
        # answer_label = input("\nChoice? ") # adding a label to each alternative, asking user for label input only
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")
    
    answer = labeled_alternatives[answer_label] # storing reordered alternatives to look up answer based on answer label entered
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

# print(f"\nYou got {num_correct} correct out of {num} questions")