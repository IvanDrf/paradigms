from schemas.course import CourseAssignment


# один преподаватель может вести на в нескольких кафедрах
course_assignments: list[CourseAssignment] = [
    CourseAssignment(1, 1),

    CourseAssignment(1, 2),
    CourseAssignment(3, 2),
    CourseAssignment(5, 2),

    CourseAssignment(2, 3),
    CourseAssignment(6, 3),

    CourseAssignment(4, 4),
    CourseAssignment(3, 4),

    CourseAssignment(3, 5),
    CourseAssignment(4, 5),
]
