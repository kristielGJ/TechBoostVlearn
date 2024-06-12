import React, { useState, useEffect } from 'react'
import QuizTile from './QuizTile';
import Quiz from './Quiz';
import axios, { all } from 'axios';

const Quizzes = ({ advSkills, back, next }) => {

    const [skills, setSkills] = useState(advSkills);
    const [showQuiz, setShowQuiz] = useState(false);
    const [currentIndex, setCurrentIndex] = useState(null);
    const [allQuizComplete, setAllQuizComplete] = useState(false);

    useEffect(()=>{
        const completed = skills.reduce((acc, current) => acc && current.complete, true);
        setAllQuizComplete(completed);
    },[skills])

    useEffect(()=>{
        const completed = skills.reduce((acc, current) => acc && current.complete, true);
        setAllQuizComplete(completed);
    },[])

    const quizTileCallback = (index) => {
        setShowQuiz(true);
        setCurrentIndex(index);
    }

    
    const quizCallback = (index, score) => {
        setShowQuiz(false);
        const updatedSkills = [...skills]
        const newLevel = (score > 0.6) ? updatedSkills[index].value : updatedSkills[index].value - 1
        updatedSkills[index] = { ...updatedSkills[index], complete: true, score: score, }
        setSkills(updatedSkills);
        
        const formData=new FormData
        formData.append("rating", newLevel)
        let uuid = localStorage.getItem("user_id")
        console.log("NEW LEVEL:" ,newLevel)
        
        axios
        .put("http://127.0.0.1:8000/users/"+uuid+"/skills/"+updatedSkills[index].name,formData)
        .catch((error)=>{console.log(error)})
        

    }

    const goForward = () => {
        next(skills,allQuizComplete)
    }

    const Stepper = () => {
        return (
            <ol class="flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base">
                <li class="flex md:w-full items-center text-red-600 dark:text-red-500 sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
                    <span class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                        <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                        </svg>
                        Skills <span class="hidden sm:inline-flex sm:ms-2">Info</span>
                    </span>
                </li>

                <li class="flex md:w-full items-center  text-red-600 dark:text-red-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
                    <span class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                        <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                        </svg>
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


    return (
        <div className='flex flex-col  h-full w-full  py-10 px-10'>
            <Stepper />

            {showQuiz ?
                <div><Quiz topic={skills[currentIndex].name} rating={skills[currentIndex].value} callback={quizCallback} index={currentIndex} /></div>

                :
                
                <div>
                    {skills.length > 0 ? 
                    <div className='flex flex-wrap flex-row w-5/6'>
                    {skills.map((skill, index) => (<QuizTile callback={quizTileCallback} key={skill.name} skill={skill} index={index} />))}
                </div>
                : <div className='flex justify-center items-center h-60 text-2xl text-center font-bold'> Congratulations on starting your learning journey! Please move ahead. </div>}
                    <div className="flex flex-row flex-start mt-10">
                        <button onClick={back} className='btn-black'>Back</button>
                        <div className=' flex grow flex-row justify-end space-x-5'>
                            <button onClick={goForward} disabled={!allQuizComplete} className='btn-black'>Next</button>
                        </div>

                    </div>
                </div>

            }




        </div>

    )
}

export default Quizzes