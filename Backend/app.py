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
from flask import Flask, request, jsonify
from flask_cors import CORS
from cv_parser import CVParser
from course_generator import CourseGenerator

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

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


if __name__ == "__main__":
    app.run(port=8000, debug=True) # In some cases you may get errors, try changing the port number if your app is not working
