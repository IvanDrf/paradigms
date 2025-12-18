class CourseAssignment:
    __slots__ = ('department_id', 'teacher_id')

    def __init__(self, department_id: int, teacher_id: int) -> None:
        self.department_id: int = department_id
        self.teacher_id: int = teacher_id
