import pathlib

from todo import repository, todo_app


def create_todo_app() -> todo_app.TodoApp:
    storage_path = pathlib.Path.cwd() / "todo.json"
    repo = repository.TodoListJsonRepository(storage_path)
    return todo_app.TodoApp(repo)
