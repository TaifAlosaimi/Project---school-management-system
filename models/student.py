class Student:
    """Represent a student in the school management system"""

    def __init__(self, student_id, name, age):
        # Store the student's basic information
        self.student_id = student_id
        self.name = name
        self.age = age
        self.enrolled_courses = []
        # Start with an empty list because the student may have no enrolled courses when the object is created.



    def enroll_course(self, course_code):
        """Enroll the student in a course"""
        # Prevent the same course from being added more than once
        if course_code not in self.enrolled_courses:
            self.enrolled_courses.append(course_code)

  
    def drop_course(self, course_code):
        """Remove the student from a course"""
        # Remove the course only if the student is currently enrolled.
        if course_code in self.enrolled_courses:
            self.enrolled_courses.remove(course_code)


    def display_info(self):
        """Display the student's information"""

        # Display the stored information
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Enrolled Courses: {self.enrolled_courses}")