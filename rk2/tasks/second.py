
from schemas.teacher import Degree


def find_departments_with_candidates(one_to_many: list[tuple[str, Degree, str]]) -> list[tuple[str, str]]:
    department_candidates_dict: dict[str, list[str]] = {}

    for teacher_name, degree, department_name in one_to_many:
        if degree == Degree.candidate:
            if department_name not in department_candidates_dict:
                department_candidates_dict[department_name] = []
            department_candidates_dict[department_name].append(teacher_name)

    res: list[tuple[str, str]] = []
    for department_name, candidates in sorted(department_candidates_dict.items()):
        candidates_str = ", ".join(candidates)
        res.append((department_name, candidates_str))

    return res
