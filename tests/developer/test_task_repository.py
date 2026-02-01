import json
import pathlib

import pytest

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


def test_list_tasks_when_repo_file_has_no_tasks(
    repo: task_repository.TaskRepository, repo_file_path: pathlib.Path
) -> None:
    # Given a repo file that have no tasks
    create_json_file(repo_file_path, [])

    # When we list tasks
    output_tasks = repo.list_tasks()

    # Then there are no tasks
    assert output_tasks == []
