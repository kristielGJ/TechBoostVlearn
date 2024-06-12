
import axios from "axios"
import React, { useState, useEffect } from "react"
import Question from "./Question"



const Quiz = ({ topic, rating , callback, index }) => {

    const [quizQuestions, setQuizQuestions] = useState([])
    const [dataRetrieved, setDataRetrieved] = useState(false)
    const [responses,  setResponses]=useState([false,false,false,false,false])
    const [quizIncomplete, setQuizIncomplete] = useState(true)

    useEffect(() => {
        fetchData()
    }, [])

    const fetchData = async () => {

        const url = "http://localhost:8000/quiz?skill=" +topic+"&rating="+rating;
        try {
            const response = await axios.get(url)
            setQuizQuestions(response.data.questions)
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
        setQuizIncomplete(false)
        callback(index,correctResponses/responses.length);
        
    }
    


    return (
        
        <div className="flex flex-col min-h-screen my-5 ">
            <div className="text-3xl text-black">
                {dataRetrieved ? topic : topic}
                {quizIncomplete? quizQuestions.map((item, index) => (
                <div key={index}>
                <Question number={index} question={item} callback={ParentCallback} />
                </div>
                )):<p></p>
                }
            </div>
            {quizIncomplete && <div>
                <button className="btn-black my-5" onClick={handleClick}> Submit</button>
            </div>}

        </div>
    )
}

export default Quiz