
import logo from "../assets/VSH_logo.png"
import { useState } from "react"
import LoginForm from "../components/LoginForm"
import SignUpForm from "../components/Signup"

const LoginPage = ({callback}) => {
    const [signUpForm, setSignUpForm] = useState(false);

    const handleChangeForm =()=>{
        setSignUpForm(!signUpForm);
    }

    const loginHandler = (name,pass) => {
        console.log('Username:', name);
        console.log('Password:', pass);
        callback(true)

    };

    const signUpHandler = (name,pass,email) => {
        console.log('Username:', name);
        console.log('Password:', pass);
        console.log('Email:', email);
    };

   
    return (
        <div className="flex flex-row bg-gradient-to-br from-vf-red to-red-600  w-screen h-screen">
            <div className=" items-start">
                <img src={logo} alt={logo} className="w-full h-full"></img>
            </div>
            <div className="flex flex-col bg-white items-center rounded-lg  w-2/6 drop-shadow-lg my-10 mx-10">
                <p className="py-3 text-red-700 text-2xl" > V-Skills Hub</p>
                <div className="w-9/12 mt-3">
                    {signUpForm ? <SignUpForm callback={signUpHandler}/>: <LoginForm callback={loginHandler}/>}
                </div>
                {signUpForm ? 
                    <p className="mt-5">Already have an account? <span onClick={handleChangeForm}className="text-blue-600 underline hover:text-blue-500 ">Login</span></p>
                    :<p className="mt-5">Don't have an account? <span onClick={handleChangeForm}className="text-blue-600 underline hover:text-blue-500 "> Sign Up</span></p>    
            }


            </div>


        </div>
    )
}

export default LoginPage