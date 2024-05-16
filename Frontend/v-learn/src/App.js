import './App.css';
import NavBar from './components/NavBar';
import { Routes, Route, useNavigate } from "react-router-dom";
import WelcomePage from './pages/WelcomePage';
import LearnPage from './pages/LearnPage';
import ProfilePage from './pages/ProfilePage';
import LeaderBoardPage from './pages/LeaderboardPage';
import Quiz from './pages/Quiz';
import LoginPage from './pages/LoginPage';
import { useState } from 'react';

function App() {
  const [loggedIn,setLoggedIn] = useState(false);
  const navigate = useNavigate();

  const loginHandle =()=>{
    setLoggedIn(true)
    navigate(`/`)
  }

  return (
    <div>
      <div className="bg-gradient-to-t from-red-700 ...">
        <NavBar loggedIn={loggedIn} />
      </div>
      <div>
        <Routes>
          <Route path="/" element={<WelcomePage />}/>
          <Route path="/" element={<LeaderBoardPage/>}/>
          <Route path="/learn" element={<LearnPage />}/>
          <Route path="/profile" element={<ProfilePage />}/>
          <Route path="/leaderboard" element={<LeaderBoardPage />}/>
          <Route path="/quiz" element={<Quiz topic={"Python"}/>}/>
          <Route path="/login" element={<LoginPage callback={loginHandle}/>}/>
        </Routes>
      </div>
    </div>
  );
}

export default App;
