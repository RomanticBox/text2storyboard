import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // useNavigate hook
import './2_ImageButtons.css';
import image1 from './images/image1.png';
import image2 from './images/image2.png';
import image3 from './images/image3.png';
import image4 from './images/image4.png';
import image5 from './images/image5.png';

const ImageButtons = () => {
  const navigate = useNavigate(); // useNavigate hook

  const handleClick = (imageNumber) => {
    // Navigate to the appropriate page
    navigate('/loading');
    // You can also perform additional actions here, like storing the selected image number in localStorage
    localStorage.setItem('selectedImage', imageNumber);
  };

  return (
    <div>
      <h2>원하는 그림체의 이미지를 선택하세요 ✏️</h2>
      <div className="button-container1">
        <button className="image-button" onClick={() => handleClick(1)}>
          <img src={image1} alt="Button 1" />
          <div className="button-info">
            <p>storymakerver1</p>
          </div>
        </button>
        <button className="image-button" onClick={() => handleClick(2)}>
          <img src={image2} alt="Button 2" />
          <div className="button-info">
            <p>이미지 2</p>
          </div>
        </button>
        <button className="image-button" onClick={() => handleClick(3)}>
          <img src={image3} alt="Button 3" />
          <div className="button-info">
            <p>이미지 3</p>
          </div>
        </button>
        <button className="image-button" onClick={() => handleClick(4)}>
          <img src={image4} alt="Button 4" />
          <div className="button-info">
            <p>fantasy</p>
          </div>
        </button>
        <button className="image-button" onClick={() => handleClick(5)}>
          <img src={image5} alt="Button 5" />
          <div className="button-info">
            <p>casual</p>
          </div>
        </button>
      </div>
    </div>
  );
};

export default ImageButtons;
