from pdfminer.high_level import extract_text
import re

class CVParser:
    def detect_skills_from_pdf(self, cv_file):
        try:
            detected_skills = []

            # Convert PDF to text
            text = self.extract_text_from_pdf(cv_file)

            # Define categories for skills along with additional relevant keywords
            skill_categories = {
                'Digital Marketing': ['Digital Marketing', 'SEO', 'SEM', 'Content Marketing', 'Email Marketing'],
                'Data Analysis': ['Data Analysis', 'Data Visualization', 'Data Mining', 'Statistical Analysis'],
                'Business Analysis': ['Business Analysis', 'Requirement Gathering', 'Process Modeling', 'SWOT Analysis'],
                'Software Development': ['Software Development', 'Programming', 'Agile Methodology', 'Version Control'],
                'Project Management': ['Project Management', 'Risk Management', 'Stakeholder Management', 'Agile Project Management'],
                'Cloud Computing': ['Cloud Computing', 'AWS', 'Azure', 'Google Cloud Platform', 'DevOps'],
                'UX Design': ['User Experience (UX) Design', 'Wireframing', 'Prototyping', 'Usability Testing'],
                'AI/ML': ['Artificial Intelligence (AI)', 'Machine Learning (ML)', 'Deep Learning', 'Natural Language Processing'],
                'Sales': ['Sales', 'Negotiation', 'Client Relationship Management', 'Lead Generation'],
                'Marketing': ['Marketing', 'Brand Management', 'Market Research', 'Advertising'],
                'Languages': ['Languages', 'Fluent in English', 'Spanish Proficiency', 'French (Basic)'],
            }

            # Detect skills from the extracted text
            for skill, keywords in skill_categories.items():
                if any(re.search(r'\b{}\b'.format(keyword), text, re.IGNORECASE) for keyword in keywords):
                    detected_skills.append(skill)

            return detected_skills
        except Exception as e:
            # Log the exception for debugging
            print("An error occurred while detecting skills from PDF:", str(e))
            return []

    def extract_text_from_pdf(self, cv_file):
        try:
            return extract_text(cv_file)
        except Exception as e:
            # Log the exception for debugging
            print("An error occurred while extracting text from PDF:", str(e))
            return ""
