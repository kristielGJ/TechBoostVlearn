import os
import tempfile
from extract_skills import ExtractSkills
import chardet  # Library for character encoding detection
from pdfminer.high_level import extract_text

'''
Authors: Gera Jahja
This code is an initial attempt at detecting skills in a cv, and generating reccomendations with it.
The code interacts with app.py (sends data to the react app on port 3000, the backend is on port 8000)
It uses ExtractSkillsFronPDF.py instead of a database atm.
'''
class CVParser:
    
    def extract_text_from_pdf(cv_file):
        try:
            # Save the uploaded CV to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file_path = temp_file.name
                cv_file.save(temp_file_path)

            with open(temp_file_path, 'rb') as f:
                raw_content = f.read()
                # Detect the encoding 
                encoding = chardet.detect(raw_content)['encoding']
                # Use a default encoding 'utf-8' if not detected
                if encoding is None:
                    encoding = 'utf-8'
                cv_content = raw_content.decode(encoding, errors='ignore')

            skills_data = ExtractSkills.detect_skills_from_pdf(temp_file_path)
            skills_found = skills_data[0]
            skill_Recs = skills_data[1]

            text = ""  #THIS TEXT IS DISPLYED ON THE REACT APP

            if skills_found:
                text += "Skills detected in the PDF:\n"
                for skill, keywords, languages, similar_skills in skill_Recs:
                    text += "- {} (Related keywords: {})\n".format(skill, ', '.join(keywords))
                    if languages:
                        text += "  Recommended programming languages: {}\n".format(', '.join(languages))
                    else:
                        text += "  No programming language recommendations for this skill category.\n"
                    if similar_skills:
                        text += "  Similar skills recommendations: {}\n".format(', '.join(similar_skills))
                    else:
                        text += "  No similar skills recommendations for this skill category.\n"
            else:
                text = "No skills detected in the PDF."

            return [text,skills_found]

        except Exception as e:
            print("An error occurred while extracting text from PDF:", str(e))
            return ""
        finally:
            # Delete the temporary file
            os.unlink(temp_file_path)
