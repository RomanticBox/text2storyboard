import React from 'react';
import { GoMarkGithub } from './images/github.png';

const GitHubButton = () => {
  return (
    <a href="https://github.com/your-username/your-repository" target="_blank" rel="noopener noreferrer">
      <button>
        <GoMarkGithub style={{ marginRight: '8px' }} />
        Go to GitHub Repository
      </button>
    </a>
  );
}

export default GitHubButton;