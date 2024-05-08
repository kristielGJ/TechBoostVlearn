import { useEffect, useState } from "react"
import topGlobal from "../dummyData/topTenGlobal.json"
import topTeam from "../dummyData/topTenTeam.json"
import Stage from "../components/LeaderStage"
import PositionTile from "../components/LeaderPosition"

const LeaderBoardPage = () => {
    const [topTenGlobal, setTopTenGlobal] = useState([])
    const [topTenTeam, setTopTenTeam] = useState([])
    const [dataRetrieved, setDataRetrieved] = useState(false)





    useEffect(() => {
        const timer = setTimeout(() => { fetchData() }, 2500)

    }, [])

    const fetchData = async () => {

        try {
            setTopTenGlobal(topGlobal)
            setTopTenTeam(topTeam)
            setDataRetrieved(true)
        }
        catch (error) {
            console.log("Error fetching data", error)
        }
    }

    const topThreeTeam=topTenTeam.slice(0,3)
    let temp = topThreeTeam.pop()
    topThreeTeam.unshift(temp)

    const topThreeGlobal =topTenGlobal.slice(0,3)
     temp = topThreeGlobal.pop()
     topThreeGlobal.unshift(temp)

    return (
        <div className="bg-logo min-h-screen w screen  py-10 px-10">
            <div className="grid grid-cols-2 space-x-5">
                <div className="bg-white rounded-lg">
                    <div  className="w-full flex flex-row justify-center py-3">
                        <p className="font-bold text-2xl">Team Leaderboard</p>
    
                    </div>

                    {dataRetrieved ? (
                        <div className="grid grid-cols-3 space-x-5 pt-10 px-10 items-end">
                            {topThreeTeam.slice(0, 3).map((item, index) => (
                                <Stage key={index} username={item.username} index={index} />
                            ))}
                        </div>

                    ) : (<p></p>)}


                    <div>
                        {dataRetrieved ? (
                            <div className="mt-10">
                                {topTenTeam.map((item, index) => (
                                    <PositionTile key={index} name={item.username} place={index + 1} score={item.Score} />
                                ))}
                            </div>
                        ) : (
                            <p>Loading...</p>)}
                    </div>
                </div>
                <div className="bg-white  rounded-lg">
                <div  className="w-full flex flex-row justify-center py-3">
                        <p className="font-bold text-2xl">Company Leaderboard</p>
    
                    </div>

                    {dataRetrieved ? (
                        <div className="grid grid-cols-3 space-x-5 pt-10 px-10 items-end">
                            {topThreeGlobal.map((item, index) => (
                                <Stage key={index} username={item.username} index={index} />
                            ))}
                        </div>

                    ) : (<p></p>)}


                    <div>
                        {dataRetrieved ? (
                            <div className="mt-10">
                                {topTenGlobal.map((item, index) => (
                                    <PositionTile key={index} name={item.username} place={index + 1} score={item.Score} />
                                ))}
                            </div>
                        ) : (
                            <p>Loading...</p>)}
                    </div>
                </div>




            </div>
        </div>
    )
}

export default LeaderBoardPage