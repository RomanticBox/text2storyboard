import React from 'react';
import { Link } from 'react-router-dom';
import './0_HomePage.css';
import image from './images/logo.gif';

const HomePage = () => {
    return (
        <div className="container">
            <div className="content">
                <h1>StoryWeaver</h1>
                <div className="content1">A Storyboard Generator for Webtoon Artist</div>
                <div className="creators">Created by 1nhye, RomanticBox, shifrepot, chaehyun1, yerilolilye, standor0415, gdvstd</div>
                <Link to="/input" className="link-button">Get Started</Link>
            </div>
            <div className="image-wrapper">
                <img src={image} alt="Story Weaver Image" className="side-image" />
            </div>
        </div>
    );
};

export default HomePage;

