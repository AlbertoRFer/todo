import typing

import attrs

from todo import exceptions


@attrs.define
class Task:
    description: str = attrs.field()

    @description.validator
    def _validate_description(self, _: typing.Any, value: str) -> None:
        if not value.strip():
            msg = "Task description cannot be empty."
            raise exceptions.InvalidTaskDescriptionError(msg)
