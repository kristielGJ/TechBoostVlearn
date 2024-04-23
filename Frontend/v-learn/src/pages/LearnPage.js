import CourseGenerator from "../components/CourseGenerator"
import logo from "../assets/altLogo.png"

const LearnPage = () => {
    return (
        <div className="grid grid-cols-5 min-h-screen bg-gradient-to-br from-vf-red to-red-700 ">
            <div className="col-span-3">
                <CourseGenerator className="col-span-4 p-16 mx-auto  mt-10 boarder rounded boarder-neutral-200 bg-white w-6/12 text-center align-center" />
            </div>
            
        </div>
    )
}

export default LearnPage