class Department:
    __slots__ = ('id', 'name', 'faculty')

    def __init__(self, id: int, name: str, faculty: str) -> None:
        self.id: int = id
        self.name: str = name
        self.faculty: str = faculty
