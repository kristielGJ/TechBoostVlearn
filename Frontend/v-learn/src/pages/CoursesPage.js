import React, { useState } from 'react'
import Course from '../components/Course';
import course1 from "../dummyData/BA.json"
import course2 from "../dummyData/pythonCourse.json"
import course3 from "../dummyData/javaCourse.json"
import logo from "../assets/VSH_logo.png"

const Courses = () => {

  const [recommendedCourses, setReccomendedCourses] = useState([course1, course2, course3])
  const [enrolledCourses, setEnrolledCourses] = useState([])
  const [courseActive, setCourseActive] = useState(false)
  const [currentCourse, setCurrentCourse] = useState(null);

  const handleEnrollment = (value) => {
    const updatedEnrollment = [...enrolledCourses]
    updatedEnrollment.push(value)
    setEnrolledCourses(updatedEnrollment)

    const updatedCourses = recommendedCourses.reduce((acc, course) => {
      if (Object.keys(course)[0] !== Object.keys(value)[0]) {
        acc.push(course);
      }
      return acc;
    }, []);
    setReccomendedCourses(updatedCourses);
    setCourseActive(true)
    setCurrentCourse(value)
  }

  const handleBack = (value) => {
    const updatedCourses = enrolledCourses.reduce((acc, course) => {
      if (Object.keys(course)[0] !== Object.keys(value)[0]) {
        acc.push(course);
      } else {
        acc.push(value)
      }
      return acc;
    }, []);
    setCourseActive(false);
    setEnrolledCourses(updatedCourses)
  }

  const initiateCourse = (value) => {
    setCurrentCourse(value)
    setCourseActive(true);

  }

  const handleSubmit = (value) => { 
    const updatedCourses = enrolledCourses.reduce((acc, course) => {
      if (Object.keys(course)[0] !== Object.keys(value)[0]) {
        acc.push(course);
      } else {
        acc.push(value)
      }
      return acc;
    }, []);
    setCourseActive(false);
    setEnrolledCourses(updatedCourses)
  }
  

  console.log("COURSE ACTIVE :", courseActive)

  return (
    <div className="bg-gradient-to-br from-10% to-80% to-vf-red from-black min-h-screen h-full w screen  py-10 px-10">

      {courseActive ? <div>
        <Course course_layout={currentCourse} backCallback={handleBack} submitCallback={handleSubmit} />
      </div> :

        <div >
          <p className='text-2xl font-bold text-white'>  Recommended Courses</p>
          <div className='flex flex-row bg-white rounded-lg space-x-7 bg-opacity-60'>
            {recommendedCourses.map((value, index) => (
              <div key={index} className='py-5 px-5 shadow-xl w-1/5 bg-white border-black rounded-lg my-10 mx-5 '>
                <p>{Object.keys(value)[0]}</p>
                <div className='flex flex-row mt-2'>
                  <img className="w-20 h-20" alt={"image"} src={logo} />
                  <p className='text-elipses text-xs truncate text-wrap h-20'>{value[Object.keys(value)[0]]["Content"]["Overview"]}</p>
                </div>
                <button
                  className='btn-red mt-2 w-1/2'
                  onClick={() => handleEnrollment(value)} // Pass the entire value object when the button is clicked
                >
                  Enrol
                </button>
              </div>
            ))}
          </div>

          {enrolledCourses && enrolledCourses.length > 0 ?
            <div className='mt-5'>
              <p className='text-2xl font-bold text-white'>  Enrolleded Courses</p>
              <div className='flex flex-row bg-white rounded-lg space-x-7 bg-opacity-60'>




                {enrolledCourses.map((value, index) => (
                  <div onClick={() => initiateCourse(value)} key={index} className='py-5 px-5 shadow-xl w-1/5 bg-white border-black rounded-lg my-10 mx-5'>
                    <p>{Object.keys(value)[0]}</p>
                    <div className='flex flex-row mt-2'>
                      <img className="w-20 h-20" alt={"image"} src={logo} />
                      <p className='text-elipses text-xs truncate text-wrap h-20'>{value[Object.keys(value)[0]]["Content"]["Overview"]}</p>
                      
                    </div>
                    {Object.values(value).every(item => item.Complete) ? (
                        <p className="text-green-500 ml-2">Complete</p>
                      ) : (
                        <p className="text-yellow-500 ml-2">In Progress</p>
                      )}
                  </div>
                ))}


              </div>



            </div> :

            <div></div>}

        </div>
      }
    </div>
  )
}

export default Courses