import "./App.css";
import React, { useState, useEffect } from "react";

function Todos({ todos, loading, getIndex }) {
  return (
    <div className="container">
      <p className="py-4">{loading ? "Loading..." : ""}</p>
      <span>
        <h2 className="mb-4 py-4">Todo List</h2>{" "}
      </span>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Todo</th>
            <th>Completed</th>
            <th>User ID</th>
          </tr>
        </thead>
        <tbody>
          {todos.map((todo) => (
            <tr
              className="cursor-pointer"
              key={todo.id}
              onClick={() => getIndex(todo.id)}
            >
              <td>{todo.id}</td>
              <td>{todo.todo}</td>
              <td>{todo.completed ? "✅ Yes" : "❌ No"}</td>
              <td>{todo.userId}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const OneTodo = ({ index, getIndex }) => {
  const [todo, setTodo] = useState({});

  useEffect(() => {
    async function fetchTodo() {
      const response = await fetch(`https://dummyjson.com/todos/${index}`);
      const data = await response.json();
      setTodo(data);
    }
    fetchTodo();
  }, []);

  return (
    <div>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Todo</th>
            <th>Completed</th>
            <th>User ID</th>
          </tr>
        </thead>
        <tbody>
          <tr
            className="cursor-pointer"
            key={todo.id}
            onClick={() => getIndex(null)}
          >
            <td>{todo.id}</td>
            <td>{todo.todo}</td>
            <td>{todo.completed ? "✅ Yes" : "❌ No"}</td>
            <td>{todo.userId}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

function App() {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [clickIndex, setClickIndex] = useState(null);

  useEffect(() => {
    fetch("https://dummyjson.com/todos")
      .then((res) => {
        if (!res.ok) throw new Error("failed to fetch");
        return res.json();
      })
      .then((data) => {
        setTodos(data.todos);
        setLoading(false);
      });
  }, []);

  function getIndex(i) {
    setClickIndex(i);
    // console.log(i);
  }

  return (
    <>
      {clickIndex == null ? (
        <Todos todos={todos} loading={loading} getIndex={getIndex} />
      ) : (
        <OneTodo index={clickIndex} getIndex={getIndex} />
      )}
    </>
  );
}

export default App;
