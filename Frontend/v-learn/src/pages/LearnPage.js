import CourseGenerator from "../components/CourseGenerator"
import { Link } from "react-router-dom"

const LearnPage = () => {
    return (
        <div className="grid grid-cols-5 min-h-screen bg-gradient-to-br from-vf-red to-red-600 ">
            <div className="col-span-3">
                <CourseGenerator className="col-span-4 p-16 mx-auto  mt-10 boarder rounded boarder-neutral-200 bg-white w-6/12 text-center align-center" />
            </div>
            <Link to="/quiz" className="col-span-3">
                <button> Press Me </button>
            </Link>
            
        </div>
    )
}

export default LearnPage