import logo from './logo.svg';
import './App.css';
import CourseGenerator from './components/CourseGenerator';
import NavBar from './components/NavBar';
import { Routes, Route } from "react-router-dom";
import WelcomePage from './pages/WelcomePage';
import LearnPage from './pages/LearnPage';
import ProfilePage from './pages/ProfilePage';
import LeaderBoardPage from './pages/LeaderboardPage';
function App() {
  return (
    <div>
      <div className="bg-gradient-to-t from-red-700 ...">
        <NavBar />
      </div>
      <div>
        <Routes>
          <Route path="/" element={<WelcomePage />}/>
          <Route path="/" element={<LeaderBoardPage/>}/>
          <Route path="/learn" element={<LearnPage />}/>
          <Route path="/profile" element={<ProfilePage />}/>
          <Route path="/leaderboard" element={<LeaderBoardPage />}/>
        </Routes>
      </div>
    </div>
  );
}

export default App;
