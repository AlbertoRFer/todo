import pathlib

from todo import storage, task_repository, todo_app


def create_todo_app() -> todo_app.TodoApp:
    storage_path = pathlib.Path.cwd() / "todo.json"
    repo_storage = storage.JsonStorage(storage_path)
    repo = task_repository.TaskRepository(repo_storage)
    return todo_app.TodoApp(repo)
