import React, { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  let count: number = 0;
  const [counter, setCounter] = useState<number>(count);

  function handlePlusClick() {
    setCounter(counter + 1);
  }
  function handleMinusClick() {
    if (counter === count) {
      setCounter(count);
    } else {
      setCounter(counter - 1);
    }
  }

  useEffect(() => {
    document.title = `${counter}`;
  }, [counter]);

  const inputRef = useRef<HTMLInputElement>(null);

  return (
    <div className="App">
      <div className="counter">{counter}</div>
      <div className="buttons" ref={inputRef}>
        <button
          className="button-click"
          onClick={handlePlusClick}
          style={{ backgroundColor: "#81c784" }}
        >
          +
        </button>
        <button
          className="button-click"
          onClick={handleMinusClick}
          style={{ backgroundColor: "#e57373" }}
        >
          -
        </button>
      </div>
    </div>
  );
}

export default App;
