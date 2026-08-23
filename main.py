from models.school import School
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from utils.file_handler import load_json, save_json


# ==========================
# Create School Object
# ==========================

school = School()


print("School Management System")
print("-" * 40)


# ==========================
# Load Data From JSON Files
# ==========================

students_data = load_json("students.json")
teachers_data = load_json("teachers.json")
courses_data = load_json("courses.json")


# ==========================
# Convert Students Data
# ==========================

for student_data in students_data:

    student = Student(
        student_data["student_id"],
        student_data["name"],
        student_data["age"]
    )

    student.enrolled_courses = student_data.get(
        "enrolled_courses",
        []
    )

    school.add_student(student)


print("Students loaded successfully!")


# ==========================
# Convert Teachers Data
# ==========================

for teacher_data in teachers_data:

    teacher = Teacher(
        teacher_data["teacher_id"],
        teacher_data["name"],
        teacher_data["subject"]
    )

    school.add_teacher(teacher)


print("Teachers loaded successfully!")


# ==========================
# Convert Courses Data
# ==========================

for course_data in courses_data:

    course = Course(
        course_data["course_code"],
        course_data["course_title"],
        course_data.get("assigned_teacher")
    )

    course.enrolled_student_ids = course_data.get(
        "enrolled_student_ids",
        []
    )

    school.add_course(course)


print("Courses loaded successfully!")


# ==========================
# Main Menu
# ==========================

while True:

    print("\nSCHOOL MANAGEMENT SYSTEM")
    print("-" * 40)

    print("1. Add student")
    print("2. Add course")
    print("3. Enroll student")
    print("4. View students")
    print("5. View courses")
    print("6. Save and Exit")


    choice = input(
        "Choose an option: "
    ).strip()


    # Add Student
    if choice == "1":

        try:

            student_id = input(
                "Enter student ID: "
            ).strip()

            name = input(
                "Enter student name: "
            ).strip()

            age = int(
                input("Enter student age: ")
            )


            student = Student(
                student_id,
                name,
                age
            )


            school.add_student(student)


            print(
                "Student added successfully!"
            )


        except Exception as error:

            print(
                "Error:",
                error
            )


    # Add Course
    elif choice == "2":

        try:

            course_code = input(
                "Enter course code: "
            ).strip()

            course_title = input(
                "Enter course title: "
            ).strip()

            assigned_teacher = input(
                "Enter assigned teacher ID: "
            ).strip()


            course = Course(
                course_code,
                course_title,
                assigned_teacher
            )


            school.add_course(course)


            print(
                "Course added successfully!"
            )


        except Exception as error:

            print(
                "Error:",
                error
            )


    # Enroll Student
    elif choice == "3":

        try:

            student_id = input(
                "Enter student ID: "
            ).strip()

            course_code = input(
                "Enter course code: "
            ).strip()


            school.enroll_student(
                student_id,
                course_code
            )


            print(
                "Student enrolled successfully!"
            )


        except Exception as error:

            print(
                "Error:",
                error
            )


    # View Students
    elif choice == "4":

        school.display_students()


    # View Courses
    elif choice == "5":

        school.display_courses()


    # Save And Exit
    elif choice == "6":

        students_data = []

        for student in school.students.values():

            students_data.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "enrolled_courses": student.enrolled_courses
            })


        save_json(
            "students.json",
            students_data
        )


        courses_data = []

        for course in school.courses.values():

            courses_data.append({
                "course_code": course.course_code,
                "course_title": course.course_title,
                "assigned_teacher": course.assigned_teacher,
                "enrolled_student_ids": course.enrolled_student_ids
            })


        save_json(
            "courses.json",
            courses_data
        )


        teachers_data = []

        for teacher in school.teachers.values():

            teachers_data.append({
                "teacher_id": teacher.teacher_id,
                "name": teacher.name,
                "subject": teacher.subject
            })


        save_json(
            "teachers.json",
            teachers_data
        )


        print("Data saved successfully!")
        print("Thank You!")

        break


    else:

        print(
            "Invalid choice. Please try again."
        )