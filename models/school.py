from models.student import Student
from models.course import Course
from models.teacher import Teacher


class School:
    """Manage students, courses, and teachers in the school."""

    def __init__(self):
        # Store records in dictionaries for fast lookup by ID or code
        self.students = {}
        self.courses = {}
        self.teachers = {}


    def add_student(self, student):
        """Add a student to the school."""

        # Check that the student object is actually a Student.
        if not isinstance(student, Student):
            raise TypeError("student must be a Student object.")

        # Check for duplicate student IDs.
        if student.student_id in self.students:
            raise ValueError(
                f"Student ID {student.student_id} already exists."
            )

        # Use the student ID as the unique dictionary key.
        self.students[student.student_id] = student


    def add_course(self, course):
        """Add a course to the school."""

        # Check that the course object is actually a Course.
        if not isinstance(course, Course):
            raise TypeError("course must be a Course object.")

        # Check for duplicate course codes.
        if course.course_code in self.courses:
            raise ValueError(
                f"Course code {course.course_code} already exists."
            )

        # Use the course code as the unique dictionary key.
        self.courses[course.course_code] = course

        


    def add_teacher(self, teacher):
        """Add a teacher to the school."""

        # Check that the teacher object is actually a Teacher.
        if not isinstance(teacher, Teacher):
            raise TypeError("teacher must be a Teacher object.")

        # Check for duplicate teacher IDs.
        if teacher.teacher_id in self.teachers:
            raise ValueError(
                f"Teacher ID {teacher.teacher_id} already exists."
            )

        # Use the teacher ID as the unique dictionary key.
        self.teachers[teacher.teacher_id] = teacher






    def enroll_student(self, student_id, course_code):
        """Enroll a student in a course."""

        # Check that the student exists
        if student_id not in self.students:
            raise ValueError(
                f"Student {student_id} does not exist."
            )

        # Check that the course exists
        if course_code not in self.courses:
            raise ValueError(
                f"Course {course_code} does not exist."
            )

        student = self.students[student_id]
        course = self.courses[course_code]

        # Prevent duplicate enrollment
        if course_code in student.enrolled_courses:
            raise ValueError(
                f"Student {student_id} is already enrolled in {course_code}."
            )

        # Update the student's enrolled courses
        student.enroll_course(course_code)

        # Update the course's enrolled students
        course.add_student(student_id)



    def drop_course(self, student_id, course_code):
        """Remove a student from a course."""

        # Check that the student exists.
        if student_id not in self.students:
            raise ValueError(
                f"Student {student_id} does not exist."
            )

        # Check that the course exists.
        if course_code not in self.courses:
            raise ValueError(
                f"Course {course_code} does not exist."
            )

        student = self.students[student_id]
        course = self.courses[course_code]

        # Check that the student is actually enrolled.
        if course_code not in student.enrolled_courses:
            raise ValueError(
                f"Student {student_id} is not enrolled in {course_code}."
            )

        # Remove the course from the student.
        student.drop_course(course_code)

        # Remove the student from the course.
        course.remove_student(student_id)




    def display_students(self):
        """Display all students in the school."""

        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            student.display_info()
            print("-" * 40)



    def display_courses(self):
        """Display all courses in the school."""

        if not self.courses:
            print("No courses found.")
            return

        for course in self.courses.values():
            course.display_info()
            print("-" * 40)


    def display_teachers(self):
        """Display all teachers in the school."""

        if not self.teachers:
            print("No teachers found.")
            return

        for teacher in self.teachers.values():
            teacher.display_info()
            print("-" * 40)