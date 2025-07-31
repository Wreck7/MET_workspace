import React, { useState } from "react";

const Reverser = () => {
  const [text, setText] = useState("");
  const reversedWord = text.split("").reverse().join("");
  return (
    <div>
      <>
        <h2>Text Reverser</h2>
        <input
          placeholder="Type here!"
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <p>Reversed: {reversedWord}</p>
        <p>Original: {text}</p>
      </>
    </div>
  );
};

export default Reverser;
