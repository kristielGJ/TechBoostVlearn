from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tempfile
from cv_parser import CVParser

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes
CORS(app, resources={r"/detect_skills": {"origins": "*"}})  # Allow CORS for '/detect_skills'

@app.route('/detect_skills', methods=['POST'])
def detect_skills():
    try:
        # Receive the CV file from the request
        cv_file = request.files['cv']

        # Extract text from the PDF and detect skills
        text = CVParser.extract_text_from_pdf(cv_file)

        # Return the extracted text as JSON response
        return jsonify({'text': text}), 200

    except Exception as e:
        # Return error response if an exception occurs
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000, debug=True)
