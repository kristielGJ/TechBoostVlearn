# V-Learn
Generate personalised courses using langchain based on a user's personal experience.

V1.0 - 21/03- Skill detection via CV Upload

# Backend
## app.py (*Backend/app.py*)
This runs the flask app, please cd to this folder in your terminal, ensure you are in the backend folder 
### Requirements: 
- Python, the code is compatible with Python 3.x versions. 
  Please use pip to install the libraries once python is downloaded:

 In terminal ---->  ```pip install Flask flask-cors pdfminer.six chardet PyMuPDF```
                
  - Flask: A micro web framework for building web applications.
  - Flask-CORS: An extension for Flask that allows cross-origin resource sharing (CORS) with AJAX requests.
  - pdfminer.six: A PDF parsing library.
  - chardet: A character encoding detection library.
  - PyMuPDF: A library for PDF processing.

### Expected output: 

```
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 118-649-118
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Frontend
## App.js (*Frontend/v-learn/src/App.js*)
### Requirements:
- Node.js
- NPM 

Once node and npm are downloaded , use terninal to navigate to the frontend folder 
```cd Frontend```
Type in : ```npm install```   (to download missing files I removed using gitignore, i.e node_modules)          

To run the app, use the commands:   ``` cd v-learn 
                                        npm start ```

MAKE SURE YOU RUN THE BACKEND AND THE FRONTEND TOGETHER OTHERWISE YOU WILL GET ERRORS
Ensure you use two seperate terminals like so:

<img width="753" alt="Screenshot 2024-03-21 at 01 37 31" src="https://github.com/kristielGJ/TechBoostVlearn/assets/38893338/7aa7c21a-6485-402b-ab67-fa394964c9ac">


### Expected output: 
```
      Compiled successfully!

      You can now view v-learn in the browser.

        Local:            http://localhost:3000
        On Your Network:  http://192.168.0.155:3000

      Note that the development build is not optimized.
      To create a production build, use npm run build.

      webpack compiled successfully 
```
