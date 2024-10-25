import React, { useEffect, useState } from 'react'
import { GetAllUsers } from '../User/UserService'

export default function UserManagement() {
  let [users, setUsers] = useState([]);
  useEffect(() => {
    GetAllUsers().then((user) => {
      console.log(user)
      setUsers(user)
    })
  }, [])
  return (
    <div>
      <div>User Details:</div>
      {users.length}
      {users.map((user, index) => (
        <div>{user.name}</div>
      ))}
      <div className='margin-right:1rem'>
        <table className='table table-bordered'>
          <thead>
            <th>Name</th>
            <th>Email</th>
          </thead>
          <tbody>
            {users.map((user,index)=>(
              <tr>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>
                  <button className='btn btn-secondary' >Edit</button>
                  <button className='btn btn-danger'>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button className='btn btn-primary' onClick={() => { console.log(users) }} >Show users</button>
    </div>
  )
}