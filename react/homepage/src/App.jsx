import { useState } from "react";
import "./App.css";
import Header from "./compo/Header";
import UserForm from "./compo/UserForm";
import UserCards from "./compo/UserCards";

function App() {
  const [users, setUsers] = useState([
    { username: "tejas", password: "tejas@1234", id: 1 },
  ]);
  const [updatableUser, setUpdatableUser] = useState()
  function getInfo(user) {
    const newUser = { ...user, id: Date.now() };
    setUsers([newUser, ...users]);
    setUpdatableUser(null)
  }

  function onDelete(id) {
    setUsers(prev => prev.filter(user => user.id !== id))
    
  }
  
  function onUpdate(id) {
    const userToUpdate = users.find(user => user.id === id);
    setUpdatableUser(userToUpdate);
    setUsers(prev => prev.filter(user => user.id !== id));
  }

  return (
    <>
      <Header />
      <div className="container">
        <div className="main">
          <div>
            <UserForm getInfo={getInfo} updatableUser={updatableUser} />
          </div>
        </div>
        <div className="main">
          <UserCards users={users} onDelete={onDelete} onUpdate={onUpdate} />
        </div>
      </div>
    </>
  );
}

export default App;
