from todo import task_repository


class TodoApp:
    def __init__(self, repo: task_repository.TaskRepository) -> None:
        self.repo = repo
