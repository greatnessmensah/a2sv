import React, { useState } from "react";
import "./App.css";

function App() {
  let count: number = 0;
  const [counter, setCounter] = useState<number>(count);

  function handlePlusClick() {
    setCounter(counter + 1);
  }
  function handleMinusClick() {
    if (counter === count) {
      setCounter(count)
    } else {
    setCounter(counter - 1)
    }
  }

  return (
    <div className="App">
      <div className="counter">{counter}</div>
      <div className="buttons">
      <button className="button-click" onClick={handlePlusClick}>+</button>
      <button className="button-click" onClick={handleMinusClick}>-</button>
      </div>
    </div>
  );
}

export default App;
