from schemas.teacher import Degree
from tasks.first import find_doctors_of_science
from tasks.second import find_departments_with_candidates
from tasks.third import find_related_teachers_and_deps
from tests.fixture.relations import many_to_many, one_to_many


def test_first_task(one_to_many: list[tuple[str, Degree, str]]) -> None:
    first_res: list[tuple[str, str]] = find_doctors_of_science(one_to_many)

    expected: list[tuple[str, str]] = [
        ('Иванов', 'Математика'), ('Овечкин', 'Физика'), ('Овечкин', 'Химия')
    ]

    assert first_res == expected


def test_second_task(one_to_many: list[tuple[str, Degree, str]]) -> None:
    second_res = find_departments_with_candidates(one_to_many)

    expected: list[tuple[str, str]] = [
        ('История', 'Козлова'), ('Литература', 'Петрова'),
        ('Математика', 'Петрова'), ('Программирование', 'Петрова, Козлова')
    ]

    assert second_res == expected


def test_third_task(many_to_many: list[tuple[str, Degree, str]]) -> None:
    third_res = find_related_teachers_and_deps(many_to_many)

    expected: list[tuple[str, Degree, str]] = [
        ('Козлова', Degree.candidate, 'История'),
        ('Николаев', Degree.doctor, 'История'),
        ('Петрова', Degree.candidate, 'Литература'),
        ('Иванов', Degree.scientist, 'Математика'),
        ('Петрова', Degree.candidate, 'Математика'),
        ('Козлова', Degree.candidate, 'Программирование'),
        ('Николаев', Degree.doctor, 'Программирование'),
        ('Петрова', Degree.candidate, 'Программирование'),
        ('Овечкин', Degree.scientist, 'Физика'),
        ('Овечкин', Degree.scientist, 'Химия')
    ]

    assert third_res == expected
