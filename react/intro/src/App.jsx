import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className='container'>
      <p id='countDisplay'>{count}</p>
      <button className='btn red' onClick={() => count > 0 && setCount(prev => prev-1)}>decrement(-)</button>
      <button className='btn green' onClick={() => setCount(prev => prev+1)}>increment(+)</button>
    </div>
  )
}

export default App
