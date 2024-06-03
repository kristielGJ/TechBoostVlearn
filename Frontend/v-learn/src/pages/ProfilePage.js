import EnrolledCourseInfo from "../components/EnrolledCourseInfo"
import ProfileInfo from "../components/ProfileInfo"
import SkillsInfo from "../components/SkillsInfo"

const ProfilePage = () => {
    return (
        <div className="bg-logo w-screen h-screen  py-10 px-10">
            <div className="grid grid-cols-2 space-x-5">
            <div className=" flex flex-col space-y-5">
                <ProfileInfo />
                <SkillsInfo />
            </div>
            <div>
                <EnrolledCourseInfo/>
            </div>
            </div>

        </div>
    )
}

export default ProfilePage