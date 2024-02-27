from pdfminer.high_level import extract_text # pip install pdfminer.six
import re

def detect_skills_from_pdf(pdf_path):
    skill_keywords = [
        'Python', 'Java', 'C++', 'JavaScript', 'HTML', 'CSS',
        'Machine Learning', 'Data Science', 'Database Management', 'SQL',
        'Web Development', 'Mobile Development', 'Cloud Computing',
        'Problem Solving', 'Communication', 'Teamwork'
        # Add more skill keywords as needed 

    ]
    
    detected_skills = []

    # Extract text from PDF
    text = extract_text(pdf_path)

    # Detect skills from the extracted text
    for skill in skill_keywords:
        # Use regular expression to find matches (case-insensitive)
        if re.search(r'\b{}\b'.format(skill), text, re.IGNORECASE):
            detected_skills.append(skill)

    return detected_skills

# Example usage
pdf_path = 'cv.pdf'
skills_found = detect_skills_from_pdf(pdf_path)

if skills_found:
    print("Skills detected in the PDF:")
    for skill in skills_found:
        print("- ", skill)
else:
    print("No skills detected in the PDF.")
