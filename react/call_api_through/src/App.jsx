import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState([])
  useEffect(() => {
    async function fetchingData() {
      const response = await fetch('https://api.datamuse.com/words?ml=ringing+in+the+ears')
      const res = await response.json()
      setData(res)
    }
    fetchingData()
  }, [])
  

  return (
    <>
      {data.map((user, index) => (
        <div key={index}>{user.word}</div>
      )
      )}
    </>
  )
}

export default App
