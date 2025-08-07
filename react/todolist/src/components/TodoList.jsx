import React from "react";
import "../App.css";

const TodoList = ({ todos, toggleComplete, deleteTodo, getEditIndex }) => {
  return (
    <div>
      {todos.map((todo, i) => (
        <div
          style={{ textDecoration: todo.completed ? "line-through" : "none" }}
          key={i}
          className="todo-item"
        >
          <span
            onClick={() => toggleComplete(i)}
            className={`todo-text ${todo.completed ? "completed" : ""}`}
          >
            {todo.text}
          </span>
          <div className="todo-buttons">
            <button onClick={() => getEditIndex(i)}>
              <i class="fa-solid fa-pen-to-square"></i>
            </button>
            <button onClick={() => deleteTodo(i)}>
              <i class="fa-solid fa-trash"></i>
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default TodoList;
