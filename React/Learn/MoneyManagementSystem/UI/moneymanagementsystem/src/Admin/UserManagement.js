import React, { useEffect, useState } from 'react'
import { GetAllUsers } from '../User/UserService'
import AddUser from '../User/AddUser';

export default function UserManagement() {
  let [users, setUsers] = useState([]);
  let [show, setShow] = useState('')
  let [editUserDetails,setEditUserDetails]=useState(null)
  const tableOuterStyle={
    margin:'1rem 5rem'
  }

  let onAddUserClose=()=>{
    setEditUserDetails(null)
    setShow('')
  }

  let sendUserToEdit=(user)=>{
    setEditUserDetails(user)
    setShow('edit')
  }

  useEffect(() => {
    GetAllUsers().then((user) => {
      console.log(user)
      setUsers(user)
    })
  }, [])
  return (
    <div>
      {show=='add' && <AddUser action={show} onClose={onAddUserClose} userDetails={editUserDetails}></AddUser>}
      {show=='edit' && <AddUser action={show} onClose={onAddUserClose} userDetails={editUserDetails}></AddUser>}
      <div>User Details:</div>
      <div style={tableOuterStyle}>
        <table className='table table-bordered'>
          <thead>
            <th>Name</th>
            <th>Email</th>
          </thead>
          <tbody>
            {users && users.map((user,index)=>(
              <tr>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>
                  <button className='btn btn-secondary' onClick={()=>sendUserToEdit(user)} >Edit</button>
                  <button className='btn btn-danger'>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <div>
          <div className='d-flex justify-content-center'>
            <button className='btn btn-primary' onClick={()=>setShow('add')}>Add User</button>
          </div>
        </div>
      </div>
    </div>
  )
}