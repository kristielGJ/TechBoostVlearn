import CourseGenerator from "../components/CourseGenerator"
import logo from "../assets/altLogo.png"

const LearnPage = () => {
    return (
        <div className="grid grid-cols-5 min-h-screen bg-gradient-to-br from-vf-red from-10% via-red-logo via-20% to-red-logo to-90%">
            <div className="col-span-3">
                <CourseGenerator className="col-span-4 p-16 mx-auto  mt-10 boarder rounded boarder-neutral-200 bg-white w-6/12 text-center align-center" />
            </div>
            <div className="col-span-2 h-screen">
                <img className="ill-current h-screen w-screen mr-2 " src={logo} alt="logo" />
            </div>
        </div>
    )
}

export default LearnPage