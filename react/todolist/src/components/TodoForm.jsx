import React, { useState, useEffect } from "react";
import "../App.css";

const TodoForm = ({ addTodo, todo, editIndex, onEdit }) => {
  const [text, setText] = useState("");
  const [editText, setEditText] = useState('');

  useEffect(() => {
  setEditText(todo?.text || "");
}, [todo]);


  const handleAddTodo = (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    addTodo(text);
    setText("");
  };
  const handleEditTodo = (e) => {
    e.preventDefault();
    onEdit(editText);
    setEditText("");
  };

  return (
    <>
      {editIndex === null ? (
        <form onSubmit={handleAddTodo}>
          <input
            type="text"
            placeholder="Add a new task"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button type="submit">Add</button>
        </form>
      ) : (
        <form onSubmit={handleEditTodo}>
          <input
            type="text"
            placeholder="Add a new task"
            value={editText}
            onChange={(e) => setEditText(e.target.value)}
          />
          <button type="submit">Edit</button>
        </form>
      )}
    </>
  );
};

export default TodoForm;
