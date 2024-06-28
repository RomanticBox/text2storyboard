import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // useNavigate hook
import './SixImage.css';
import character_sample_1 from './images/character_sample_1.png';
import character_sample_2 from './images/character_sample_2.png';
import character_sample_3 from './images/character_sample_3.png';
import character_sample_4 from './images/character_sample_4.png';
import character_sample_5 from './images/character_sample_5.png';
import character_sample_6 from './images/character_sample_6.png';

const SixImage = () => {
  const navigate = useNavigate(); // useNavigate hook

  const handleClick = (imageNumber) => {
    // Navigate to the appropriate page
    navigate(`/page`);
    // You can also perform additional actions here, like storing the selected image number in localStorage
    localStorage.setItem('selectedCharacter', imageNumber);
  };

  return (
    <div>
      <h3>가장 마음에 드는 이미지를 선택하세요 ✏️</h3>
      <div className="button-container-sixImage">
        <button className="image-button-sixImage" onClick={() => handleClick(1)}>
          <img src={character_sample_1} alt="Button 1" />
          <div className="button-info-sixImage">
          </div>
        </button>
        <button className="image-button-sixImage" onClick={() => handleClick(2)}>
          <img src={character_sample_2} alt="Button 2" />
          <div className="button-info-sixImage">
          </div>
        </button>
        <button className="image-button-sixImage" onClick={() => handleClick(3)}>
          <img src={character_sample_3} alt="Button 3" />
          <div className="button-info-sixImage">
          </div>
        </button>
        <button className="image-button-sixImage" onClick={() => handleClick(4)}>
          <img src={character_sample_4} alt="Button 4" />
          <div className="button-info-sixImage">
          </div>
        </button>
        <button className="image-button-sixImage" onClick={() => handleClick(5)}>
          <img src={character_sample_5} alt="Button 5" />
          <div className="button-info-sixImage">
          </div>
        </button>
        <button className="image-button-sixImage" onClick={() => handleClick(6)}>
          <img src={character_sample_6} alt="Button 6" />
          <div className="button-info-sixImage">
          </div>
        </button>
      </div>
    </div>
  );
};

export default SixImage;
