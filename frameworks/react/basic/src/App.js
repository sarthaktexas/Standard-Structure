// React likes being on the cutting-edge, so ES6 modules are being used.
import React from 'react';
import logo from './logo.svg';

// CSS imports work as well! You can add them to the global scope like this:
import './App.css';

function App() {
  // Normally, all React components return JSX. However, you can also go with the less condensed method using React.createElement()
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
    </div>
  );
}

export default App;
