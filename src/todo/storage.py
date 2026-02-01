import json
import pathlib
import typing


class Storage(typing.Protocol):
    def load_data(self) -> typing.Any: ...


class JsonStorage:
    def __init__(self, file_path: pathlib.Path) -> None:
        self.file_path = file_path

    def load_data(self) -> typing.Any:
        with open(self.file_path, encoding="utf-8") as f:
            return json.load(f)
