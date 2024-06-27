import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';
// import image from './image.png';
import image from './image_circle.gif';

const HomePage = () => {
    return (
        <div className="container">
            <div className="content">
                <h1>Story Weaver 🎨</h1>
                <div className="content1">
                    <p>"웹툰 작가를 위한 콘티 생성기"</p>
                </div>
                <Link to="/input" className="link-button">Get Started 😎</Link>
            </div>
            <div className="image-wrapper">
                <img src={image} alt="Story Weaver Image" className="side-image" />
            </div>
        </div>
    );
};

export default HomePage;

