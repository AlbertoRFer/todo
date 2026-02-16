import uuid

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


def test_todo_list_can_get_task_from_id() -> None:
    # Given a todo list with tasks
    tasks = [task.Task(f"Task {n}") for n in range(1, 4)]
    todo = todo_list.TodoList(tasks)
    lookup_id = tasks[2].id

    # When we get a task
    output_task = todo.get_task(lookup_id)

    # Then the task is returned
    assert tasks[2] == output_task


def test_todo_list_throws_exception_when_task_does_not_exist() -> None:
    # Given a todo list with tasks
    tasks = [task.Task(f"Task {n}") for n in range(1, 4)]
    todo = todo_list.TodoList(tasks)
    random_lookup_id = uuid.uuid4()

    # When we try to get a Task using a random lookup id
    # Then an exception is raised
    with pytest.raises(exceptions.TaskNotFoundError):
        todo.get_task(random_lookup_id)


def test_todo_list_can_update_task_status() -> None:
    # Given a todo list with tasks
    tasks = [task.Task(f"Task {n}") for n in range(1, 4)]
    todo = todo_list.TodoList(tasks)

    task_id = tasks[2].id
    new_status = True

    # When we update the status of a task
    todo.update_task_status(task_id, new_status)

    # Then the task status is updated
    assert new_status == todo.get_task(task_id).is_done
