import React from 'react'; // Import the React library
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import the BrowserRouter, Route, and Routes components
import HomePage from './components/0_HomePage'; // Import the HomePage component
import InputPage from './components/1_InputPage'; // Import the InputPage component
import InputPage2 from './components/2_InputPage2'; // Import the InputPage component
import StylePage from './components/3_ImageButtons';
import LoadingPage1 from './components/4_LoadingPage';
import LoadingPage2 from './components/6_LoadingPage';
import OutputPage from './components/7_OutputPage';
import  CharacterSelect from './components/5_CharacterSelect';

const App = () => { // Create a functional component named App
    return (
        <Router> 
            <div>
                <Routes>
                    <Route exact path="/" element={<HomePage />} /> 
                    <Route path="/input" element={<InputPage />} />
                    <Route path="/input2" element={<InputPage2 />} />
                    <Route path="/style" element={<StylePage />} />
                    <Route path="/character" element={<CharacterSelect />} />
                    <Route path="/loading1" element={<LoadingPage1 />} />
                    <Route path="/loading2" element={<LoadingPage2 />} />
                    <Route path="/output" element={<OutputPage />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
