class DomainError(Exception):
    pass


class DuplicateTaskDescriptionError(DomainError):
    pass


class InvalidTaskDescriptionError(DomainError):
    pass


class TaskNotFoundError(DomainError):
    pass
