import React from 'react'; // Import the React library
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import the BrowserRouter, Route, and Routes components
import HomePage from './components/0_HomePage'; // Import the HomePage component
import InputPage from './components/1_InputPage'; // Import the InputPage component
import StylePage from './components/2_ImageButtons';
import LoadingPage from './components/3_LoadingPage';
import OutputPage from './components/4_OutputPage';

const App = () => { // Create a functional component named App
    return (
        <Router> 
            <div>
                <Routes>
                    <Route exact path="/" element={<HomePage />} /> 
                    <Route path="/input" element={<InputPage />} />
                    <Route path="/style" element={<StylePage />} />
                    <Route path="/loading" element={<LoadingPage />} />
                    <Route path="/output" element={<OutputPage />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
