import React from "react"
import { useRef } from "react"
import gsap from "gsap";
import { useGSAP } from "@gsap/react";
import { Link } from "react-router-dom"
import { HashLink } from "react-router-hash-link";
import LearnPage from "./LearnPage";
import LeaderBoardPage from "./LeaderboardPage";
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
                    <Link ref={text} className="text text-white mt-5 text-2xl text-center border rounded border-white hover:border-black hover:text-red-500 hover:bg-white translate-y-96 " to="/#LeaderBoard"> Learn More</Link>

                </div>
            </div>
            <div>
                <div className="bg-slate-200 mx-10">
                    <h1 className="text-bold text-3xl py-3 px-2">About Platform</h1>
                    <p className="py-3 px-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempor vulputate velit ultricies vulputate. Praesent pulvinar vehicula tempor. Vestibulum commodo efficitur ligula, vitae molestie mi aliquam eu. Phasellus ac neque nibh. Quisque eu orci nec enim posuere congue. Maecenas ornare, nibh quis accumsan ornare, tortor turpis bibendum magna, ac laoreet elit neque et massa. Nulla mauris nunc, suscipit scelerisque tempus vitae, pellentesque eget turpis. Phasellus viverra iaculis tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent vel felis ante. Praesent sed urna ligula. Pellentesque posuere facilisis erat non congue.</p>

                    <h1 className="text-bold text-3xl py-3 px-2">Personalised Content</h1>
                    <p className="py-3 px-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempor vulputate velit ultricies vulputate. Praesent pulvinar vehicula tempor. Vestibulum commodo efficitur ligula, vitae molestie mi aliquam eu. Phasellus ac neque nibh. Quisque eu orci nec enim posuere congue. Maecenas ornare, nibh quis accumsan ornare, tortor turpis bibendum magna, ac laoreet elit neque et massa. Nulla mauris nunc, suscipit scelerisque tempus vitae, pellentesque eget turpis. Phasellus viverra iaculis tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent vel felis ante. Praesent sed urna ligula. Pellentesque posuere facilisis erat non congue.</p>

                    <h1 className="text-bold text-3xl py-3 px-2">How does our model work</h1>
                    <p className="py-3 px-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempor vulputate velit ultricies vulputate. Praesent pulvinar vehicula tempor. Vestibulum commodo efficitur ligula, vitae molestie mi aliquam eu. Phasellus ac neque nibh. Quisque eu orci nec enim posuere congue. Maecenas ornare, nibh quis accumsan ornare, tortor turpis bibendum magna, ac laoreet elit neque et massa. Nulla mauris nunc, suscipit scelerisque tempus vitae, pellentesque eget turpis. Phasellus viverra iaculis tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent vel felis ante. Praesent sed urna ligula. Pellentesque posuere facilisis erat non congue.</p>

                    <h1 className="text-bold text-3xl py-3 px-2">Lorem ipsum</h1>
                    <p className="py-3 px-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempor vulputate velit ultricies vulputate. Praesent pulvinar vehicula tempor. Vestibulum commodo efficitur ligula, vitae molestie mi aliquam eu. Phasellus ac neque nibh. Quisque eu orci nec enim posuere congue. Maecenas ornare, nibh quis accumsan ornare, tortor turpis bibendum magna, ac laoreet elit neque et massa. Nulla mauris nunc, suscipit scelerisque tempus vitae, pellentesque eget turpis. Phasellus viverra iaculis tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent vel felis ante. Praesent sed urna ligula. Pellentesque posuere facilisis erat non congue.</p>

                </div>
            </div>
        </div>
    )
}

export default WelcomePage