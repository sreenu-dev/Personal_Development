import logo from './logo.svg';
import './App.css';
import Header from './compoents/header';
import Footer from './compoents/footer';
import { useState } from 'react';
import Content from './compoents/content';

function App() {
  const name = 'Josh Perez';
  const age= 20;

  return(
    <div className='container mt-3'>
      <Header></Header>
      <Content name={name} age={age}></Content>
      <Footer></Footer>
    </div>
  )
}

export default App;
