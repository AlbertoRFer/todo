import json
import pathlib
import typing

import pytest
import pytest_cases

from todo import exceptions, storage, task_repository


@pytest.fixture
def repo_file_path(tmp_path: pathlib.Path) -> pathlib.Path:
    return tmp_path / "tasks.json"


@pytest.fixture
def repo(repo_file_path: pathlib.Path) -> task_repository.TaskRepository:
    json_storage = storage.JsonStorage(repo_file_path)
    return task_repository.TaskRepository(json_storage)


def create_json_file(file_path: pathlib.Path, tasks: typing.Any) -> None:
    with open(file_path, "w") as f:
        json.dump(tasks, f)


@pytest_cases.parametrize(
    "tasks",
    [[], ["Task 1"], ["Task 1", "Task 2", "Task 3"]],
    ids=["no tasks", "one task", "three tasks"],
)
def test_list_tasks_when_repo_file_exists(
    repo: task_repository.TaskRepository, repo_file_path: pathlib.Path, tasks: list[str]
) -> None:
    # Given a repo file that exists
    create_json_file(repo_file_path, tasks)

    # When we list tasks
    output_tasks = repo.list_tasks()

    # Then the tasks in the repo file are returned
    assert output_tasks == tasks


def test_list_tasks_when_repo_file_does_not_exist(
    repo: task_repository.TaskRepository,
) -> None:
    # Given a repo file that does not exist

    # When we list tasks
    output_tasks = repo.list_tasks()

    # Then an empty list is returned
    assert output_tasks == []


def create_text_file(file_path: pathlib.Path, text: str) -> None:
    with open(file_path, "w") as f:
        f.write(text)


@pytest_cases.parametrize(
    "file_content, error_code",
    [
        ("", exceptions.RepositoryErrorCode.READ_FAILED),
        ('["Task 1', exceptions.RepositoryErrorCode.READ_FAILED),
        ("{}", exceptions.RepositoryErrorCode.INVALID_DATA),
        ("[5]", exceptions.RepositoryErrorCode.INVALID_DATA),
        ('[""]', exceptions.RepositoryErrorCode.INVALID_DATA),
    ],
    ids=[
        "empty file",
        "invalid json",
        "wrong data structure",
        "wrong data decription type",
        "empty data description",
    ],
)
def test_list_tasks_when_invalid_data_in_repo_file(
    repo: task_repository.TaskRepository,
    repo_file_path: pathlib.Path,
    file_content: str,
    error_code: exceptions.RepositoryErrorCode,
) -> None:
    # Given a repo file with invalid data
    create_text_file(repo_file_path, file_content)

    # When we list tasks
    # Then an exception is raised
    with pytest.raises(exceptions.RepositoryError) as exc_info:
        repo.list_tasks()

    # And the correct error code is returned
    assert error_code == exc_info.value.error


def test_add_todo_list(
    repo: task_repository.TaskRepository, repo_file_path: pathlib.Path
) -> None:
    # Given an existent repo and a list of tasks
    create_text_file(repo_file_path, "[]")
    todo_list = ["Task 1", "Task 2", "Task 3"]

    # When we add a task list
    repo.add_todo_list(todo_list)

    # Then the task is added to the repo
    with open(repo_file_path) as f:
        data = json.load(f)

    assert todo_list == data
