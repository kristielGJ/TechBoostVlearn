'''
Authors: Gera Jahja
!MAIN CODE!

This runs the flask app, please cd to this folder in your terminal, ensure you are in the backend folder 
Requirements: - Python, the code is compatible with Python 3.x versions. 
                Please use pip to install the libraries once python is downloaded:

                In terminal ---->  pip install Flask flask-cors pdfminer.six chardet PyMuPDF
                
                - Flask: A micro web framework for building web applications.
                - Flask-CORS: An extension for Flask that allows cross-origin resource sharing (CORS) with AJAX requests.
                - pdfminer.six: A PDF parsing library.
                - chardet: A character encoding detection library.
                - PyMuPDF: A library for PDF processing.

Additional libraries added: pip install flask_sqlalchemy                
Expected output:

* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 118-649-118
'''
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os
from cv_parser import CVParser
from course_generator import CourseGenerator
from database import db
from generate_quiz import QuizGenerator
from users.routes import users
from auth.routes import auth

app = Flask(__name__)
app.register_blueprint(users)
app.register_blueprint(auth)
CORS(app)  # Allow CORS for all routes

# configure the SQLite database, and JWT keys
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

load_dotenv()

jwt_secret_key = os.getenv("JWT_SECRET_KEY")
secret_key = os.getenv("SECRET_KEY")

if jwt_secret_key is None or secret_key is None:
    print("Please set the JWT_SECRET_KEY and SECRET_KEY environment variables")
    exit(1)

app.config["SECRET_KEY"] = jwt_secret_key
app.config["JWT_SECRET_KEY"] = secret_key
app.config["JWT_TOKEN_LOCATION"] = ["headers"]

# initialize the app with the extension
db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    from model import User
    db.create_all()

quiz_gen = QuizGenerator()

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/detect_skills', methods=['POST'])
def detect_skills():
    try:
        cv_file = request.files['cv']
        data=CVParser.extract_text_from_pdf(cv_file)
        text=data[0]
        skills=data[1]
        # Return the extracted text as JSON response, 200 means the code works!
        return jsonify({'text': text,'skills': skills}), 200

    except Exception as e:
        # Return error response if an exception occurs, 500, 430 etc are error codes
        return jsonify({'error': str(e)}), 500

# This function returns the skill ratings and Course recomendations
def display_course():
    try:
        cv_file = request.files['cv']
        skill_ratings=[1,2,3] #Replace this with laras solution
        courses = CourseGenerator.generate_courses(cv_file, skill_ratings)

        return jsonify({'courses': courses}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/quiz', methods=['GET'])
def get_quiz():
   
    skill = request.args.get('skill')
    rating = request.args.get('rating')

    if skill is None or rating is None:
        return jsonify({"error": "Both value1 and value2 are required"}), 400
        
    try:
        quiz_response = quiz_gen.generate_quiz(5, "Multiple-choice", skill)
        return jsonify(json.loads(quiz_response))
    except Exception as e:    
        with open ("quiz_data.json","r") as file:
            result=json.load(file)
        return jsonify(result)





if __name__ == "__main__":
    app.run(port=8000, debug=True) # In some cases you may get errors, try changing the port number if your app is not working
