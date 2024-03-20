from pdfminer.high_level import extract_text
import re

def detect_skills_from_pdf(pdf_path):
    detected_skills = []

    # Convert PDF to text
    with open(pdf_path, 'rb') as file:
        text = extract_text(file)

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

    # Define programming language recommendations based on skill categories
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

    # Define similar skills recommendations based on skill categories
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

    # Detect skills from the extracted text
    for skill, keywords in skill_categories.items():
        # Check if any keyword for the skill is present in the text
        if any(re.search(r'\b{}\b'.format(keyword), text, re.IGNORECASE) for keyword in keywords):
            detected_skills.append((skill, keywords, language_recommendations.get(skill), similar_skills_recommendations.get(skill)))

    return detected_skills

'''
# List of sought-out skills
sought_out_skills = [
    'Digital Marketing',
    'Data Analysis',
    'Business Analysis',
    'Software Development',
    'Project Management',
    'Cloud Computing',
    'UX Design',
    'AI/ML',
    'Sales',
    'Marketing',
    'Languages'
]

while True:
    try:
        pdf_path = input("Enter the path to the PDF file: ")
        
        skills_found = detect_skills_from_pdf(pdf_path, sought_out_skills)

        if skills_found:
            print("Skills detected in the PDF:")
            for skill, keywords, languages, similar_skills in skills_found:
                print("- {} (Related keywords: {})".format(skill, ', '.join(keywords)))
                if languages:
                    print("  Recommended programming languages:", ', '.join(languages))
                else:
                    print("  No programming language recommendations for this skill category.")
                if similar_skills:
                    print("  Similar skills recommendations:", ', '.join(similar_skills))
                else:
                    print("  No similar skills recommendations for this skill category.")
        else:
            print("No skills detected in the PDF.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
'''