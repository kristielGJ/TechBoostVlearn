

const EnrolledCourseInfo = () => {

    
    
    return (
    
        <div className="bg-white bg-opacity-70 rounded-lg min-h-80  drop-shadow-2xl shadow-red-100 flex flex-col align-center  ">
            <h1 className="text-red-600 text-2xl font-semibold place-self-start ml-10 mt-5"> Enrolled Courses</h1>
            <ul className="ml-10 mt-5 space-y-5 mb-10">
                <li className="ml-14 pr-10">
                    <h1 className="text-l font-semibold"> Python 301</h1>
                    <p>Advance your Python skills with our intermediate course, exploring topics like object-oriented programming, data structures, algorithms, and practical application development.</p>
                </li>

                <li className="ml-14 pr-10">
                    <h1 className="text-l font-semibold"> Python for Data Analytics</h1>
                    <p>Level up your Python proficiency with our data analytics-focused course, leveraging powerful libraries like pandas for data manipulation, visualization, statistical analysis, and machine learning techniques."</p>
                </li>

                <li className="ml-14 pr-10">
                    <h1 className="text-l font-semibold"> React: Build your First App</h1>
                    <p>Dive into web development with our beginner-friendly React course, covering fundamental concepts such as component-based architecture, state management, JSX syntax, and building interactive user interfaces.</p>
                </li>
               
            </ul>
        </div>

    )
}

export default EnrolledCourseInfo