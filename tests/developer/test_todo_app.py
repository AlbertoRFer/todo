import pytest

from todo import exceptions, repository, todo_app


@pytest.fixture
def app(fake_repo: repository.Repository) -> todo_app.TodoApp:
    return todo_app.TodoApp(fake_repo)


def test_list_tasks_throw_exception_on_empty_task_description(
    app: todo_app.TodoApp,
) -> None:
    with pytest.raises(exceptions.InvalidTaskDescriptionError):
        app.create_task("")
