import typing
import uuid

import attrs

from todo import exceptions


@attrs.define
class Task:
    description: str = attrs.field()
    _id: uuid.UUID = attrs.field(factory=uuid.uuid4)

    @description.validator
    def _validate_description(self, _: typing.Any, value: str) -> None:
        if not value.strip():
            msg = "Task description cannot be empty."
            raise exceptions.InvalidTaskDescriptionError(msg)

    @property
    def id(self) -> uuid.UUID:
        return self._id
