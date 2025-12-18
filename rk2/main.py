from entities.courses import course_assignments
from entities.departments import departments
from entities.teachers import teachers
from schemas.teacher import Degree
from tasks.first import find_doctors_of_science
from tasks.second import find_departments_with_candidates
from tasks.third import find_related_teachers_and_deps


def main() -> None:
    # связь один ко многим
    one_to_many: list[tuple[str, Degree, str]] = [
        (teacher.name, teacher.academic_degree, department.name)
        for teacher in teachers
        for assignment in course_assignments
        for department in departments
        if teacher.id == assignment.teacher_id and department.id == assignment.department_id
    ]

    temp: list[tuple[str, int, int]] = [
        (department.name, ca.department_id, ca.teacher_id)
        for department in departments
        for ca in course_assignments
        if department.id == ca.department_id
    ]

    # связь многие ко многим
    many_to_many: list[tuple[str, Degree, str]] = [
        (teacher.name, teacher.academic_degree, department_name)
        for department_name, _, teacher_id in temp
        for teacher in teachers if teacher.id == teacher_id
    ]

    print('Задание 1')
    first_res: list[tuple[str, str]] = find_doctors_of_science(one_to_many)
    print('Преподаватели с ученой степенью:')
    for teacher_name, department_name in first_res:
        print(f'{teacher_name} - {department_name}')
    print()

    print('Задание 2')
    second_res: list[tuple[str, str]
                     ] = find_departments_with_candidates(one_to_many)
    print('Кафедры с преподавателем кандидатами:')
    for department_name, teacher_name in second_res:
        print(f'{department_name}: {teacher_name}')
    print()

    print('Задание 3')
    third_res = find_related_teachers_and_deps(many_to_many)
    print('Все связанные преподаватели и кафедры:')
    for teacher_name, degree, department_name in third_res:
        print(f'{department_name}: {teacher_name} - {degree.value}')


if __name__ == '__main__':
    main()
