import React, { useState, useEffect } from 'react'
import { useLocation} from 'react-router-dom';
import QuizTile from '../components/QuizTile';
import Quiz from './Quiz';
import { all } from 'axios';

const Quizzes = () => {

    let location = useLocation();
    const [skills, setSkills] = useState([]);
    const [showQuiz,setShowQuiz] = useState(false);
    const [currentIndex, setCurrentIndex]= useState(null);
    const [allQuizComplete,setAllQuizComplete] = useState(false);


    const quizTileCallback = (index) =>{
        setShowQuiz(true);
        setCurrentIndex(index);
    }

    const quizCallback = (index, score) =>{
        setShowQuiz(false);
        const updatedSkills = [...skills]
        const newLevel = (score>0.6) ? updatedSkills[index].value : updatedSkills[index].value-1
        updatedSkills[index]={...updatedSkills[index],complete:true,score:score,}
        setSkills(updatedSkills);
        const completed=updatedSkills.reduce((acc,current)=>acc&&current.complete, true);
        setAllQuizComplete(completed);
        //TODO check if all quiz Complete
        //TODO send SCORE To BACKEND using newLevel      

    }

    useEffect(() => {
        const updatedSkills = Object.entries(location.state.skill).map(([skill, value]) => ({
          name: skill,
          value,
          complete: false,
          score: 0,
        }));
        setSkills(updatedSkills);
      }, []);

    return (
        <div className='flex flex-col bg-logo min-h-screen w-screen  py-10 px-10'>
            {showQuiz?
            <div><Quiz topic={skills[currentIndex].name} rating={skills[currentIndex].value} callback={quizCallback} index={currentIndex}/></div>
            :
            <div className='flex flex-wrap flex-row w-5/6'>
            {skills.map((skill,index) => (<QuizTile callback={quizTileCallback} key={skill.name} skill={skill} index={index}/>))}
            </div>

            }
            {allQuizComplete ? <div>Complete</div> : <div>Incomplete</div>}



        </div>
    )
}

export default Quizzes