import React, { useState } from "react";

const EvenOrOdd = () => {
  const [num, setNum] = useState("");
  const parsedNum = parseInt(num);
  return (
    <div>
      <h2>Even or Odd checker</h2>
      <input
        type="text"
        value={num}
        placeholder="enter a number here!"
        onChange={(e) => setNum(e.target.value)}
      />
      <p>{num === "" ? "" : parsedNum % 2 === 0 ? "Even" : "Odd"}</p>
    </div>
  );
};

export default EvenOrOdd;
