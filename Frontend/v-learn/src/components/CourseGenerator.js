/*
THIS IS ONE OF THE COMPONENTS DISPLAYED IN THE REACT APP. MAKE CHANGES HERE!
*/

import React, { useState, useCallback } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone'


const CourseGenerator = ({ className }) => {
  const [cvFile, setCvFile] = useState(null);
  const [cvText, setCvText] = useState('');
  const [error, setError] = useState(null);
  const [detectedSkills, setDetectedSkills] = useState([]);
  const [skillRatings, setSkillRatings] = useState({});
  const [genCourse, setGenCourse] = useState([]);


  const onDrop = useCallback(acceptedFiles => {
    console.log(acceptedFiles)
    setCvFile(acceptedFiles[0])
    console.log(cvFile)
  }, [])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    maxFiles: 1,
    accept: {
      'application/pdf': ['.pdf']
    }
  })

  // const handleCVUpload = (event) => {
  //   setCvFile(event.target.files[0]);
  //   console.log(event.target.files[0])
  // };

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
    await handleSkillRatingChange();

  };

  return (
    <div >


      <div className='grid grid-cols-4'>
        <h2 className="text-3xl font-bold text-center text-white col-span-4">Upload your CV</h2>
        <div {...getRootProps({
          className: className
        })}>
          <input {...getInputProps()} />
          {
            isDragActive ?
              <p>Drop the files here ...</p> :
              <p>Drag 'n' drop your CV as a PDF, or click to select files</p>
          }




        </div>
        <div className="flex flex-row col-start-2 col-end-4 items-center mt-5" >
          <div >
            <button className="boarder rounded-full text-white  bg-black min-h-10 min-w-60 " onClick={handleGenerateRecommendations}>Generate Recommendations</button>
          </div>
          {cvFile && (<p className='text-right col-span-1 ml-3'>{cvFile.name}</p>)}
        </div>
      </div>




      {error && <p>{error}</p>}


      {cvText && (
        <div className="mt-7">
          <h2 className={"text-white"}>PDF Text:</h2>
          <pre className='text-pretty'>{cvText}</pre>
        </div>
      )}
      {detectedSkills && detectedSkills.length > 0 ? (
        <div className="grid grid-cols-2">
          <div>
            <h2 className={"text-white"}>Skills Found:</h2>
            <p > Please  rank your skill level</p>
            {detectedSkills.map((skill, index) => (
              <div className="grid grid-cols-2 mb-3"key={index}>
                <label>{skill}:</label>
                <input
                  className='w-10'
                  type="number"
                  min="1"
                  max="5"
                  value={skillRatings[skill] || ''}
                  onChange={(e) => handleSkillRatingChange(skill, parseInt(e.target.value))}
                />
              </div>
            ))}
          </div>
          <div>
            <h2 className={"text-white"}> Detected Course:</h2>
            <ul>
              {genCourse.map((course, index) => (
                <li key={index}>{course}</li>
              ))}
            </ul>
          </div>
        </div>
      ) : (
        <p> </p>
      )}
    </div>
  );
};

export default CourseGenerator;
