
import React, { useState } from 'react';

export default function TodoApp() {

    const [toDoList, setToDoList] = useState([
        {task:'Todo 1',isChecked:false},
        {task:'Todo 2',isChecked:false},
        {task:'Todo 3',isChecked:false},
    ]);
    const [toDoItem, setToDoItem] = useState('');
    const [toDoRemoveItems, setToDoRemoveItems] = useState([]);
    let refresh = false

    const addToDoItem = () => {
        let toDoItemObject = {task:toDoItem,isChecked:false};
        setToDoList([...toDoList, toDoItemObject]);
        setToDoItem('');
    }

    const deleteToDoItems = (e, index) => {
        let updatedToList=toDoList.map((todo, i) => {
            if(i===index){
                todo.isChecked=e.target.checked;
            }
            return todo;
        })

        setToDoList(updatedToList);
    }

    const removeToDoItems = () => {
        let toDoListCopy = [...toDoList];
        toDoListCopy = toDoListCopy.filter((todo) => !todo.isChecked);
        setToDoList([...toDoListCopy]);
    }

    return (
        <div>
            <header>
                <div classNmame='h1'>My First React App</div>
            </header>
            <div>
                <input type='text' value={toDoItem} onChange={(e) => { setToDoItem(e.target.value) }}></input>
                <button className="btn btn-primary" onClick={addToDoItem}>Add Todo</button>
            </div>
            <div>
                {
                    !refresh && <ul>
                        {toDoList.map((todo, index) => <li key={index}><input type='checkbox' checked={todo.checked} onChange={(e) => deleteToDoItems(e, index)} className='me-2'/><span id={index}>{todo.task}-{index}</span></li>)}
                    </ul>
                }
                <button className="btn btn-danger" onClick={removeToDoItems}>Delete Todo</button>
            </div>
        </div>
    )
}