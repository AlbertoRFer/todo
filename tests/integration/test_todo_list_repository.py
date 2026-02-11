import json
import pathlib
import typing

import pytest

from todo import repository, task, todo_list


@pytest.fixture
def repo_file_path(tmp_path: pathlib.Path) -> pathlib.Path:
    return tmp_path / "tasks.json"


@pytest.fixture
def repo(repo_file_path: pathlib.Path) -> repository.TodoListJsonRepository:
    return repository.TodoListJsonRepository(repo_file_path)


def write_json_file(file_path: pathlib.Path, tasks: typing.Any) -> None:
    with open(file_path, "w") as f:
        json.dump(tasks, f)


def read_json_file(file_path: pathlib.Path) -> typing.Any:
    with open(file_path) as f:
        return json.load(f)


def test_repository_can_save_a_todo_list(
    repo: repository.TodoListJsonRepository,
) -> None:
    # Given a todo list
    tasks = [task.Task(f"Task {n}") for n in range(1, 4)]
    todo = todo_list.TodoList(tasks)

    # When the repository saves the todo list
    repo.add_todo_list(todo)

    # Then the todo list is saved
    data = read_json_file(repo.file_path)
    for expected_task, actual_task in zip(tasks, data["tasks"], strict=True):
        assert expected_task.description == actual_task["description"]


def test_repository_can_retrieve_a_todo_list(
    repo: repository.TodoListJsonRepository,
) -> None:
    # Given a file containing a todo list
    task_descriptions = [f"Task {n}" for n in range(1, 4)]
    data = {"tasks": [{"description": desc} for desc in task_descriptions]}
    write_json_file(repo.file_path, data)

    # When we retrieve the todo list
    todo = repo.get_todo_list()

    # Then the todo list is returned
    tasks = [task.Task(desc) for desc in task_descriptions]
    assert todo_list.TodoList(tasks) == todo
