import json
import os
from flask import Flask, jsonify, request
import random
import pathlib
from sqlalchemy import insert

cwd = os.getcwd() # Get current working directory
files = os.listdir(cwd) # Get all files in that directory
# print ("Files in %r:%s" % (cwd, files))
    # Implement skill rating management , and quiz generation

class create_user_quiz:
    # getting the correct questions IN PYTHON FIRST
    NUM_Q_PER_QUIZ = 5
    USER_DATA = pathlib.Path(__file__).parent / "dummy_user_data.json"
    # QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.json"
    with open("dummy_user_data.json", "r") as json_file:
        obj_data = json.load(json_file)
 
        # getting hold of skills and their ranking from the dictionary
        
        skills = obj_data['Skills']
        skill_ranking = obj_data['Skill Ranking']
            #extracted_data = json_extract[i].values()
            #skills = list(extracted_data)[1]
            #skill_ranking = list(extracted_data)[2]
        print(skills, skill_ranking)

    with open("questions.json","r") as quiz_file: # loading the quiz bank
        obj_quiz = json.load(quiz_file)

        # searching question bank for correct quiz
        for entry in obj_quiz['Bank']:
            topic = entry['Topic']
            questions = entry['questions']

            if topic in skills:
                print(topic, questions)
            
class update_sql:
    # getting user from results json file
    with open("user_results.json","r") as results_file: # loading the quiz bank
        obj_results = json.load(results_file)

    user = obj_results['ID']
    skill_level_result = obj_results['Skill Ranking']

    stmt = (
        insert('user_scores')
        values('User' = user, 'scores' = skill_level_result)
    )

###### GERA WORK ######
# This function returns the skill ratings and Course recomendations
#def display_course():
#    try:
#        cv_file = request.files['cv']
#        skill_ratings=[1,2,3,4,5,6,7,8,9] #Replace this with laras solution
#        courses = CourseGenerator.generate_courses(cv_file, skill_ratings)
#
#        return jsonify({'courses': courses}), 200
#
#    except Exception as e:
#        return jsonify({'error': str(e)}), 500
#####

    pass
