import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    // Accessing the environment variable for the API URL
    const apiUrl = import.meta.env.VITE_API_URL;

    // Making a fetch request to the Django backend
    fetch(`${apiUrl}/mymodel/`)
        .then(response => response.json())
        .then(data => setData(data))
        .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
      <div className="App">
          <h1>Data from Django API</h1>
          <ul>
              {data.map(item => (
                  <li key={item.id}>{item.name}</li>
              ))}
          </ul>
      </div>
  );
}


export default App
