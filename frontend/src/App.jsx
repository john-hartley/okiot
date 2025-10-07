import { useState } from "react";
import tokioLogo from "./assets/tmhcc-logo-white.png";
import "./App.css";

function App() {
  const [id, setId] = useState(0);

  const handleClick = async () => {
    const response = await fetch(`http://127.0.0.1:8000/policies/${id + 1}`);
    const data = await response.json();

    setId(data.policy.id);
  }

  return (
    <main>
      <nav>
        <a href="https://www.tmhcc.com/en/" target="_blank">
          <img src={tokioLogo} className="logo" alt="Tokio logo" />
        </a>
      </nav>
      <h1>Policies</h1>
      <div className="">
        <div>{id}</div>
        <button onClick={handleClick}>Load Policy</button>
      </div>
    </main>
  )
}

export default App;
