import axios from 'axios'

export async function GetAllUsers(){
    try{
        const response=await axios.get('http://127.0.0.1:5000/user/users');
        return response.data
    }
    catch(error){
        console.log(error.message)
        return null
    }
}