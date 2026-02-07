from todo import task_repository


class TodoApp:
    def __init__(self, repo: task_repository.TaskRepository) -> None:
        self.repo = repo

    def list_tasks(self) -> list[str]:
        return self.repo.list_tasks()

    def create_task(self, description: str) -> None:
        todo_list = self.repo.list_tasks()
        todo_list.append(description)
        self.repo.add_todo_list(todo_list)
