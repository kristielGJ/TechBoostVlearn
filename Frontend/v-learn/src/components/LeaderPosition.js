const PositionTile =(props)=>{
    return(
        <div className="grid grid-cols-3 my-4 mx-3 bg-slate-200 drop-shadow-lg rounded-lg min-h-8">
            <div className="text-center text-lg font-bold" >{props.place}</div>
            <div className="">{props.name}</div>
            <div className="text-center">{props.score}</div>
        </div>
    )
}
export default PositionTile