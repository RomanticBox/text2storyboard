import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // useNavigate hook
import './5_CharacterSelect.css';
import image1 from './images/image1.png'; // SDXL로 생성된 이미지 경로
import image2 from './images/image2.png';
import image3 from './images/image3.png';
import image4 from './images/image4.png';
import image5 from './images/image5.png';

const CharacterSelect = () => {
  const navigate = useNavigate(); // useNavigate hook

  const handleClick = (imageNumber) => {
    // Navigate to the appropriate page
    navigate('/loading2');
    // You can also perform additional actions here, like storing the selected image number in localStorage
    localStorage.setItem('selectedCharacter', imageNumber);
  };

  return (
    <div>
      <h2>Which character do you prefer?</h2>
      <div className="button-container1">
        <button className="image-button" onClick={() => handleClick(1)}>
          <img src={image1} alt="Button 1" />
        </button>
        <button className="image-button" onClick={() => handleClick(2)}>
          <img src={image2} alt="Button 2" />
        </button>
        <button className="image-button" onClick={() => handleClick(3)}>
          <img src={image3} alt="Button 3" />
        </button>
        <button className="image-button" onClick={() => handleClick(4)}>
          <img src={image4} alt="Button 4" />
        </button>
        <button className="image-button" onClick={() => handleClick(5)}>
          <img src={image5} alt="Button 5" />
        </button>
      </div>
    </div>
  );
};

export default CharacterSelect;
