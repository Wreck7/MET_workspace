import React, { useState } from "react";

const EmojiToggle = () => {
  const [isHappy, setIsHappy] = useState(true);
  
  return (
    <div>

      <h2>Emotion toggle</h2>
      <h3>{isHappy ? "😀" : "☹️"}</h3>
      <button onClick={() => setIsHappy(!isHappy)}>
        {isHappy ? "Happy" : "Sad"}
      </button>

    </div>
  );
};

export default EmojiToggle;
