from extract_skills import ExtractSkills
import fitz  # PyMuPDF library for PDF processing
'''
Authors: Gera Jahja

    WIP
    Task: use lang chain here to generate courses

'''
class CourseGenerator:
    def __init__(self):
        pass
    
    def generate_courses(self, cv_file, skill_ratings):
        try:
            detected_skills = ExtractSkills.detect_skills_from_pdf(cv_file) 
            courses = self.generate_course_recommendations(detected_skills)
            return {'courses': courses, 'skill_ratings': skill_ratings}
        except Exception as e:
            return {'error': str(e)}

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
