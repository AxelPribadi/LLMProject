import React, { useState, useEffect } from 'react';
import PromptTextBox from './PromptTextBox';
import ToggleButton from './ToggleButton';
import './App.css'

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleToggle = () => {
    setIsDarkMode(!isDarkMode);
  };

  useEffect(() => {
    document.body.classList.toggle("dark-mode", isDarkMode);
    document.body.classList.toggle("light-mode", !isDarkMode);
  }, [isDarkMode]);

  return (
    <>
      <div className={`mainApp ${isDarkMode ? "dark-mode" : "light-mode"}`}>
        <ToggleButton onToggle={handleToggle} isDarkMode={isDarkMode} />
        <h1> AI Content Detector </h1>
      
        {PromptTextBox()}
      </div>
    </>
  );
}

export default App;
