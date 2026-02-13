from todo import repository, task, todo_list


class TodoApp:
    def __init__(self, repo: repository.Repository) -> None:
        self.repo = repo

    def list_tasks(self) -> todo_list.TodoList:
        return self.repo.get_todo_list()

    def create_task(self, description: str) -> None:
        new_task = task.Task(description)

        todo_list = self.repo.get_todo_list()
        todo_list.add_task(new_task)

        self.repo.add_todo_list(todo_list)
