from schemas.teacher import Degree


def find_related_teachers_and_deps(many_to_many: list[tuple[str, Degree, str]]) -> list[tuple[str, Degree, str]]:
    return sorted(many_to_many, key=lambda x: (x[2], x[0]))
