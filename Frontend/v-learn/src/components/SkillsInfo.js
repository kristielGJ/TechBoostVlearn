import Slider from '@mui/material/Slider';


const SkillsInfo = () => {
    const redDisabledSliderStyle = {
        color: 'red', // Change the color to red
        '& .MuiSlider-thumb': {
          // Change the color of the thumb (handle)
          color: 'red',
        },
      };
    
    
    return (
    
        <div className="bg-white bg-opacity-70 rounded-lg min-h-80  drop-shadow-2xl shadow-red-100 flex flex-col align-center  ">
            <h1 className="text-red-600 text-2xl font-semibold place-self-start ml-10 mt-5"> Skills</h1>
            <ul className="ml-10 mt-5 space-y-5 mb-10">
                <li>
                    <p>Business Alalysis</p>
                    <Slider
                        
                        disabled
                        defaultValue={2}
                        step={1}
                        marks
                        min={1}
                        max={5}
                        sx={{
                            width:'80%'
                        }}
                        style={redDisabledSliderStyle}
                    />
                </li>
                <li>
                    <p>Cloud Computing</p>
                    
                    <Slider
                        
                        disabled
                        defaultValue={2}
                        step={1}
                        marks
                        min={1}
                        max={5}
                        sx={{
                            width:'80%'
                        }}
                        style={redDisabledSliderStyle}
                    />
                </li>
                 <li>
                    <p>Marketing</p>
                    
                    <Slider
                        
                        disabled
                        defaultValue={3}
                        step={1}
                        marks
                        min={1}
                        max={5}
                        sx={{
                            width:'80%'
                        }}
                        style={redDisabledSliderStyle}
                    />
                </li>
                <li>
                    <p>Software Engineer</p>
                    
                    <Slider
                        
                        disabled
                        defaultValue={5}
                        step={1}
                        marks
                        min={1}
                        max={5}
                        sx={{
                            width:'80%'
                        }}
                        style={redDisabledSliderStyle}
                    />
                </li>

            </ul>
        </div>

    )
}

export default SkillsInfo