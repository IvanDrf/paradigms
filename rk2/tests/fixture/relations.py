from pytest import fixture

from entities.courses import course_assignments
from entities.departments import departments
from entities.teachers import teachers
from schemas.teacher import Degree


@fixture(scope='session')
def one_to_many() -> list[tuple[str, Degree, str]]:
    return [
        (teacher.name, teacher.academic_degree, department.name)
        for teacher in teachers
        for assignment in course_assignments
        for department in departments
        if teacher.id == assignment.teacher_id and department.id == assignment.department_id
    ]


@fixture(scope='session')
def many_to_many() -> list[tuple[str, Degree, str]]:
    temp: list[tuple[str, int, int]] = [
        (department.name, ca.department_id, ca.teacher_id)
        for department in departments
        for ca in course_assignments
        if department.id == ca.department_id
    ]

    # связь многие ко многим
    return [
        (teacher.name, teacher.academic_degree, department_name)
        for department_name, _, teacher_id in temp
        for teacher in teachers if teacher.id == teacher_id
    ]
