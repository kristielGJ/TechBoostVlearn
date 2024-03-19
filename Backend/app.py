#gerajahja@Geras-MacBook-Pro backend % python3.11 app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from cv_parser import CVParser
from course_generator import CourseGenerator

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
CORS(app, resources={r"/detect_skills": {"origins": "*"}})  # Allow CORS for '/detect_skills'

@app.route('/detect_skills', methods=['POST'])
def detect_skills():
    try:
        # Get the uploaded file
        cv_file = request.files['cv']

        # Handle the file and detect skills
        cv_parser = CVParser()
        detected_skills = cv_parser.detect_skills_from_pdf(cv_file)

        # Return the detected skills as JSON response
        return jsonify({'skills': detected_skills}), 200

    except Exception as e:
        # Return error response if an exception occurs
        return jsonify({'error': str(e)}), 500

@app.route('/generate_courses', methods=['POST'])
def generate_courses():
    try:
        # Log the received request data
        app.logger.info("Received POST request to /generate_courses")
        app.logger.info("Request files: %s", request.files)
        app.logger.info("Request form: %s", request.form)

        cv_file = request.files.get('cv')
        skill_ratings = list(map(int, request.form.getlist('skill_ratings[]')))

        # Log the extracted data
        app.logger.info("CV file: %s", cv_file)
        app.logger.info("Skill ratings: %s", skill_ratings)

        # Handle the request and generate course recommendations
        course_generator = CourseGenerator()
        detected_skills = course_generator.cv_parser.detect_skills_from_pdf(cv_file)
        
        # Combine detected skills with skill ratings
        skill_data = [{'skill': skill[0], 'keywords': skill[1], 'ratings': rating}
                      for skill, rating in zip(detected_skills, skill_ratings)]

        response_data = {
            'detected_skills': skill_data,
            'courses': course_generator.generate_courses(detected_skills),
            'skill_ratings': skill_ratings
        }

        # Log the generated response data
        app.logger.info("Generated course recommendations: %s", response_data)

        return jsonify(response_data)

    except Exception as e:
        # Log any exceptions that occur during request processing
        app.logger.error("An error occurred: %s", str(e))
        return jsonify({'error': 'An internal server error occurred.'}), 500
