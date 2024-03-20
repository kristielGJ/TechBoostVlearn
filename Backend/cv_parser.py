import os
import tempfile
from ExtractSkillsFromPDF import detect_skills_from_pdf
import chardet  # Library for character encoding detection
from pdfminer.high_level import extract_text

class CVParser:

    @staticmethod
    def extract_text_from_pdf(cv_file):
        try:
            # Save the uploaded CV to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file_path = temp_file.name
                cv_file.save(temp_file_path)

            # Read the content of the temporary file with various encodings
            with open(temp_file_path, 'rb') as f:
                raw_content = f.read()
                # Detect the encoding of the content
                encoding = chardet.detect(raw_content)['encoding']
                # If encoding cannot be detected, use a default encoding like 'utf-8'
                if encoding is None:
                    encoding = 'utf-8'
                # Decode the content using the detected encoding, ignoring errors
                cv_content = raw_content.decode(encoding, errors='ignore')

            # Process the content to detect skills
            skills_found = detect_skills_from_pdf(temp_file_path)

            text = ""

            if skills_found:
                text += "Skills detected in the PDF:\n"
                for skill, keywords, languages, similar_skills in skills_found:
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

            return text

        except Exception as e:
            # Log the exception for debugging
            print("An error occurred while extracting text from PDF:", str(e))
            return ""
        finally:
            # Clean up: Delete the temporary file
            os.unlink(temp_file_path)
