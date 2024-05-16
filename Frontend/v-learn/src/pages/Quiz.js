
import axios from "axios"
import React, { useState, useEffect } from "react"
import { json } from "react-router-dom"
import Question from "../components/Question"

const ScoreCard=({value})=>{
   
    switch(value){
        case 0:
            return(
            <div>
                SCORE Fail = {value}
            </div>)
        case 0.2:
            return(
                <div>
                    SCORE Bad = {value}
                </div>)
        case 0.4:
            return(
                <div>
                    SCORE Low = {value}
                </div>)
        case 0.6: 
            return(
                <div>
                    SCORE Average = {value}
                </div>)  
        case 0.8:
            return(
                <div>
                    SCORE Good = {value}
                </div>)
        case 1:
            return(
                <div>
                    SCORE Perfect = {value}
                </div>)
    }
}

const Quiz = ({ topic }) => {
    const [quizQuestions, setQuizQuestions] = useState([])
    const [quizName, setQuizName] = useState("")
    const [dataRetrieved, setDataRetrieved] = useState(false)
    const [responses,  setResponses]=useState([false,false,false,false,false])
    const [quizIncomplete, setQuizIncomplete] = useState(true)
    const [score,setScore]=useState(0)

    useEffect(() => {
        fetchData()
    }, [])

    const fetchData = async () => {

        try {
            const response = await axios.get('http://localhost:8000/quiz')
            setQuizQuestions(response.data.questions)
            setQuizName(response.data.quizContext)
            setDataRetrieved(true)
        }
        catch (error) {
            console.log("Error fetching data", error)
        }
    }

    const ParentCallback =(number, answer)=>{
        const newAnswer=[...responses]
        newAnswer[number]=answer
        setResponses(newAnswer)
    }

    const handleClick =() =>{
        const correctResponses=responses.reduce((count, currentValue) => {
            return count + (currentValue ? 1 : 0);
          }, 0);
        setScore(correctResponses/responses.length)
        setQuizIncomplete(false)
        
    }
    


    return (
        
        <div className="flex flex-col min-h-screen bg-gradient-to-br from-vf-red to-red-700 ">
            <div className="text-3xl text-white">
                {dataRetrieved ? quizName: topic}
                {quizIncomplete? quizQuestions.map((item, index) => (
                <div key={index}>
                <Question number={index} question={item} callback={ParentCallback} />
                </div>
                )): <ScoreCard value={score}/>
                }
            </div>
            {quizIncomplete && <div>
                <button onClick={handleClick}> Submit</button>
            </div>}

        </div>
    )
}

export default Quiz