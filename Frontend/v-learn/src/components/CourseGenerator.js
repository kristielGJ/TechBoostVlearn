import React, { useState } from 'react';
import axios from 'axios';

const CourseGenerator = () => {
  const [cvFile, setCvFile] = useState(null);
  const [cvText, setCvText] = useState('');
  const [error, setError] = useState(null);

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

      const { text, error } = response.data;
      if (error) {
        setError(error);
      } else {
        setCvText(text);
      }
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

  return (
    <div>
      <h2>Upload your CV</h2>
      <input type="file" accept=".pdf,.doc,.docx" onChange={handleCVUpload} />
      <button onClick={handleGenerateRecommendations}>Generate Recommendations</button>
      {error && <p>Error: {error}</p>}
      {cvText && (
        <div>
          <h2>PDF Text:</h2>
          <pre>{cvText}</pre>
        </div>
      )}
    </div>
  );
};

export default CourseGenerator;
