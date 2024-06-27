import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './InputPage2.css';

const HomePage = () => {
    // State to manage the text input and placeholder visibility
    const [description, setDescription] = useState('');

    // Handler function to update description state
    const handleDescriptionChange = (event) => {
        setDescription(event.target.value);
    };

    return (
        <div className="inputContainer2">
            <h1>Main Character Description ✏️</h1>

            <div className="box-container-input2">
            
                <div className="main-character">
                    <label>Main Character Name:</label>
                    <textarea 
                        value={description} 
                        onChange={handleDescriptionChange} 
                        className="main-character-input2"
                        placeholder="여기 입력해주세요."
                    />
                </div>

                <div className="main-character-description">
                    <label>Main Character Description:</label>
                    {/* Text area with conditional placeholder */} 
                    <textarea 
                        value={description} 
                        onChange={handleDescriptionChange} 
                        className="main-character-description-input2"
                        placeholder="여기 입력해주세요."
                    />
                </div>
                
                <Link to="/image-buttons" className="button-container-input2">Submit 📮</Link>
            </div>
        </div>
    );
}

export default HomePage;
