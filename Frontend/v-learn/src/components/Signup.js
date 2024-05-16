import { useState } from "react";
const SignUpForm = ({callback}) =>{

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [passwordTwo, setPasswordTwo] = useState('');

    const handleSubmit =(event) =>{
        event.preventDefault();
        callback(username,password, email)
    }


    return (
        <form onSubmit={handleSubmit} className="w-full">
        <div className="mb-4">
            <label className="block mb-2 text-sm font-medium text-gray-700" htmlFor="password">
                E-mail
            </label>
            <input
                id="password"
                type="password"
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-blue-300"
                value={password}
                onChange={(e) => setEmail(e.target.value)}
                required
            />
        </div>
        <div className="mb-4">
            <label className=" mb-2 text-sm font-medium text-gray-700" htmlFor="username">
                Username
            </label>
            <input
                id="username"
                type="text"
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-blue-300"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
            />
        </div>
        <div className="mb-4">
            <label className="block mb-2 text-sm font-medium text-gray-700" htmlFor="password">
                Password
            </label>
            <input
                id="password"
                type="password"
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-blue-300"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />
        </div>
        <div className="mb-4">
            <label className="block mb-2 text-sm font-medium text-gray-700" htmlFor="password">
                Repeat Password
            </label>
            <input
                id="password"
                type="password"
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-blue-300"
                value={password}
                onChange={(e) => setPasswordTwo(e.target.value)}
                required
            />
        </div>
        <button
            type="submit"
            className="w-full px-4 py-2 font-semibold text-white bg-red-700 rounded-lg hover:bg-red-800 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75"
        >
            Sign Up
        </button>
    </form>
    )

}
export default SignUpForm