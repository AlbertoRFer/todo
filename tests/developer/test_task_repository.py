import json
import pathlib

import pytest
import pytest_cases

from todo import task_repository


@pytest.fixture
def repo_file_path(tmp_path: pathlib.Path) -> pathlib.Path:
    return tmp_path / "tasks.json"


@pytest.fixture
def repo(repo_file_path: pathlib.Path) -> task_repository.TaskRepository:
    return task_repository.TaskRepository(repo_file_path)


def create_json_file(file_path: pathlib.Path, tasks: list[str]) -> None:
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
