import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './6_LoadingPage.css';

const LoadingPage2 = () => {
  const [loading, setLoading] = useState(true);
  const [progress, setProgress] = useState(0);
  const navigate = useNavigate();

  useEffect(() => {
    const checkStatus = async () => {
      try {
        const response = await axios.get('https://your-backend-endpoint.com/api/status');
        if (response.data.status === 'completed') {
          setLoading(false);
          navigate('/output');
        } else {
          // Increment the progress bar by 10% until it reaches 100%
          setProgress(prevProgress => (prevProgress >= 100 ? 100 : prevProgress + 10));
        }
      } catch (error) {
        console.error('Error fetching status:', error);
      }
    };

    const interval = setInterval(checkStatus, 1000);

    return () => clearInterval(interval);
  }, [navigate]);

  return (
    <div className="box-container">
      <div>
        {loading ? (
          <div>
            <h2>Now generating your Storyboard...</h2>
            <div className="progress-bar">
              <div className="progress" style={{ width: `${progress}%` }}></div>
            </div>
          </div>
        ) : (
          <h2>Process completed!</h2>
        )}
      </div>
      <Link to="/output" className="button-container">Submit 📮</Link>
    </div>
  );
};

export default LoadingPage2;