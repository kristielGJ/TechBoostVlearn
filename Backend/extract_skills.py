from pdfminer.high_level import extract_text
import re
'''
Autors: Gera Jahja

This class compares text in the temp local cv file to the dictionaries bellow,
if present the skill is linked to reccomendations that are then returned
alongside the skill detected.

WIP, could generate this section or put the dictionaries into a database.

'''
class ExtractSkills:
    
    def detect_skills_from_pdf(pdf_path):
        detected_skills = []

        #  PDF to text
        with open(pdf_path, 'rb') as file:
            text = extract_text(file)

        #  categories for skills along with additional relevant keywords
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

        #  programming language recommendations based on skill categories
        language_recommendations = {
            'Digital Marketing': [],
            'Data Analysis': ['Python', 'R', 'SQL'],
            'Business Analysis': [],
            'Software Development': ['Python', 'Java', 'JavaScript', 'C#'],
            'Project Management': [],
            'Cloud Computing': [],
            'UX Design': [],
            'AI/ML': ['Python', 'R', 'Java'],
            'Sales': [],
            'Marketing': [],
            'Languages': []
        }

        #  similar skills recommendations based on skill categories
        similar_skills_recommendations = {
            'Digital Marketing': ['Social Media Marketing', 'Content Writing', 'Google Analytics'],
            'Data Analysis': ['Data Science', 'Business Intelligence', 'Predictive Modeling'],
            'Business Analysis': ['Process Improvement', 'Product Management', 'Requirements Analysis'],
            'Software Development': ['Web Development', 'Mobile Development', 'Software Engineering'],
            'Project Management': ['Agile Methodology', 'Scrum', 'Lean Management'],
            'Cloud Computing': ['DevOps', 'Big Data', 'Serverless Architecture'],
            'UX Design': ['UI Design', 'Interaction Design', 'Information Architecture'],
            'AI/ML': ['Deep Learning', 'Natural Language Processing', 'Computer Vision'],
            'Sales': ['Customer Service', 'Cold Calling', 'Sales Strategy'],
            'Marketing': ['Content Marketing', 'Digital Marketing', 'Brand Management'],
            'Languages': ['Fluent in English', 'Spanish Proficiency', 'French (Basic)']
        }

        for skill, keywords in skill_categories.items():
            # Check if any keyword for the skill is present in the text
            if any(re.search(r'\b{}\b'.format(keyword), text, re.IGNORECASE) for keyword in keywords):
                detected_skills.append((skill, keywords, language_recommendations.get(skill), similar_skills_recommendations.get(skill)))

        return detected_skills
