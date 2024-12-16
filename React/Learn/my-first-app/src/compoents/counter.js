import React,{useState} from 'react';

function Counter(){
    const [count,setCount]=useState(0);
    const [numType,setNumType]=useState('Even');

    let increment=()=>{
        setCount(count+1);
        if(count%2===0){
            setNumType('Even');
        }else{
            setNumType('Odd');
        }
    }

    let decrement=()=>{
        setCount(count-1);
        if(count%2!==0){
            setNumType('Odd');
        }else{
            setNumType('Even');
        }
    }

    let reset=()=>{
        setCount(0);
        setNumType('Even');
    }

    let showAlertMessage=(d)=>{
        console.log(d)
        alert('You have clicked the alert button');
    }

    return(
        <div>
            <div className='h1'>Counter:{count}</div>
            <div className='h3'>Number is {numType}</div>
            <div className='btn btn-primary me-2' onClick={increment}>Increment</div>
            <div className='btn btn-primary me-2' onClick={decrement}>Decrement</div>
            <div className='btn btn-primary me-2' onClick={reset}>Reset</div><br></br>

            <div className='btn btn-danger me-2 mt-2 mb-2' onClick={showAlertMessage}>Alerting</div>
        </div>
    )
}

export default Counter;