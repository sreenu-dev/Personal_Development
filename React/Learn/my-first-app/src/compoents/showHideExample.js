import React, {useState} from 'react';

export default function ShowHideExample(){
    const [isShow, setIsShow] = useState(false);
    return(
        <div>
            <button className="btn btn-primary mt-2" onClick={()=>{setIsShow(!isShow)}}>Show/Hide</button>
            {isShow && <div>Show Hide Example</div>}
            {!isShow && <div>Click the button to show the text</div>}
        </div>
    )

}