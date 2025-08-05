// import "./App.css";
import React, { useState } from "react";

// Header
// Usercard
// UserForm

function Header() {
  return (
    <nav className="navbar navbar-light bg-light px-4">
      <a className="navbar-brand" href="#">
        User Manager
      </a>
    </nav>
  );
}

function AddUserForm({ onAddUser, editIndex }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddUser({ username, password });
    setUsername("");
    setPassword("");
  };

  return (
    <div className="card p-3">
      <h5>{editIndex == null ? "Add User" : "Edit User"}</h5>
      <form onSubmit={handleSubmit}>
        <input
          className="form-control mb-2"
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className="form-control mb-2"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="btn btn-primary w-100">Add</button>
      </form>
    </div>
  );
}

function UserCardList({ users, onDelete, onEdit }) {
  return (
    <div>
      {users.map((user, index) => (
        <div className="card mb-2 p-2" key={index}>
          <h6>{user.username}</h6>
          <p className="text-muted"> Password: {user.password}</p>
          <button className="btn btn-danger" onClick={() => onDelete(index)}>
            Delete
          </button>
          <button
            className="btn btn-sm btn-secondary my-2"
            onClick={() => onEdit(index)}
          >
            Edit
          </button>
        </div>
      ))}
    </div>
  );
}

const EditUserForm = ({ onAddUser, editIndex }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddUser({ username, password });
    setUsername("");
    setPassword("");
  };

  return (
    <div className="card p-3">
      <h5>Edit user</h5>
      <form onSubmit={handleSubmit}>
        <input
          className="form-control mb-2"
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className="form-control mb-2"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="btn btn-primary w-100">Edit</button>
      </form>
    </div>
  );
};

function App() {
  const [users, setUsers] = useState([]);
  const [editIndex, setEditIndex] = useState(null);
  // const [mode, setMode] = useState(0);

  const handleAddUser = (user) => {
    setUsers([user, ...users]);
  };

  const handleDeleteUser = (indexToDelete) => {
    const updated = users.filter((_, index) => index !== indexToDelete);
    setUsers(updated);
  };

  const handleEditUser = (indexToEdit) => {
    setEditIndex(indexToEdit);
  };

  // function onUpdate(id) {
  //   const userToUpdate = users[editIndex];
  //   setUpdatableUser(userToUpdate);
  //   setUsers((prev) => prev.filter((user) => user.id !== id));
  // }

  return (
    <>
      <Header />
      <div className="container mt-4">
        <div className="row">
          <div className="col-md-6">
            <UserCardList
              users={users}
              onDelete={handleDeleteUser}
              onEdit={handleEditUser}
            />
          </div>
          <div className="col-md-6">
            {
              editIndex == null ? <AddUserForm onAddUser={handleAddUser} editIndex={editIndex} /> :
              <EditUserForm  onAddUser={handleAddUser} editIndex={editIndex} />
            }
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
