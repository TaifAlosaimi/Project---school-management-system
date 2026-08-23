class Teacher:
    """Represent a teacher in the school management system"""

    def __init__(self, teacher_id, name, subject):
        # Store the teacher s basic information
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display_info(self):
        """Display the teacher's information"""

        # Display the teacher details 
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")