import React from "react";
import "../App.css";

const TodoList = ({ todos, toggleComplete, deleteTodo, getEditIndex }) => {
  return (
    <div>
      {todos.map((todo, i) => (
        <div
          style={{ textDecoration: todo.completed ? "line-through" : "none" }} key={i}
        >
          <span onClick={() => toggleComplete(i)}>{todo.text}</span>
          <button onClick={() => deleteTodo(i)}>Delete</button>
          <button onClick={() => getEditIndex(i)}>Edit</button>
        </div>
      ))}
    </div>
  );
};

export default TodoList;
