import CourseGenerator from "../components/CourseGenerator"
import { Link, useNavigate } from "react-router-dom"


const LearnPage = () => {
    const navigate = useNavigate();


    const handle = (skills) => {
        console.log("found", skills);
        const advancedSkills = Object.fromEntries(
            Object.entries(skills).filter(([key, value]) => value >= 3)
        );
        const beginnerSkills = Object.fromEntries(
            Object.entries(skills).filter(([key, value]) => value < 3)
        );
        const arrayfromList = Object.keys(advancedSkills)
        if (arrayfromList.length > 0) {
            navigate("/quizzes", { state: { skill: advancedSkills } });
        } else {
            //TODO PUSH VALUES TO BACKEND
            console.log("No Quiz Needed")
        }
    }

    return (
        <div className="flex flex-col min-h-screen bg-gradient-to-br from-vf-red to-red-600 ">
            <div className="flex flex-row  justify-center items-center">
                <CourseGenerator callback={handle} className="flex p-16 mx-auto  mt-10 boarder rounded boarder-neutral-200 bg-white h-1/2 text-center align-center" />
            </div>

        </div>
    )
}

export default LearnPage