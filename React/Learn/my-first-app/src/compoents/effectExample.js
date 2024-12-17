import React,{useEffect,useState} from "react";

export default function EffectExample(){

    const [count,setCount] = useState(0);
    const [name, setName] = useState('')

    useEffect(()=>{
        console.log('Component Mounted');
        console.log(`Count updated to ${count}`);
        console.log(`Name updated to ${name}`);
    },[count,name])
    return (
        <div>
            <h1>Count: {count}</h1>
            <button className="btn btn-primary" onClick={()=>setCount(count+1)}>Increment</button>

            <h1>Name: {name}</h1>
            <input type='text' value={name} onChange={(e)=>setName(e.target.value)}></input>
        </div>
    )

}