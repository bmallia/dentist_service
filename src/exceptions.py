class Error(Exception):
    data = {}
    name = None

    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.data = kwargs.get("data")
        self.name = kwargs.get("name")


class AnalyzeError(Error):
    def __str__(self):
        self.name = 'saati-analyzer-error'
        return f"{self.name} - {self.data}"


class DatabaseError(Error):
    def __str__(self):
        self.name = 'database-error'
        return f"{self.name} - {self.data}"


class HTTPError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
