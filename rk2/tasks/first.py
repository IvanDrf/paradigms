from schemas.teacher import Degree


def find_doctors_of_science(one_to_many: list[tuple[str, Degree, str]]) -> list[tuple[str, str]]:
    res: list[tuple[str, str]] = [
        (teacher_name, department_name)
        for teacher_name, degree, department_name in one_to_many
        if degree.value == Degree.scientist.value
    ]

    return res
