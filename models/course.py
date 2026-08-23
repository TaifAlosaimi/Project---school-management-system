class Course:
    """Represent a course in the school management system"""

    def __init__(self, course_code, course_title, assigned_teacher=None):
        # Store the course's basic information.
        self.course_code = course_code
        self.course_title = course_title
        self.assigned_teacher = assigned_teacher

        # Keep track of students enrolled in this course
        self.enrolled_student_ids = []


    def add_student(self, student_id):
        """Add a student to the course"""

        # Prevent duplicate enrollment in the same course
        if student_id not in self.enrolled_student_ids:
            self.enrolled_student_ids.append(student_id)


    def remove_student(self, student_id):
        """Remove a student from the course"""

        # Remove the student only if they are enrolled.
        if student_id in self.enrolled_student_ids:
            self.enrolled_student_ids.remove(student_id)

    def display_info(self):
        """Display the course's information."""

        # Display the course details in a readable format.
        print(f"Course Code: {self.course_code}")
        print(f"Course Title: {self.course_title}")
        print(f"Assigned Teacher: {self.assigned_teacher}")
        print(f"Enrolled Students: {self.enrolled_student_ids}")




