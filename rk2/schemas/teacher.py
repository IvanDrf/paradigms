from enum import Enum


class Degree(Enum):
    doctor = 'доктор'
    candidate = 'кандидат'
    scientist = 'ученый'


class Teacher:
    __slots__ = ('id', 'name', 'academic_degree', 'department_id')

    def __init__(self, id: int, name: str, academic_degree: Degree, department_id: int) -> None:
        self.id: int = id
        self.name: str = name
        self.academic_degree: Degree = academic_degree
        self.department_id: int = department_id
