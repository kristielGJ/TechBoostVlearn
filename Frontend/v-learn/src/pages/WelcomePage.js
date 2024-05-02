import React from "react"
import { useRef } from "react"
import gsap from "gsap";
import { useGSAP } from "@gsap/react";
import { Link } from "react-router-dom"
import { HashLink } from "react-router-hash-link";
const WelcomePage = () => {
    const container = useRef();
    const text = useRef();


    useGSAP(() => {
        gsap.to(".text", {
            y: 0,
            x: 0,
            delay: 0.5,
            duration: 1
        })
    }, { scope: container })

    return (
        <div className=" bg-logo pb-10">
            <div className=" w-screen h-screen flex flex-col justify-center items-center">
                <div ref={container} className="flex flex-col justify-center items-center">
                    <p ref={text} className="text text-black text-5xl font-bold translate-x-96 ">Welcome to <span className="text-red-300">V</span>-Skills Hub</p>
                    <p ref={text} className="text text-gray-950 mt-5 row-start-4 col-start-2 col-end-5 text-4xl translate-y-96 ">Your Platform to access content tailored to your existing skills and knowledge</p>
                    <HashLink smooth to="/#about" ref={text} className="text text-white mt-5 text-2xl text-center border rounded border-white hover:border-black hover:text-red-500 hover:bg-white translate-y-96 "> Learn More</HashLink>

                </div>
            </div>
            <div id="about" className="py-10 px-10">
                <div className="bg-slate-200 ">
                    <h1 className="text-bold text-3xl py-3 px-2">About Platform</h1>
                    <p className="py-3 px-3">The V-Skills Hub Education Platform generates personalised content for upskilling purposes, based on a user’s CV, skills and career progression preferences. Presently, there is a plethora of information on education platforms internally and externally, such as Percipio or YouTube, but no simple way to quickly and cost effectively construct bespoke non-standard learning pathways. We hope to achieve this using GenAI to analyse user preferences and learning content. </p>

                    <h1 className="text-bold text-3xl py-3 px-2">Personalised Content</h1>
                    <p className="py-3 px-3">Introducing V-Skills Hub, a cutting-edge platform for personalized learning. With V-Skills Hub, each learner gets a tailored educational experience based on their unique strengths and learning style. Our advanced algorithms analyze individual patterns to create personalized content, including quizzes, simulations, and exercises. Whether you're a student or a professional, V-Skills Hub lets you learn at your own pace, your way. Say goodbye to generic education and unleash your full potential with V-Skills Hub today.</p>

                    <h1 className="text-bold text-3xl py-3 px-2">How does our model work</h1>
                    <p className="py-3 px-3">Using the current preprocessing model, we: </p>
                    <ul  className="list-disc py-1 px-5">
                        <li>Parse and split the material </li>
                        <li>Map into a vector database  </li>
                        <li>With the prompt + template, use langchain and Azure OpenAI to generate a response  </li>
                    </ul>
                    
                </div>
            </div>
        </div>
    )
}

export default WelcomePage