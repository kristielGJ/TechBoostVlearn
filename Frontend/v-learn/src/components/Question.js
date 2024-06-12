import React, { useState } from "react";

const Question = ({ number, question, callback}) => {
    const [selectedOption, setSelectedOption] = useState(null);
    const [answerCorrect, setAnswerCorrect] = useState(null)

    const handleOptionChange = (e) => {
        setSelectedOption(e.target.value);
        let temp=e.target.value === question.correctAnswer
        setAnswerCorrect(temp)
        callback(number,temp)
    };


    return (
        <div className="flex flex-col  bg-white border rounded-xl mx-5 max-w-3xl shadow-xl my-10">
            <div className="flex flex-row justify-start items-center text-xl text-gray-500 px-10">
                <p className="">{number + 1}.</p>
                <p className="ml-2">{question.question}</p>
            </div>
            <div className="text-base pl-20 text-black pb-5">
                {Object.entries(question.options).map(([key, value]) => (
                    <div key={key} >
                        <input
                            type="radio"
                            id={`${number}-${key}`}
                            name={`multipleChoice-${number}`}
                            value={key}
                            checked={selectedOption === key}
                            onChange={handleOptionChange}
                        />
                        <label htmlFor={`${number}-${key}`}>{value}</label>
                    </div>
                    
                ))}
            </div>
            


        </div>
    )
}

export default Question