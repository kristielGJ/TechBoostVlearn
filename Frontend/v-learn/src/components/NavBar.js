import React, { useState } from 'react';
import logo from "../assets/vfLogoW.png"
import { Link } from 'react-router-dom';
const NavBar = () => {
    return (
        <nav class="flex items-center justify-between flex-wrap bg-black p-6">
            <div class="flex items-center flex-shrink-0 text-white mr-6">
                
                <Link to="/" class="flex flex-row">
                <img className="ill-current h-12 w-20 mr-2 "src={logo} alt="logo"/>
                <h1 className="text-xl font-semibold place-self-center">V-Learn</h1>
                </Link>
            </div>
            <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
                <div class="text-sm lg:flex-grow">
                    <Link to="/learn" class="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-red-500 mr-4">
                        Learn
                    </Link>
                    <Link to="/leaderboard" className='block mt-4 lg:inline-block lg:mt-0 text-white hover:text-red-500 mr-4'> Leader Board</Link>
                    

                </div>
                <div>
                    <Link to="/profile" class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-red-500 hover:bg-white mt-4 lg:mt-0">Profile</Link>
                </div>
            </div>
        </nav>
    )
}
export default NavBar