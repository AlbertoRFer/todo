import json
import pathlib

from todo import storage


class RepositoryError(Exception):
    pass


class TaskRepository:
    def __init__(self, repo_file_path: pathlib.Path) -> None:
        self.storage = storage.JsonStorage(repo_file_path)

    def list_tasks(self) -> list[str]:
        try:
            return self._read_json_file()
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as err:
            raise RepositoryError("Unable to read repository file") from err

    def _read_json_file(self) -> list[str]:
        data = self.storage.load_data()

        if not isinstance(data, list):
            raise RepositoryError("Tasks data must be a list")

        for task_description in data:
            if not isinstance(task_description, str):
                raise RepositoryError("Task description must be a string")

            if not task_description.strip():
                raise RepositoryError("Task description must be a non empty string")

        return data
