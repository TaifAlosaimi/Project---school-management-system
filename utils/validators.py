"""
This module checks that student, teacher, and course data
contains valid values before the data is used by the system.
"""

# Custom Exceptions
# ============================================================

class InvalidStudentError(Exception):
    """Raised when student data is invalid."""

    pass


class InvalidTeacherError(Exception):
    """Raised when teacher data is invalid."""

    pass


class InvalidCourseError(Exception):
    """Raised when course data is invalid."""

    pass


# Helper Validation
# ============================================================

def validate_id(value, prefix, field_name):
    """
    Validate an ID that starts with a specific prefix.
    """

    # Check that the value exists.
    if not value:
        raise ValueError(f"{field_name} is required.")

    # IDs should be strings.
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string.")

    # Remove accidental spaces from the beginning/end.
    value = value.strip()

    # Check that the ID starts with the required letter.
    if not value.startswith(prefix):
        raise ValueError(
            f"{field_name} must start with '{prefix}'."
        )

    # Check that the remaining characters are digits.
    if not value[1:].isdigit():
        raise ValueError(
            f"{field_name} must contain digits after '{prefix}'."
        )

    return True


def validate_name(name, field_name="Name"):
    """Validate that a name is not empty and contains letters only."""

    # Required fields cannot be empty.
    if not name:
        raise ValueError(f"{field_name} cannot be empty.")

    # Name should be a string.
    if not isinstance(name, str):
        raise ValueError(f"{field_name} must be a string.")

    # Remove spaces around the name.
    name = name.strip()

    # Check again after removing whitespace.
    if not name:
        raise ValueError(f"{field_name} cannot be empty.")

    # Allow names containing spaces, such as "Ahmed Ali".
    # Every part of the name must contain letters only.
    if not all(part.isalpha() for part in name.split()):
        raise ValueError(
            f"{field_name} must contain letters only."
        )

    return True

# ============================================================
# Student Validation
# ============================================================

def validate_student(student):
    """
    Validate a student record.

    Required fields:
        student_id
        name
        age
        enrolled_courses
    """

    # The record itself must be a dictionary.
    if not isinstance(student, dict):
        raise InvalidStudentError(
            "Student record must be a dictionary."
        )

    try:
    
        # Validate required fields
        # ----------------------------------------------------

        required_fields = [
            "student_id",
            "name",
            "age",
            "enrolled_courses"
        ]

        for field in required_fields:
            if field not in student:
                raise InvalidStudentError(
                    f"Missing student field: {field}"
                )


        # Validate Student ID
        # ----------------------------------------------------

        validate_id(
            student["student_id"],
            "S",
            "Student ID"
        )


    
        # Validate Student Name
        # ----------------------------------------------------

        validate_name(
            student["name"],
            "Student name"
        )


        # Validate Age
        # ----------------------------------------------------

        age = student["age"]

        # Age must be an integer.
        if not isinstance(age, int):
            raise InvalidStudentError(
                "Age must be an integer."
            )

        # Age must be positive.
        if age <= 0:
            raise InvalidStudentError(
                "Age must be greater than 0."
            )

        
        # Validate Enrolled Courses
        # ----------------------------------------------------

        if not isinstance(student["enrolled_courses"], list):
            raise InvalidStudentError(
                "Enrolled courses must be a list."
            )

        # Every course ID should be stored as a string.
        for course_code in student["enrolled_courses"]:
            if not isinstance(course_code, str):
                raise InvalidStudentError(
                    "Each enrolled course must be a string."
                )

        return True

    except ValueError as error:
        # Convert helper validation errors into
        # our custom Student error.
        raise InvalidStudentError(str(error)) from error



# ============================================================
# Teacher Validation
# ============================================================



def validate_teacher(teacher):
    """
    Validate a teacher record.

    Required fields:
        teacher_id
        name
        subject
    """

    if not isinstance(teacher, dict):
        raise InvalidTeacherError(
            "Teacher record must be a dictionary."
        )

    try:
        # Check that all required fields exist.
        required_fields = [
            "teacher_id",
            "name",
            "subject"
        ]

        for field in required_fields:
            if field not in teacher:
                raise InvalidTeacherError(
                    f"Missing teacher field: {field}"
                )

        # Validate Teacher ID.
        validate_id(
            teacher["teacher_id"],
            "T",
            "Teacher ID"
        )

        # Validate Teacher Name.
        validate_name(
            teacher["name"],
            "Teacher name"
        )

        # Validate Subject.
        subject = teacher["subject"]

        if not isinstance(subject, str):
            raise InvalidTeacherError(
                "Subject must be a string."
            )

        if not subject.strip():
            raise InvalidTeacherError(
                "Subject cannot be empty."
            )

        return True

    except ValueError as error:
        raise InvalidTeacherError(str(error)) from error


# ============================================================
# Course Validation
# ============================================================

def validate_course(course):
    """
    Validate a course record.

    Required fields:
        course_code
        course_title
        assigned_teacher
        enrolled_student_ids
    """

    if not isinstance(course, dict):
        raise InvalidCourseError(
            "Course record must be a dictionary."
        )

    # Check required fields.
    required_fields = [
        "course_code",
        "course_title",
        "assigned_teacher",
        "enrolled_student_ids"
    ]

    for field in required_fields:
        if field not in course:
            raise InvalidCourseError(
                f"Missing course field: {field}"
            )

    
    # Validate Course Code
    # --------------------------------------------------------

    course_code = course["course_code"]

    if not isinstance(course_code, str):
        raise InvalidCourseError(
            "Course code must be a string."
        )

    if not course_code.strip():
        raise InvalidCourseError(
            "Course code cannot be empty."
        )

    # Validate Course Title
    # --------------------------------------------------------

    course_title = course["course_title"]

    if not isinstance(course_title, str):
        raise InvalidCourseError(
            "Course title must be a string."
        )

    if not course_title.strip():
        raise InvalidCourseError(
            "Course title cannot be empty."
        )

    # Validate Assigned Teacher
    # --------------------------------------------------------

    assigned_teacher = course["assigned_teacher"]

    if assigned_teacher is not None:
        if not isinstance(assigned_teacher, str):
            raise InvalidCourseError(
                "Assigned teacher must be a string or None."
            )

    # Validate Enrolled Students
    # --------------------------------------------------------

    enrolled_students = course["enrolled_student_ids"]

    if not isinstance(enrolled_students, list):
        raise InvalidCourseError(
            "Enrolled student IDs must be a list."
        )

    # Every student ID must be a string.
    for student_id in enrolled_students:
        if not isinstance(student_id, str):
            raise InvalidCourseError(
                "Each enrolled student ID must be a string."
            )

        if not student_id.strip():
            raise InvalidCourseError(
                "Student IDs cannot be empty."
            )

    return True