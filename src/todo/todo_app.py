from todo import exceptions, repository, todo_list


class TodoApp:
    def __init__(self, repo: repository.Repository) -> None:
        self.repo = repo

    def list_tasks(self) -> todo_list.TodoList:
        return self.repo.get_todo_list()

    def create_task(self, description: str) -> None:
        self._validate_task_description(description)

        todo_list = self.repo.list_tasks()
        todo_list.append(description)

        self.repo.add_todo_list(todo_list)

    def _validate_task_description(self, description: str) -> None:
        if not description.strip():
            raise exceptions.InvalidTaskDescriptionError(
                "Task description must be a non empty string"
            )
