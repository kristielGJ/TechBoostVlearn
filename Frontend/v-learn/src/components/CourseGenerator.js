// npm start
import React from 'react';
import axios from 'axios';

class CourseGenerator extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      courses: [],
      skillRatings: {},
      cvFile: null,
      detectedSkills: [] // Add a new state to store detected skills
    };
  }

  handleCVUpload = (event) => {
    this.setState({ cvFile: event.target.files[0], courses: [], detectedSkills: [] });
  };

  handleSkillRatingChange = (event, skill) => {
    const newSkillRatings = { ...this.state.skillRatings };
    newSkillRatings[skill] = parseInt(event.target.value);
    this.setState({ skillRatings: newSkillRatings });
  };

  detectSkillsFromPDF = async (cvFile) => {
    console.log('Detecting skills from PDF...');
    try {
      const formData = new FormData();
      formData.append('cv', cvFile);

      const response = await axios.post('http://127.0.0.1:5000/detect_skills', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      const skills = response.data.detected_skills || [];
      console.log('Skills detected:', skills);
      this.setState({ detectedSkills: skills }); // Update detected skills in state
    } catch (error) {
      console.error('Error detecting skills:', error);
    }
  };

  generateCourseRecommendations = async () => {
    console.log('Generating course recommendations...');
    if (!this.state.cvFile) {
      console.error('No CV file uploaded.');
      return;
    }

    try {
      await this.detectSkillsFromPDF(this.state.cvFile);

      // Proceed with generating course recommendations based on detected skills...
    } catch (error) {
      console.error('Error generating course recommendations:', error);
    }
  };  
  
  render() {
    return (
      <div>
        <h2>Upload your CV</h2>
        <input type="file" accept=".pdf,.doc,.docx" onChange={this.handleCVUpload} />
        <h2>Rate Your Skills:</h2>
        <ul>
          {this.state.detectedSkills.map((skill, index) => (
            <li key={index}>
              {skill.skill}: <input type="number" min="1" max="5" value={this.state.skillRatings[skill.skill] || ''} onChange={(e) => this.handleSkillRatingChange(e, skill.skill)} />
            </li>
          ))}
        </ul>
        <button onClick={this.generateCourseRecommendations}>Generate Course Recommendations</button>
        <h2>Recommended Courses:</h2>
        <ul>
          {this.state.courses.map((course, index) => (
            <li key={index}>{course}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default CourseGenerator;
