import React, { useState } from 'react';
import logo from "../assets/VSH_logoW.png"

import { Link } from 'react-router-dom';
const NavBar = ({ loggedIn }) => {
    return (
        <nav class="flex items-center justify-between flex-wrap bg-black p-2">
            <div class="flex items-center flex-shrink-0 text-white mr-6">

                <Link to="/" class="flex flex-row">
                    <img className="ill-current h-16 w-18  " src={logo} alt="logo" />
                    <h1 className="text-lg font-semibold place-self-center">V-Skills Hub</h1>
                </Link>
            </div>

            <div class=" flex-grow lg:flex lg:items-center lg:w-auto">
                {loggedIn &&
                    <div class="text-sm lg:flex-grow">
                        <Link to="/learn" class="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-red-500 mr-4">
                            Learn
                        </Link>
                        <Link to="/leaderboard" className='block mt-4 lg:inline-block lg:mt-0 text-white hover:text-red-500 mr-4'> Leader Board</Link>


                    </div>}

                <div className='flex  justify-end flex-grow pr-10'>
                    {loggedIn ? 
                    <Link to="/profile" class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-red-500 hover:bg-white mt-4 lg:mt-0">Profile</Link>
                    : <Link to="/login" class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-red-500 hover:bg-white mt-4 lg:mt-0">Log In</Link>}


                </div>

            </div>
        </nav>
    )
}
export default NavBar