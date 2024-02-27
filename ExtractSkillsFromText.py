import re  # Import the regular expression module

def detect_skills(text):
    # Define a list of skill keywords
    skill_keywords = [
        'Python', 'Java', 'C++', 'JavaScript', 'HTML', 'CSS',
        'Machine Learning', 'Data Science', 'Database Management', 'SQL',
        'Web Development', 'Mobile Development', 'Cloud Computing',
        'Problem Solving', 'Communication', 'Teamwork'
        # Add more skill keywords as needed
    ]
    
    detected_skills = []  # Initialize an empty list to store detected skills
    
    # Iterate through each skill keyword and check for matches in the text
    for skill in skill_keywords:
        # Use regular expression to find matches (case-insensitive)
        if re.search(r'\b{}\b'.format(skill), text, re.IGNORECASE):
            detected_skills.append(skill)  # If a match is found, add the skill to the list
    
    return detected_skills  # Return the list of detected skills

def main():
    # Read text from a file
    file_path = 'resume.txt' 
    with open(file_path, 'r') as file:
        text = file.read()

    # Detect skills
    skills_found = detect_skills(text)
    
    # Print skills
    if skills_found:
        print("Skills detected in the text:")
        for skill in skills_found:
            print("- ", skill)
    else:
        print("No skills detected in the text.")

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
