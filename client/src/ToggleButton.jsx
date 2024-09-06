import React from 'react';

function ToggleButton({ onToggle, isDarkMode }) {
  return (
    <button className={`toggleButton ${isDarkMode ? "dark" : "light"}`} onClick={onToggle}>
      {isDarkMode ? "🌙 Dark Mode" : "🌞 Light Mode"}
    </button>
  );
}

export default ToggleButton;
