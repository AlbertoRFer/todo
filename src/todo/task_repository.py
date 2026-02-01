import json
import pathlib


class TaskRepository:
    def __init__(self, repo_file_path: pathlib.Path) -> None:
        self.repo_file_path = repo_file_path

    def list_tasks(self) -> list[str]:
        try:
            return self._read_json_file()
        except FileNotFoundError:
            return []

    def _read_json_file(self) -> list[str]:
        with open(self.repo_file_path, encoding="utf-8") as f:
            return json.load(f)
