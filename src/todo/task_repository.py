import json
import typing

from todo import exceptions, storage


class TaskRepository:
    def __init__(self, repo_storage: storage.Storage) -> None:
        self.storage = repo_storage

    def list_tasks(self) -> list[str]:
        data = self._load_data()
        return self._validate_data(data)

    def _load_data(self) -> typing.Any:
        try:
            return self.storage.load_data()
        except exceptions.StorageError as err:
            if err.error == exceptions.StorageErrorCode.STORAGE_NOT_FOUND:
                return []
            elif err.error == exceptions.StorageErrorCode.READ_FAILED:
                raise exceptions.RepositoryError(
                    exceptions.RepositoryErrorCode.READ_FAILED
                ) from err

    def _validate_data(self, data: typing.Any) -> list[str]:
        if not isinstance(data, list):
            raise exceptions.RepositoryError(
                exceptions.RepositoryErrorCode.INVALID_DATA,
                "Tasks data must be a list",
            )

        for task_description in data:
            if not isinstance(task_description, str):
                raise exceptions.RepositoryError(
                    exceptions.RepositoryErrorCode.INVALID_DATA,
                    "Task description must be a string",
                )

            if not task_description.strip():
                raise exceptions.RepositoryError(
                    exceptions.RepositoryErrorCode.INVALID_DATA,
                    "Task description must be a non empty string",
                )

        return data
