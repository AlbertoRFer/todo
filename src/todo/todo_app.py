from todo import task_repository


class TodoApp:
    def __init__(self, repo: task_repository.TaskRepository) -> None:
        self.repo = repo

    def list_tasks(self) -> list[str]:
        return self.repo.list_tasks()
