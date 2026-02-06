import json
import pathlib
import typing

from todo import exceptions


class Storage(typing.Protocol):
    def load_data(self) -> typing.Any: ...
    def save_data(self, data: list[str]) -> None: ...


class JsonStorage:
    def __init__(self, file_path: pathlib.Path) -> None:
        self.file_path = file_path

    def load_data(self) -> typing.Any:
        try:
            return self._json_load()
        except FileNotFoundError as err:
            raise exceptions.StorageError(
                exceptions.StorageErrorCode.STORAGE_NOT_FOUND
            ) from err
        except json.JSONDecodeError as err:
            raise exceptions.StorageError(
                exceptions.StorageErrorCode.READ_FAILED
            ) from err

    def _json_load(self) -> typing.Any:
        with open(self.file_path, encoding="utf-8") as f:
            return json.load(f)

    def save_data(self, data: list[str]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)
