import pathlib

from todo import repository, storage, todo_app


def create_todo_app() -> todo_app.TodoApp:
    storage_path = pathlib.Path.cwd() / "todo.json"
    repo_storage = storage.JsonStorage(storage_path)
    repo = repository.TaskRepository(repo_storage)
    return todo_app.TodoApp(repo)
