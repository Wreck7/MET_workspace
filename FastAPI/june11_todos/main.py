from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def post_todos(title, desc):
    todo = {
        'id': str(len(todos)+1),
        'title': title,
        'desc': desc
    }
    todos.append(todo)
    return todos

@app.put("/todos")
def update_todos(id, updated_desc):
    for todo in todos:
        if todo['id'] == id:
            todo['desc'] = updated_desc
            break
        return 'invalid id given'

@app.delete('/todos')
def delete_todo(id: int):
    for i in range(len(todos)):
        if todos[i]["id"] == str(id):
            todos.pop(i)
            return 'deleted todo'
        