import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './2_InputPage2.css';

const InputPage2  = () => {
    // State to manage the text input and placeholder visibility
    const [description, setDescription] = useState('');

    // Handler function to update description state
    const handleDescriptionChange = (event) => {
        setDescription(event.target.value);
    };

    return (
        <div className="inputContainer">
            <h1>Tell us more about your main character.</h1>
            <p>Any description on gender, appearance, style, or personality would be helpful!</p>

            <div className="box-container">

                <div className="box-description">
                    <label>Description:</label>
                    {/* Text area with conditional placeholder */} 
                    <textarea 
                        value={description} 
                        onChange={handleDescriptionChange} 
                        className="description-input"
                        placeholder="여기 입력해주세요."
                    />
                </div>
                
                <Link to="/style" className="button-container">Submit</Link>
            </div>
        </div>
    );
}

export default InputPage2 ;
