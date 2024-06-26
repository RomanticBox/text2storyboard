import React from 'react';
import './App.css';
import Hello from './components/Hello';

function App() {

  const name = 'react';
  const stylep = {
    backgroundColor: 'black',
    color: 'aqua',
    padding: '1rem'
  }


  return (
    <>
      <Hello />
      <div style={style}>{name}</div>
    </>
  );
}

export default App;
