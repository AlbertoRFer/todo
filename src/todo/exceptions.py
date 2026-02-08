import dataclasses
import enum
import typing


class BaseErrorCode(enum.Enum):
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message


@dataclasses.dataclass
class BaseError(Exception):
    error: BaseErrorCode
    details: str | None = None

    def __str__(self) -> str:
        main_msg = f"[E{self.error.code}] {self.error.message}"
        if self.details is not None:
            return f"{main_msg}: {self.details}"

        return main_msg


class RepositoryErrorCode(BaseErrorCode):
    READ_FAILED = (1001, "Unable to read from repository")
    INVALID_DATA = (1002, "Invalid Repository data")


@dataclasses.dataclass
class RepositoryError(BaseError):
    pass


class StorageErrorCode(BaseErrorCode):
    STORAGE_NOT_FOUND = (1010, "Storage not found")
    READ_FAILED = (1011, "Unable to read from storage")


@dataclasses.dataclass
class StorageError(BaseError):
    pass


class InvalidTaskDescriptionError(Exception):
    pass
