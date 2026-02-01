import json
import pathlib
import typing

import pytest
import pytest_cases

from todo import task_repository


@pytest.fixture
def repo_file_path(tmp_path: pathlib.Path) -> pathlib.Path:
    return tmp_path / "tasks.json"


@pytest.fixture
def repo(repo_file_path: pathlib.Path) -> task_repository.TaskRepository:
    return task_repository.TaskRepository(repo_file_path)


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
    "file_content, error_msg",
    [
        ("", "Unable to read repository file"),
        ('["Task 1', "Unable to read repository file"),
        ("{}", "Tasks data must be a list"),
        ("[5]", "Task description must be a string"),
        ('[""]', "Task description must be a non empty string"),
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
    error_msg: str,
) -> None:
    # Given a repo file with invalid data
    create_text_file(repo_file_path, file_content)

    # When we list tasks
    # Then an exeption is raised
    with pytest.raises(task_repository.RepositoryError, match=error_msg):
        output_tasks = repo.list_tasks()
