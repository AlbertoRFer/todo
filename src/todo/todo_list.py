import attrs

from todo import task


@attrs.define
class TodoList:
    tasks: list[task.Task]
