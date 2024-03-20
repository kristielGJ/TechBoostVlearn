import fitz  # PyMuPDF library for PDF processing
import tempfile

class CourseGenerator:
    def __init__(self):
        pass
    
    def generate_courses(self, cv_file, skill_ratings):
        try:
            temp_cv_path = self.save_temp_cv(cv_file)
            detected_skills = self.detect_skills_from_pdf(temp_cv_path)  # Use PyMuPDF for skill detection
            courses = self.generate_course_recommendations(detected_skills)
            return {'courses': courses, 'skill_ratings': skill_ratings}
        except Exception as e:
            return {'error': str(e)}

    def save_temp_cv(self, cv_file):
        try:
            # Save the uploaded CV to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_cv_path = temp_file.name
                cv_file.save(temp_cv_path)
            return temp_cv_path
        except Exception as e:
            raise Exception("Error saving temporary CV file:", str(e))

    def detect_skills_from_pdf(self, cv_file_path):
        try:
            detected_skills = []

            # Open the PDF file
            pdf_document = fitz.open(cv_file_path)

            # Iterate through pages and extract text
            for page_number in range(len(pdf_document)):
                page = pdf_document.load_page(page_number)
                text = page.get_text()

                # Extract skills using regex or any other method
                # For demonstration, let's assume we're extracting skills like 'Data Analysis' and 'Software Development'
                if 'Data Analysis' in text:
                    detected_skills.append(('Data Analysis',))
                if 'Software Development' in text:
                    detected_skills.append(('Software Development',))

            pdf_document.close()
            return detected_skills
        except Exception as e:
            raise Exception("Error detecting skills from PDF:", str(e))

    def generate_course_recommendations(self, detected_skills):
        try:
            courses = []
            for skill, _, _, _ in detected_skills:
                # Generate course recommendations based on detected skills
                if skill == 'Data Analysis':
                    courses.append('Data Analysis with Python Course')
                elif skill == 'Software Development':
                    courses.append('Python Programming Course')
                    courses.append('JavaScript Basics')
                # Add more recommendations for other skills here as needed
            return courses
        except Exception as e:
            raise Exception("Error generating course recommendations:", str(e))
