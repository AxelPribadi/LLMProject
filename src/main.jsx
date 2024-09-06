import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'

// import ResponseField  from './ResponseField.jsx'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <hr className="divider" />
    <footer>
      <p> Powered by XtraLargeProcessors' Fine-Tuned LLM Model </p>
    </footer>
  </StrictMode>,
)
