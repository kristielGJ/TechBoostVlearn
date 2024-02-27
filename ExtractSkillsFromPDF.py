from pdfminer.high_level import extract_text
import re

def detect_skills_from_pdf(pdf_path, sought_out_skills):
    detected_skills = []

    # Convert PDF to text
    with open(pdf_path, 'rb') as file:
        text = extract_text(file)

    # Categories for skills along with additional relevant keywords
    skill_categories = {
        'Digital Marketing': ['Digital Marketing', 'SEO', 'SEM', 'Content Marketing', 'Email Marketing'],
        'Data Analysis': ['Data Analysis', 'Data Visualization', 'Data Mining', 'Statistical Analysis'],
        'Business Analysis': ['Business Analysis', 'Requirement Gathering', 'Process Modeling', 'SWOT Analysis'],
        'Software Development': ['Software Development', 'Programming', 'Agile Methodology', 'Version Control'],
        'Project Management': ['Project Management', 'Risk Management', 'Stakeholder Management', 'Agile Project Management'],
        'Cloud Computing': ['Cloud Computing', 'AWS', 'Azure', 'Google Cloud Platform', 'DevOps'],
        'UX Design': ['User Experience (UX) Design', 'Wireframing', 'Prototyping', 'Usability Testing'],
        'AI/ML': ['Artificial Intelligence (AI)', 'Machine Learning (ML)', 'Deep Learning', 'Natural Language Processing']
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
        'AI/ML': ['Python', 'R', 'Java']
    }

    # Detect skills from the extracted text
    for skill, keywords in skill_categories.items():
        # Check if any keyword for the skill is present in the text
        if any(re.search(r'\b{}\b'.format(keyword), text, re.IGNORECASE) for keyword in keywords):
            detected_skills.append((skill, keywords, language_recommendations.get(skill)))

    return detected_skills

# List of sought-out skills
sought_out_skills = [
    'Digital Marketing',
    'Data Analysis',
    'Business Analysis',
    'Software Development',
    'Project Management',
    'Search Engine Optimization (SEO)',
    'Social Media Marketing',
    'Cloud Computing',
    'User Experience (UX) Design',
    'Artificial Intelligence (AI) and Machine Learning (ML)'
]

# Example usage
pdf_path = 'cv.pdf'  # Change to your PDF file path
skills_found = detect_skills_from_pdf(pdf_path, sought_out_skills)

if skills_found:
    print("Skills detected in the PDF:")
    for skill, keywords, languages in skills_found:
        print("- {} (Related keywords: {})".format(skill, ', '.join(keywords)))
        if languages:
            print("  Recommended programming languages:", ', '.join(languages))
        else:
            print("  No programming language recommendations for this skill category.")
else:
    print("No skills detected in the PDF.")

