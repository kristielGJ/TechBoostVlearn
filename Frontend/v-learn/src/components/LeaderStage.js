import bronzemedal from "../assets/bronze_medal.png"
import silvermedal from "../assets/silver_medal.png"
import goldmedal from "../assets/gold_medal.png"

const Stage = (props) => {
    console.log(props)
    switch (props.index) {
        case 0:
            return (
                    
                <div className="flex flex-row justify-center items-center bg-gray-200 shadow-lg  max-h-12 rounded px-3 py-3">
                    <img className="max-h-12 max-w-12" src={bronzemedal} alt="bronze"></img>
                    <p className="text-right">{props.username}</p>
                </div>)
        case 1:
            return (
                <div className="flex flex-row justify-center items-center bg-gray-400 shadow-lg rounded max-h-20 min-w-min px-3 py-3">
                    <img className="max-h-20 max-w-20" src={goldmedal} alt="gold"></img>
                    <p className="text-right">{props.username}</p>
                </div>)
        case 2:
            return (
                <div className="flex flex-row justify-center items-center bg-gray-300  max-h-16 shadow-lg rounded  px-3 py-3">
                    <img className="max-h-16 max-w-16" src={silvermedal} alt="silver"></img>
                        <p className="text-right">{props.username}</p>
                </div>)
    }

}

export default Stage