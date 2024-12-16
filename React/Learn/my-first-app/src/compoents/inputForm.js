import React, {useState} from 'react';

function InputForm(){

    const [name,setName]=useState('');
    const [age,setAge]=useState(0);
    const [password,setPassword]=useState('');

    const setUpdatedName=(e)=>{
        setName(e.target.value);
    }

    const setUpdatedAge=(e)=>{
        setAge(e.target.value);
    }

    const showDetailsAlert=()=>{
        alert(`Name: ${name} Password: ${password}`);
    }

    return (
        <div>
           <form onSubmit={showDetailsAlert}>
           <input type="text" className='mb-2' value={name} onChange={setUpdatedName} placeholder='Enter your name' /><br></br>
            <input type='number' className='mb-2' value={age} onChange={setUpdatedAge} placeholder='Enter your age' /><br></br>
            <input type='password' value={password} onChange={(e)=>setPassword(e.target.value)} placeholder='Enter your password' />
            <div>
                <div className="h3">You Name is {name}</div>
                <div className="h3">You Age is {age}</div>
            </div>
            <div>
                <input type='submit' value='Submit' className='btn btn-primary'></input>
            </div>
           </form>
        </div>
    );
}

export default  InputForm;