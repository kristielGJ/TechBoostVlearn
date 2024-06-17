import React, { useEffect } from 'react'
import { useState } from 'react';
import Question from './Question';

const Module = ({ moduleName, ModuleInfo, index, courseCallback }) => {
    const [questionsAnswered, setQuestionsAnswered] = useState([false, false])
    const [score, setScore] = useState([0, 0]);
    const [buttonVisable, setButtonVisable] = useState(false)
    const [moduleComplete,setModuleComplete]= useState(ModuleInfo["Complete"])

    const moduleQuestionCallback = (number, temp) => {
        const newScore = [...score]
        newScore[number] = temp ? 1 : 0;
        const updatedValues = [...questionsAnswered]
        updatedValues[number] = true;
        setQuestionsAnswered(updatedValues);
        setScore(newScore);
    }

    useEffect(() => {
        const completed = questionsAnswered.reduce((acc, current) => acc && current, true);
        setButtonVisable(completed)
    }, [questionsAnswered])

    const handleSubmit =()=>{
        const finalScore=score.reduce((acc,current)=>acc+current,0)
        setModuleComplete(true)
        console.log("KEY ", index)
        courseCallback(moduleName,finalScore ,index)
    
    }

    return (
        (
            <div id={moduleName} key={index} className='h-1/6  my-10 py-5 px-5'>
                <p className={moduleComplete? "text-green-800" : "text-black" + "text-2xl font-bold"}>{moduleName}</p>
                {(Object.keys(ModuleInfo["Content"]).map(data => (
                    <div key={data} className='px-5'>
                        <p className='text-xl font-thin mt-3 '>{data}</p>
                        <p> {ModuleInfo["Content"][data]}</p>

                    </div>

                )))}
                
                {!moduleComplete?
                <div>
                
                {ModuleInfo["Questions"].map((value, index) => (

                    <Question number={index} question={value} callback={moduleQuestionCallback} />
                ))}
                <div className='flex flex-row justify-end'>
                <button
                    disabled={!buttonVisable}
                    className={(buttonVisable) ? "btn-black" : "btn-black-disabled"}
                    onClick={handleSubmit}
                >Submit</button>
                </div>
                </div> : <div></div>}


            </div>
        ))
}

export default Module