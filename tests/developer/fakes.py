class FakeRepository:
    def list_tasks(self) -> list[str]:
        return []

    def add_todo_list(self, tasks: list[str]) -> None:
        pass
