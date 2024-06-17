import React, { useEffect } from 'react'
import { HashLink } from 'react-router-hash-link';
import Module from './Module';
import { useState } from 'react';

const Course = ({ course_layout , backCallback, submitCallback  }) => {

    const topLevelKeys = Object.keys(course_layout);
    const [moduleScores,setModuleScores]=useState(Array(topLevelKeys.length).fill(-1))
    const [courseComplete,setCourseComplete]= useState(false)

    useEffect(()=>{
        const val = topLevelKeys.reduce((acc, current) => 
             acc && course_layout[current]["Complete"]
        , true);
        setCourseComplete(val)
    },[moduleScores])


    const handleSubmit = ()=>{
        submitCallback(course_layout)
    }
    const handleBack = ()=>{
        backCallback(course_layout)
    }


    const callback = (value, score,key )=>{
        console.log(value,score,key);
        const newScores =[...moduleScores]
        newScores[key]=score;
        setModuleScores(newScores)
        course_layout[value]["Score"]=score;
        course_layout[value]["Complete"]=true;

    }



    return (
        <div className='flex flex-col rounded-xl bg-white'>
        <div className='flex flex-row justify-end'>
            <button
            className='mt-5 mr-5 btn-red'
            onClick={handleBack}
            >Back</button>
        </div>
        <div className='flex flex-row '>
            <div className='  pe-6 ' >
                {topLevelKeys.map((value, index) => (
                    <div className={"text-xl  px-5 my-10 text-red-800"} key={index}>
                        <HashLink smooth to={'/courses#' + value}>{value}</HashLink>
                    </div>

                ))}
            </div>

            <div
                class=" my-10  w-0.5  bg-neutral-100 dark:bg-white/10">
            </div>

            <div className=' flex flex-col grow ps-6 px-5 ' >
                {topLevelKeys.map((value, index) =>
                    <Module key={value} moduleName={value} index={index} ModuleInfo={course_layout[value]} courseCallback={callback}/>
                )}


            </div>

            
        </div>
        <div className='flex  justify-center pb-5'>
            <button
                    disabled={!courseComplete}
                    className={(courseComplete) ? "btn-black" : "btn-black-disabled"}
                    onClick={handleSubmit}
                >Complete Course</button>
            </div>
        </div>
    )
}

export default Course