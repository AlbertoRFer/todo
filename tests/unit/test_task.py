import pytest
import pytest_cases

from todo import exceptions, task


@pytest_cases.parametrize(
    "description",
    ["", " ", "\t", "\n"],
    ids=["empty", "whitespace", "tabs", "newlines"],
)
def test_task_raises_exception_on_empty_description(description: str) -> None:
    # Given an empty task description

    # When we create a task
    # Then an exception is raised
    with pytest.raises(exceptions.InvalidTaskDescriptionError):
        task.Task(description)
