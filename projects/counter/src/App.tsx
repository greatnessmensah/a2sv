import React, { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  let count: number = 0;
  // the useState keeps or creates something like a variables in your
  // homepage that can be referenced and reassigned. It's a variable in a webpage
  const [counter, setCounter] = useState<number>(count);

  // this function increments the current counter by one, we declare the useState with two
  // parameters, one for referencing the variable aand another for setting the value
  function handlePlusClick() {
    setCounter(counter + 1);
  }

  // this function decrements the current counter by one
  function handleMinusClick() {
    if (counter === count) {
      setCounter(count);
    } else {
      setCounter(counter - 1);
    }
  }

  // the useEffect is used to manipulate the DOM of the webpage here,
  // it sets the title of the document to the value of the counter
  useEffect(() => {
    document.title = `${counter}`;
  }, [counter]);

  // the useRef is used for referencing values that will not be rendered on the page
  // over here the useRef is used to access the button element
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
