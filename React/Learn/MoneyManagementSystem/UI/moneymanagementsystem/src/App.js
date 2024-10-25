import logo from './logo.svg';
import './App.css';
import AddUser from './User/AddUser';
import {BrowserRouter as Router, Routes,Route} from 'react-router-dom'
import UserManagement from './Admin/UserManagement';

function App() {
  return (
    <div className="">
      <div className=''>
        <div className='mms_title'>Money Management System</div>
        <AddUser></AddUser>
        <Routes>
          <Route path='/useradmin' element={<UserManagement></UserManagement>} ></Route>
        </Routes>
      </div>
    </div>
  );
}

export default App;
