import { useState } from "react";
const LoginForm = ({callback}) =>{
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit =(event) =>
    {
        event.preventDefault();
        callback(email,password)
    }
    
    return(
        <form onSubmit={handleSubmit} className="w-full">
            <div className="mb-4">
                <label className=" mb-2 text-sm font-medium text-gray-700" htmlFor="email">
                    E-mail
                </label>
                <input
                    id="email"
                    type="text"
                    className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-blue-300"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
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
            <button
                type="submit"
                className="w-full px-4 py-2 font-semibold text-white bg-red-700 rounded-lg hover:bg-red-800 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75"
            >
                Login
            </button>
        </form>
    )

}
export default LoginForm