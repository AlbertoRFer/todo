import json
import typing

from todo import storage


class RepositoryError(Exception):
    pass


class TaskRepository:
    def __init__(self, repo_storage: storage.Storage) -> None:
        self.storage = repo_storage

    def list_tasks(self) -> list[str]:
        data = self._load_data()
        return self._validate_data(data)

    def _load_data(self) -> typing.Any:
        try:
            return self.storage.load_data()
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as err:
            raise RepositoryError("Unable to read repository file") from err

    def _validate_data(self, data: typing.Any) -> list[str]:
        if not isinstance(data, list):
            raise RepositoryError("Tasks data must be a list")

        for task_description in data:
            if not isinstance(task_description, str):
                raise RepositoryError("Task description must be a string")

            if not task_description.strip():
                raise RepositoryError("Task description must be a non empty string")

        return data
