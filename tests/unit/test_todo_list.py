import pytest

from todo import exceptions, task, todo_list


def test_todo_list_can_add_tasks() -> None:
    # Given a todo list with tasks and a new task
    tasks = [task.Task(f"Task {n}") for n in range(1, 4)]
    new_task = task.Task("New Task")
    todo = todo_list.TodoList(tasks)

    # When we add a new task
    todo.add_task(new_task)

    # Then the new task is added
    tasks.append(new_task)
    assert tasks == todo.tasks


def test_todo_list_raises_exception_when_adding_duplicate_tasks() -> None:
    # Given a todo list with tasks
    tasks = [task.Task(f"Task {n}") for n in range(1, 4)]
    todo = todo_list.TodoList(tasks)

    # When we try to add a duplicate task
    # Then an exception is raised
    with pytest.raises(exceptions.DuplicateTaskDescriptionError):
        todo.add_task(task.Task("Task 2"))
