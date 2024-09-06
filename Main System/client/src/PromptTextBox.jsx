
import React, { useEffect, useState, useRef } from 'react';
import SubmitButton from './SubmitButton';
import ResponseField from './ResponseField';

import axios from 'axios'

// Replace with API
function getRandomResponse() {
  const resp = Math.round(Math.random());
  return resp === 0 ? "Human Generated Text" : "AI Generated Text";
}



function PromptTextBox() {
  const [text, setText] = useState("");
  const [isButtonEnabled, setIsButtonEnabled] = useState(false);
  const [response, setResponse] = useState(null);

  // Check for Text in Text Area
  const handleChange = (e) => {
    const newText = e.target.value;
    setText(newText);
    setIsButtonEnabled(newText.trim().length > 0);
  };

  // Adjust Text Area Height
  const textareaRef = useRef(null);
  useEffect(() => {
    if (textareaRef.current){
      textareaRef.current.style.padding = "0";
      textareaRef.current.style.height = "25px";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
      textareaRef.current.style.padding = '10px';
    }
  }, [text]);

  const handleSubmit = () => {
    if (isButtonEnabled) {
      console.log("Submitted Prompt: ", text); // Send to LLM Model

      // const generatedResponse = getRandomResponse();
      // setRepsonse(generatedResponse);

      // Send to Python BackEnd
      axios.post("http://127.0.0.1:5000/api/predict", {prompt:text}) // Later Add UserId etc
        .then(res => {
          setResponse(res.data.response);
        })
        .catch(err => {
          console.error("Error", err)
        });

    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey && isButtonEnabled){
      e.preventDefault();
      handleSubmit();
    };
  };
  
  return (
    <>
      <div className="promptContainer">
        <textarea className="promptTextArea"
          ref={textareaRef}
          value={text} 
          onChange={handleChange} 
          onKeyDown={handleKeyDown}
          placeholder="Enter your text here..."
          rows="10" 
          cols="50"
        />
        
        <SubmitButton onSubmit={handleSubmit} isEnabled={isButtonEnabled} />
      </div>
      
      <div className="responseContainer">
        {response && <ResponseField response={response} />}
      </div>
    </>
  );
}

export default PromptTextBox;