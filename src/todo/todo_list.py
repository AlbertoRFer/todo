import uuid

import attrs

from todo import exceptions, task


@attrs.define
class TodoList:
    tasks: list[task.Task]
    _task_descriptions: set[str] = attrs.field(init=False)
    _tasks_uuid_map: dict[uuid.UUID, task.Task] = attrs.field(init=False)

    def __attrs_post_init__(self) -> None:
        self._task_descriptions = {t.description for t in self.tasks}
        self._tasks_uuid_map = {t.id: t for t in self.tasks}

    def add_task(self, new_task: task.Task) -> None:
        if new_task.description in self._task_descriptions:
            msg = f"Duplicate task description: '{new_task.description}'"
            raise exceptions.DuplicateTaskDescriptionError(msg)

        self._task_descriptions.add(new_task.description)
        self.tasks.append(new_task)

    def get_task(self, task_id: uuid.UUID) -> task.Task:
        try:
            return self._tasks_uuid_map[task_id]
        except KeyError as err:
            msg = f"Task not found: missing id '{task_id}'"
            raise exceptions.TaskNotFoundError(msg) from err
