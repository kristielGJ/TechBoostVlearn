/*
THIS IS ONE OF THE COMPONENTS DISPLAYED IN THE REACT APP. MAKE CHANGES HERE!
*/

import React, { useState } from 'react';
import axios from 'axios';

const CourseGenerator = () => {
  const [cvFile, setCvFile] = useState(null);
  const [cvText, setCvText] = useState('');
  const [error, setError] = useState(null);
  const [detectedSkills, setDetectedSkills] = useState([]);
  const [skillRatings, setSkillRatings] = useState({});
  const [genCourse, setGenCourse] = useState([]);

  const handleCVUpload = (event) => {
    setCvFile(event.target.files[0]);
  };

  const detectSkillsFromPDF = async () => {
    try {
      const formData = new FormData();
      formData.append('cv', cvFile);

      const response = await axios.post('http://localhost:8000/detect_skills', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      const { text, skills } = response.data;
      console.log('Skills detected:', skills);

      // Update state with detected skills
      setDetectedSkills(skills);
      setCvText(text);
    } catch (error) {
      console.error('Error detecting skills:', error);
      setError('Error detecting skills. Please try again.');
    }
  };

  const handleGenerateRecommendations = async () => {
    if (!cvFile) {
      setError('Please upload a CV file.');
      return;
    }

    await detectSkillsFromPDF();
  };

  const handleSkillRatingChange = (skill, rating) => {
    setSkillRatings({ ...skillRatings, [skill]: rating });
  };
  const getCourses = async () => {
    try {
      const formData = new FormData();
      formData.append('cv', cvFile);

      const response = await axios.post('http://localhost:8000/display_course', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      const { courses } = response.data;
      console.log('Courses detected:', courses);

      // Update state with detected skills
      setGenCourse(courses);
      
    } catch (error) {
      console.error('Error detecting skills:', error);
      setError('Error detecting skills. Please try again.');
    }
    await detectSkillsFromPDF();

  };

  return (
    <div>
      <h2>Upload your CV</h2>
      <input type="file" accept=".pdf" onChange={handleCVUpload} />
      <button onClick={handleGenerateRecommendations}>Generate Recommendations</button>
      {error && <p>{error}</p>}
      {cvText && (
        <div>
          <h2>PDF Text:</h2>
          <pre>{cvText}</pre>
        </div>
      )}
      {detectedSkills && detectedSkills.length > 0 ? (
        <div>
          <h2>Detected Skills:</h2>
          <ul>
            {detectedSkills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
          <h2>Skill Ratings:</h2>
          {detectedSkills.map((skill, index) => (
            <div key={index}>
              <label>{skill}:</label>
              <input
                type="number"
                min="1"
                max="5"
                value={skillRatings[skill] || ''}
                onChange={(e) => handleSkillRatingChange(skill, parseInt(e.target.value))}
              />
            </div>
          ))}
          <h2>Detected Course:</h2>
          <ul>
            {genCourse.map((course, index) => (
              <li key={index}>{course}</li>
            ))}
          </ul>
        </div>
      ) : (
        <p> </p>
      )}
    </div>
  );
};

export default CourseGenerator;
