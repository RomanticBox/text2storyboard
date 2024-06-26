import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './InputPage.css';

const HomePage = () => {
    // State to manage the text input and placeholder visibility
    const [description, setDescription] = useState('');

    // Handler function to update description state
    const handleDescriptionChange = (event) => {
        setDescription(event.target.value);
    };

    return (
        <div className="inputContainer">
            <h1>콘티로 생성하고 싶은 상황을 설명해주세요 ✏️</h1>
            <p>"더 자세하게 설명할수록 원하는 콘티를 얻을 수 있어요!"</p>

            <div className="box-container">
            
                <div className="box-example">
                    <label>Example:</label>
                    <div>On the weekend, five lovely girls went to a playground park. They arrived with a guide who is knowledgeable about the park. Before entering the park, she gave the playing role instructions. They had a wonderful time and participated in a variety of activities. They played golf, which was incredibly interesting to them. Finally, they immensely enjoyed it.</div>
                </div>

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
                
                <Link to="/input" className="button-container">Submit 📮</Link>
            </div>
        </div>
    );
}

export default HomePage;
