import React, { useState, useEffect } from "react";
import "../App.css";

const UserForm = ({ getInfo, updatableUser }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleClick = (e) => {
    e.preventDefault();
    getInfo({username, password});
    setUsername("");
    setPassword("");
  };
  useEffect(() => {
  if (updatableUser) {
    setUsername(updatableUser.username || "");
    setPassword(updatableUser.password || "");
  }
}, [updatableUser]);

  
  return (
    <div>
      <div className="userForm">
        <h2>Add User</h2>
        <input
          type="text"
          className="inputBox"
          placeholder="Enter username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="text"
          className="inputBox"
          placeholder="Enter Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="btn" onClick={handleClick}>
          Add
        </button>
      </div>
    </div>
  );
};

export default UserForm;
