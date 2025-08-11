import React, { useState } from "react";
import "./App.css";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";

function App() {
  const [todos, setTodos] = useState([]);
  const [editIndex, setEditIndex] = useState(null);

  const toggleComplete = (id) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  const handleAddTodo = (text) => {
    const newTodo = {
      text,
      completed: false,
    };
    setTodos([newTodo, ...todos]);
  };

  const deleteTodo = (index) => {
    setTodos(todos.filter((todo, i) => i !== index));
  };

  const getEditID = (id) => {
    setEditIndex(id);
    // console.log(id)
  };

  const editTodo = (text) => {
    // todos[editIndex].text = text
    // setTodos(todos)
    // setEditIndex(null)
    const updatedTodos = [...todos];
    updatedTodos[editIndex] = { ...updatedTodos[editIndex], text };
    setTodos(updatedTodos);
    setEditIndex(null);
  };
  return (
    <div className="app">
      <div className="container">
        <h1>My Todo App</h1>
        <TodoForm
          addTodo={handleAddTodo}
          todo={todos[editIndex]}
          editIndex={editIndex}
          onEdit={editTodo}
        />

        <TodoList
          todos={todos}
          toggleComplete={toggleComplete}
          deleteTodo={deleteTodo}
          getEditIndex={getEditID}
        />
      </div>
    </div>
  );
}

export default App;
