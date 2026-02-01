import json
import pathlib


class TaskRepository:
    def __init__(self, repo_file_path: pathlib.Path) -> None:
        self.repo_file_path = repo_file_path

    def list_tasks(self) -> list[str]:
        with open(self.repo_file_path) as f:
            return json.load(f)
