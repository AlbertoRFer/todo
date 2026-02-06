import dataclasses
import enum


class RepositoryErrorCode(enum.Enum):
    READ_FAILED = (1001, "Unable to read from repository")
    INVALID_DATA = (1002, "Invalid Repository data")

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message


@dataclasses.dataclass
class RepositoryError(Exception):
    error: RepositoryErrorCode
    details: str | None = None

    def __str__(self) -> str:
        main_msg = f"[E{self.error.code}] {self.error.message}"
        if self.details is not None:
            return f"{main_msg}: {self.details}"

        return main_msg


class StorageErrorCode(enum.Enum):
    STORAGE_NOT_FOUND = (1010, "Storage not found")
    READ_FAILED = (1011, "Unable to read from storage")

    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message


@dataclasses.dataclass
class StorageError(Exception):
    error: StorageErrorCode
    details: str | None = None

    def __str__(self) -> str:
        main_msg = f"[E{self.error.code}] {self.error.message}"
        if self.details is not None:
            return f"{main_msg}: {self.details}"

        return main_msg
