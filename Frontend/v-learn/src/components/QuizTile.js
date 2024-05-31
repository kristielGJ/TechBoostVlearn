import React from 'react'
import { Link } from 'react-router-dom'
import Card from 'react-bootstrap/Card';
import logo from "../assets/vfLogo.png"
const QuizTile = ({callback, index,skill}) => {
  const handleClick = ()=>{
    callback(index);
  }

  return (
    <div onClick={handleClick} className={`bg-white w-80 h-64 mx-3 my-3 rounded-lg ${skill.complete? 'pointer-events-none':''}`}>
            <img className={"w-48 h-40"} src={logo} alt={'logo'}></img>
            <p className='text-xl font-bold pl-5 '>{skill.name}</p>
            <div className='flex flex-row space-x-1.5'>
            <p className='italic text-slate-500 pl-5'>Level:  {skill.value}</p>
            {skill.complete ? 
            <p className='text-green-400 text-bold'> Complete</p> : 
            <p className='text-red-700 text-bold'> Incomplete</p>
            }

            </div>
            
    
    </div>
  )
}

export default QuizTile