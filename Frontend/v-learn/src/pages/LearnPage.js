import { useState } from "react";
import CourseGenerator from "../components/CourseGenerator"
import QuizPage from '../components/QuizPage'
import Interest from "../components/Interest";
import axios, { HttpStatusCode } from "axios";


const LearnPage = () => {
    const [index, setIndex] = useState(0);
    const [skills, setSkills] = useState();
    const [advancedSkills, setAdvancedSkills] = useState();
    const [jobs, setJobs] = useState([]);
    const [interests, setInterests] = useState([]);
    const [category, setCategory] = useState([]);




    const handleRatingsSubmit = (skills) => {
        const uuid = localStorage.getItem("user_id")
        Object.keys(skills).forEach((key) => {
            const formData= new FormData;
            formData.append("skill_name", key)
            formData.append("rating",skills[key])
            axios
            .post("http://127.0.0.1:8000/users/"+uuid+"/skills",formData)
            .then((response)=>{
                if(response.status===HttpStatusCode.Ok){
                    console.log("Skill Added ", key)
                } 
            })
            .catch((error)=>{
                console.log(error)
            })
        })
        const filteredSkills = Object.fromEntries(
            Object.entries(skills).filter(([key, value]) => value >= 3)
        );

        const updatedSkillsObject = Object.entries(filteredSkills).map(([skill, value]) => ({
            name: skill,
            value,
            complete: false,
            score: 0,
        }));
        setSkills(skills)
        setAdvancedSkills(updatedSkillsObject)
        handleNext()
    }

    const quizStateNextHandle = (data) => {
        setAdvancedSkills(data)
        handleNext()
    }


    const handleBack = () => {
        console.log("back called")
        const val = (index === 0) ? 0 : index - 1
        setIndex(val)
    }

    const handleNext = () => {
        const val = (index === 2) ? 2 : index + 1
        setIndex(val)
    }

    const handleInterestBack = (jobs, interest, category) => {
        setInterests(interests);
        setJobs(jobs);
        setCategory(category)
        handleBack();
    }




    let test =
        [<CourseGenerator skillCallback={handleRatingsSubmit} className="flex p-16 mx-auto  mt-10 boarder rounded boarder-neutral-200 h-1/2  border" />,
        <QuizPage advSkills={advancedSkills} back={handleBack} next={quizStateNextHandle} />,
        <Interest back={handleInterestBack} jobs={jobs} interests={interests} category={category} />]


    return (
        <div className="flex flex-col items-center min-h-screen bg-gradient-to-br from-10% to-80% to-vf-red from-black ">
            <div className="flex flex-col justify-center items-center bg-slate-50 w-10/12 px-14 py-10 my-10 rounded-lg">
                {test[index]}
            </div>

        </div>
    )
}

export default LearnPage