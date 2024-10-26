import React, { useEffect, useState } from 'react'

export default function AddUser({action,onClose,userDetails}) {
  useEffect(() => {
    if(action=='edit'){
      console.log(userDetails)
    }
  }, [])
  return (
    <div>
      <div className='modal d-block'>
        <div className='modal-dialog'>
          <div className='modal-content'>
            <div className='modal-header'>
              <h5 className='modal-title'>Add User</h5>
              <button className='btn-close' onClick={()=>onClose()}></button>
            </div>
            <div className='modal-body'>
              <form>
                <div className='form-group'>
                  <label>Name:</label>
                  <input type='text' className='form-control'></input>
                </div>
                <div className='form-group'>
                  <label>Email:</label>
                  <input type='text' className='form-control'></input>
                </div>
                <div className='form-group'>
                  <label>Password:</label>
                  <input type='password' className='form-control'></input>
                </div>
                {/* <div className='form-group'>
                  <label>Role:</label>
                  <select className='form-control'>
                    <option>Admin</option>
                    <option>User</option>
                  </select>
                </div> */}
              </form>
            </div>
            <div className='modal-footer'>
              <button className='btn btn-primary'>{action=='add'?'Add':'Edit'}</button>
              <button className='btn btn-secondary' onClick={()=>onClose()}>Cancel</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
