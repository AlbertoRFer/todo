import json
import pathlib
import typing

import cattrs

from todo import todo_list


class Repository(typing.Protocol):
    def get_todo_list(self) -> todo_list.TodoList: ...
    def add_todo_list(self, todo: todo_list.TodoList) -> None: ...
    def initialize(self) -> None: ...


EMPTY_TODO_LIST_SCHEMA: dict[str, typing.Any] = {"tasks": []}


class TodoListJsonRepository:
    def __init__(self, file_path: pathlib.Path) -> None:
        self._file_path = file_path

    def initialize(self) -> None:
        if not self._file_path.exists():
            self._save_json_data(EMPTY_TODO_LIST_SCHEMA)

    def get_todo_list(self) -> todo_list.TodoList:
        data = self._load_json_data()
        return cattrs.structure(data, todo_list.TodoList)

    def _load_json_data(self) -> typing.Any:
        with open(self._file_path, encoding="utf-8") as f:
            return json.load(f)

    def add_todo_list(self, todo: todo_list.TodoList) -> None:
        data_to_save = cattrs.unstructure(todo)
        self._save_json_data(data_to_save)

    def _save_json_data(self, data: typing.Any) -> None:
        with open(self._file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)
