import avatar from "../assets/image.jpeg"
const ProfileInfo = () => {
    return (
        <div className="bg-white bg-opacity-70 rounded-lg min-h-80  drop-shadow-2xl shadow-red-100 flex flex-row align-center  items-center">
            <div className="pl-10 ">
                <img src={avatar} alt="avatar" className="border rounded-full w-50 h-50" />
            </div>
            <div className="ml-10 ">
                <div className="flex flex-row">
                    <div className=" min-w-52 text-red-600 font-bold text-lg "><h1>Username:</h1></div>
                    <div className="  min-w-52 text-left text-red-600 font-bold text-lg"><h1 >Organisational Role:</h1></div>
                </div>
                <div className="flex flex-row ">
                    <div className="min-w-52  "><h1>Jane Doe</h1></div>
                    <div className="text-left min-w-52 "><h1 >Project Manager</h1></div>
                </div>
                <div className="mt-10"> <h1>jane.doe@vodafone.com</h1></div>

            </div>

        </div>
    )
}

export default ProfileInfo