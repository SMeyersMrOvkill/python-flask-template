import logo from './logo.svg';
import './App.css';

function App() {
  // Lazy load components here if necessary
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>backend/app.py</code> and save to reload and add endpoints.
        </p>
        <p>
          Edit <code>src/App.js</code> and re-run to see your changes.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Learn React"
        >
          Learn React
        </a>

        <a 
          className="App-link"
          href="https://flask.palletsprojects.com/en/stable/#"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Learn Flask"
        >
          Learn Flask
        </a>
      </header>
    </div>
  );
}

export default App;
