import React from "react";

const UserCards = ({ users, onDelete, onUpdate }) => {
  return (
    <div>
      {users.map((user) => (
        <div className="userCard" key={user.id}>
          <p>Username: {user.username}</p>
          <p>Password: {user.password}</p>
          <div className="btns">
            <button onClick={() => onDelete(user.id)} className="btn delete">
              Delete
            </button>
            <button onClick={() => onUpdate(user.id)} className="btn delete">
              Update
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default UserCards;
