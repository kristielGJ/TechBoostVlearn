/*
MAIN CODE
DO NOT ADD CODE HERE , ONLY DISPLAY COMPONENTS 

Requirements: - Node.js
              - NPM 
      Once node and nop are downloaded , use terninal to navigate to the frontend folder (cd Frontend)
      Type in : npm install   (to download missing files I removed using gitignore, i.e node_modules)          

      To run the app, use the commands:   cd v-learn 
                                          npm start

      MAKE SURE YOU RUN THE BACKEND AND THE FRONTEND TOGETHER 
      OTHERWISE YOU WILL GET ERRORS
      TWO SEPERATE TERMINALS :p

      Expected output:
      
      Compiled successfully!

      You can now view v-learn in the browser.

        Local:            http://localhost:3000
        On Your Network:  http://192.168.0.155:3000

      Note that the development build is not optimized.
      To create a production build, use npm run build.

      webpack compiled successfully

*/
import CourseGenerator from './components/CourseGenerator';

function App() {
  return (
    <div className="App">
      <CourseGenerator />
      {/* Other components or content */}
    </div>
  );
}

export default App;

