import { useState } from "react";
import tokioLogo from "./assets/tmhcc-logo-white.png";
import "./App.css";

function App() {
  const [id, setId] = useState(1);

  const handleChange = e => {
    setId(e.target.value);
  }

  const handleClick = async () => {
    if (!id) {
      return;
    }
    const response = await fetch(`http://127.0.0.1:8000/policies/${id}`);
    const data = await response.json();

    console.log(data);
  }

  return (
    <main>
      <nav>
        <a href="https://www.tmhcc.com/en/" target="_blank">
          <img src={tokioLogo} alt="Tokio logo" />
        </a>
      </nav>
      <h1>Policies</h1>
      <div>
        <input type="number" value={id} placeholder="Enter a policy id" onChange={handleChange} />
        <button onClick={handleClick}>Load Policy</button>
      </div>
    </main>
  )
}

export default App;
