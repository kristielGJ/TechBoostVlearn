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
                match skill:

                    case 'Data Analysis':
                        courses.append('Data Analysis with Python Course')
                    
                    case'Software Development':
                        courses.append('Python Programming Course')
                        courses.append('JavaScript Basics')

                    case 'Digital Marketing':
                        courses.append('Digital Marketing Intorduction Course')
                    
                    case 'Business Analysis':
                        courses.append('Business Analysis Intorduction Course')
                    
                    case 'Project Management':
                        courses.append('Project Management Intorduction Course')
                    
                    case 'Cloud Computing':
                        courses.append('Cloud Computing Intorduction Course')
                    
                    case 'UX Design':
                        courses.append('UX Design Intorduction Course')
                    
                    case 'AI/ML':
                        courses.append('AI/ML Intorduction Course')
                    
                    case'Sales':
                        courses.append('Sales Intorduction Course')
                    
                    case 'Marketing':
                        courses.append('Marketing Intorduction Course')
                    
                    case 'Languages':
                        courses.append('French Intorduction Course')
                        courses.append('Spanish Intorduction Course')
                        courses.append('Mandarin Intorduction Course')
                # Add more recommendations for other skills here as needed
            return courses
        except Exception as e:
            raise Exception("Error generating course recommendations:", str(e))
