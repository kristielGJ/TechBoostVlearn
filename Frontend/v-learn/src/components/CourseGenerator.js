/*
THIS IS ONE OF THE COMPONENTS DISPLAYED IN THE REACT APP. MAKE CHANGES HERE!
*/
import Slider from '@mui/material/Slider';

import React, { useState, useCallback } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone'


const CourseGenerator = ({ className, skillCallback }) => {
  const [cvFile, setCvFile] = useState(null);
  const [error, setError] = useState(null);
  const [detectedSkills, setDetectedSkills] = useState([]);
  const [skillRatings, setSkillRatings] = useState({});


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

  const handleRatingSubmit = (event) => {
    event.preventDefault();
    skillCallback(skillRatings);
  }

 

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
      // setCvText(text);
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
  
  const Stepper = () =>{
    return(
        <ol class="flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base">
<li class="flex md:w-full items-center text-red-600 dark:text-red-500 sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
    <span class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
        <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"/>
        </svg>
        Skills <span class="hidden sm:inline-flex sm:ms-2">Info</span>
    </span>
</li>

<li class="flex md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
    <span class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
        <span class="me-2">2</span>
        Skill  <span class="hidden sm:inline-flex sm:ms-2">Assesment</span>
    </span>
</li>
<li class="flex items-center">
    <span class="me-2">3</span>
    Interests
</li>
</ol>
    )
}

const redDisabledSliderStyle = {
  color: 'red', // Change the color to red
  '& .MuiSlider-thumb': {
    // Change the color of the thumb (handle)
    color: 'red',
  },
};

  return (
    <div className=' flex flex-col  justify-start items-start w-full' >
      <Stepper/>
      <div className='flex flex-col items-center w-full mt-5'>
        <h2 className="text-3xl font-bold text-center  ">Upload your CV</h2>
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
        <div className="flex flex-row items-center justify-center mt-7" >

          <button className="btn-black " onClick={handleGenerateRecommendations}>Generate Recommendations</button>
          {cvFile && (<p className='text-right  ml-3'>{cvFile.name}</p>)}
        </div>
      </div>
      {error && <p>{error}</p>}
      
      {detectedSkills && detectedSkills.length > 0 ? (
        <div className="flex flex-col mt-10 w-full">
          
            <p className='text-2xl font-bold  mb-5'> Please rank your skills :</p>
            <form className=" w-full " onSubmit={handleRatingSubmit}>
              <div >
                {detectedSkills.map((skill, index) => (
                  <div className="grid grid-cols-2 my-4 pl-5 " key={index}>
                    <label>{skill}:</label>
                    <Slider
                        
                        defaultValue={1}
                        step={1}
                        min={0}
                        max={5}
                        sx={{
                            width:'80%'
                        }}
                        marks
                        valueLabelDisplay={"auto"}
                        onChange={(e) => handleSkillRatingChange(skill, parseInt(e.target.value))}
                        style={redDisabledSliderStyle}
                    />

                
                  </div>
                ))}
              </div>
              <div className='flex justify-end items-center'>
                <button className="btn-black" type="submit"> Next</button>
              </div>
            </form>
          

        </div>
      ) : (
        <p> </p>
      )}
    </div>

  );
};

export default CourseGenerator;
