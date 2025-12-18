from schemas.teacher import Degree, Teacher


teachers: list[Teacher] = [
    # основные кафедры для препрдавателей

    # математика
    Teacher(1, 'Иванов', Degree.scientist, 1),
    # математика
    Teacher(2, 'Петрова', Degree.candidate, 1),
    # физика
    Teacher(3, 'Овечкин', Degree.scientist, 2),
    # история
    Teacher(4, 'Козлова', Degree.candidate, 4),
    # программирование
    Teacher(5, 'Николаев', Degree.doctor, 3)
]
