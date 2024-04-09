class SkillRatingManager:
    # Implement skill rating management , and quiz generation

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

# This function asks user to self rank themselves in a particular skill
    def user_ranking():
        user_skill_level = input("Please rank yourself from 1 to 5 with how comfortable you are with this skill, 1 being a beginner to 5 being (almost) an expert!")    
        int(user_skill_level) # convert string to an integer

 #   def quiz_generation():

pass
