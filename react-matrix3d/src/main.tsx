import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './react-matrix3d'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
