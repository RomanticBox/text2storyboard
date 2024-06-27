import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './1_InputPage.css';

const HomePage = () => {
    // State to manage the text input and placeholder visibility
    const [description, setDescription] = useState('');

    // Handler function to update description state
    const handleDescriptionChange = (event) => {
        setDescription(event.target.value);
    };

    return (
        <div className="inputContainer">
            <h1>Tell us about your own story ✏️</h1>
            <p>You can get better result if you let us know more specific...</p>

            <div className="box-container">
            
                <div className="box-example">
                    <label>Example:</label>
                    <div>On the weekend, five lovely girls went to a playground park. They arrived with a guide who is knowledgeable about the park. Before entering the park, she gave the playing role instructions. They had a wonderful time and participated in a variety of activities. They played golf, which was incredibly interesting to them. Finally, they immensely enjoyed it.</div>
                </div>

                <div className="box-description">
                    <label>Your Story:</label>
                    {/* Text area with conditional placeholder */} 
                    <textarea 
                        value={description} 
                        onChange={handleDescriptionChange} 
                        className="description-input"
                        placeholder="여기 입력해주세요."
                    />
                </div>
                
                <Link to="/input2" className="button-container">Submit 📮</Link>
            </div>
        </div>
    );
}

export default HomePage;
