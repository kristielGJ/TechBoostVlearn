import { useEffect, useState } from "react"
import React from 'react'
import roles from "../assets/roles.json"
import topics from "../assets/topics.json"
import axios, { HttpStatusCode } from "axios"
import { useNavigate } from "react-router-dom"

const Interest = ({back,jobs,interests,category}) => {
    const [selectedCategories, setSelectedCategories] = useState(category);
    const [selectedJobs, setSelectedJobs] = useState(jobs);
    const [selectedTopics, setSelectedTopics] = useState(interests);
    const [minSelectedTopic, setMinSelectedTopic] = useState(false)
    const [minSelectedJob, setMinSelectedJob] = useState(false)
    const navigate = useNavigate()

    useEffect(() => {
        setMinSelectedJob(selectedJobs.length >= 1)
    }, [selectedJobs])

    useEffect(() => {
        setMinSelectedTopic(selectedTopics.length >= 5);
    }, [selectedTopics])

    const handleSubmit = () => {
        const formData = new FormData();
        formData.append("jobs", selectedJobs.toString())
        formData.append("interests", selectedTopics.toString())
        const uid = localStorage.getItem("user_id")

        axios
            .put("http://localhost:8000/users/update/" + uid, formData)
            .then((response) => {
                if (response.status === HttpStatusCode.Ok) {
                    navigate("/")
                }
            })
            .catch((error) => {
                console.log(error);
            })
    }

    const handleCategoryCheckboxChange = (category) => {
        const updatedCategories = selectedCategories.includes(category)
            ? selectedCategories.filter(item => item !== category)
            : [...selectedCategories, category];
        setSelectedCategories(updatedCategories);

    };


    const handleJobCheckboxChange = (job) => {
        if (selectedJobs.includes(job)) {
            setSelectedJobs(selectedJobs.filter(item => item !== job));
        } else {

            setSelectedJobs([...selectedJobs, job]);

        }

    };

    const handleTopicButtonClick = (topic) => {
        if (selectedTopics.includes(topic)) {
            setSelectedTopics(selectedTopics.filter(item => item !== topic));
        } else {

            setSelectedTopics([...selectedTopics, topic]);
        }
    };

    const categories = Object.keys(roles)


    const Stepper = () => {
        return (
            <ol class="flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 sm:text-base">
                <li class="flex md:w-full items-center text-red-600 dark:text-red-500 sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
                    <span class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                        <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                        </svg>
                        Skills <span class="hidden sm:inline-flex sm:ms-2">Info</span>
                    </span>
                </li>

                <li class="flex md:w-full items-center text-red-600 dark:text-red-500 after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
                    <span class="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                        <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                        </svg>
                        Skill  <span class="hidden sm:inline-flex sm:ms-2">Assesment</span>
                    </span>
                </li>
                <li class="flex items-center  text-red-600 dark:text-red-500">
                    <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 me-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z" />
                    </svg>        Interests
                </li>
            </ol>
        )
    }

    const handleBack = ()=>{
        back(selectedJobs,selectedTopics,selectedCategories)
    }

    console.log(minSelectedTopic, selectedTopics.length, selectedTopics, minSelectedJob, selectedJobs.length, selectedJobs)

    return (

        <div className='w-full '>
            <Stepper />

            <div className="py-5">

                <h2 className="text-2xl font-bold">Categories</h2>
                <div className="flex flex-row space-x-5">
                    {categories.map(category => (
                        <div key={category}>
                            <input
                                type="checkbox"
                                id={category}
                                value={category}
                                checked={selectedCategories.includes(category)}
                                onChange={() => handleCategoryCheckboxChange(category)}
                            />
                            <label htmlFor={category}>{category}</label>
                        </div>
                    ))}
                </div>
                <h2 className="text-2xl font-bold">Jobs</h2>
                {selectedCategories.map(category => (
                    <div className=" space-y-1" key={category}>
                        <h3 className="text-xl my-5">{category}</h3>
                        <div className="flex flex-wrap  space-between-5 space">
                            {roles[category].sort().map(job => (
                                <div key={job}>
                                    <button onClick={() => handleJobCheckboxChange(job)}
                                        className={selectedJobs.includes(job) ? "role-btn-green" : "role-btn-blue"}>{job}{selectedJobs.includes(job) ? " x " : " + "}  </button>
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
                <h2 className="text-2xl font-bold">Topics</h2>
                {selectedCategories.map(category => (
                    <div className=" space-y-1" key={category}>
                        <h3 className="text-xl my-5">{category}</h3>
                        <div className="flex flex-wrap  space-between-5 space">
                            {topics[category].sort().map(topic => (
                                <div key={topic}>
                                    <button onClick={() => handleTopicButtonClick(topic)}
                                        className={selectedTopics.includes(topic) ? "role-btn-green" : "role-btn-blue"}>{topic} {selectedTopics.includes(topic) ? "x" : "+"} </button>
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
                <div className="flex flex-row">
                    <button
                        className="btn-black"
                        onClick = {handleBack}
                    >
                        Back
                    </button>

                    <div className="flex flex-row w-full justify-end">
                        <button
                            disabled={!(minSelectedTopic && minSelectedJob)}
                            className={(minSelectedTopic && minSelectedJob) ? "btn-black" : "btn-black-disabled"}
                            onClick={handleSubmit}
                        >Complete</button>
                    </div>
                </div>
            </div>

        </div>
    )
}

export default Interest