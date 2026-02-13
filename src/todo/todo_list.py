import attrs

from todo import exceptions, task


@attrs.define
class TodoList:
    tasks: list[task.Task]
    _task_descriptions: set[str] = attrs.field(init=False)

    def __attrs_post_init__(self) -> None:
        self._task_descriptions = {t.description for t in self.tasks}

    def add_task(self, new_task: task.Task) -> None:
        if new_task.description in self._task_descriptions:
            msg = f"Duplicate task description: '{new_task.description}'"
            raise exceptions.DuplicateTaskDescriptionError(msg)

        self._task_descriptions.add(new_task.description)
        self.tasks.append(new_task)
