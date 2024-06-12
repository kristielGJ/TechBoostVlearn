
import logo from "../assets/VSH_logo.png"
import { useState } from "react"
import LoginForm from "../components/LoginForm"
import SignUpForm from "../components/Signup"
import axios, { HttpStatusCode } from 'axios';


const LoginPage = ({callback}) => {
    const [signUpForm, setSignUpForm] = useState(false);

    const handleChangeForm =()=>{
        setSignUpForm(!signUpForm);
    }

    const loginHandler = (email,pass) => {
        const formData= new FormData();
        formData.append("email", email)
        formData.append("password", pass)
        axios
        .post('http://localhost:8000/auth/login',formData, {
            headers: {
            'Content-Type': 'multipart/form-data'
            }})
        .then((response)=>{
            if(response.status===HttpStatusCode.Ok){
                callback(response.data.access_token,response.data.id)
            }})
        .catch((error) => {
            console.log(error); })
            
    };

    const signUpHandler = async (name,pass,email) => {
        const formData= new FormData();
        formData.append("username",name)
        formData.append("email", email)
        formData.append("password", pass)
    axios
    .post('http://localhost:8000/users/create',formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }})
    .then((response)=>{
        if(response.status===HttpStatusCode.Ok){
            setSignUpForm(false);
        }})
    .catch((error) => {
        console.log(error); })
        
        
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