import React,{useState,useEffect} from "react";

export default function UserList(){
    
    const [users,setUsers] = useState([]);
    const [dogImages,setDogImages] = useState([]);
    const [loading,setLoading] = useState(true);
    const [error,setError] = useState(null);

    const fetchData = async ()=>{
        const respose = await fetch('https://jsonplaceholder.typicode.com/users');
        const data = await respose.json();
        setUsers(data);
    }

    const fetchDogData=async ()=>{
        const response = await fetch('https://dog.ceo/api/breeds/image/random/3');
        const data = await response.json();
        setDogImages(data.message);
    }

    const refreshData=()=>{
        setLoading(true);
        setUsers([]);
        setDogImages([]);
        fetchData();
        fetchDogData().then(()=>setLoading(false));
    }

    useEffect(()=>{
        try{
    
            fetchData();
            fetchDogData();
            // setLoading(false);
        }catch(err){
            setError(err);
        }
        finally{
            setLoading(false);
        }
    },[])

    if(loading) return <h1>Loading...</h1>
    if(error) return <h1>Error</h1>
    return (
        <div>
            <div className="btn btn-primary" onClick={(e)=>{refreshData()}}>Refresh</div>
            <h1>Users</h1>
            <ul>
                {users.map((user,index) => <li key={index}>{user.name}-{user.email}</li>)}
            </ul>
            <h3>Dog Images</h3>
            <div>
                {dogImages.map((dogImage,index)=>{
                    return <img src={dogImage} alt="Dog"></img>
                })}
            </div>
        </div>
    )
}