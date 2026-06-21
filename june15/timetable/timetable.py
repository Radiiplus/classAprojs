import exam

CMDS = {"back", "b", "menu", "m"}


class back(Exception):
    pass


def backish(value):
    if value.lower() in CMDS:
        raise back


def menu():
    print("\nWelcome to Orbit Exam Timetable!")
    print("1. Add Course")
    print("2. Register Students")
    print("3. Generate Timetable")
    print("4. View Timetable")
    print("5. Detect Conflicts")
    print("6. View Courses")
    print("7. View Students")
    print("8. Exit")


def menchoice(prompt, min_val, max_val):
    while True:
        choice = input(prompt)

        if not choice.isdigit():
            print("Enter numbers only")
            continue

        choice = int(choice)

        if choice < min_val or choice > max_val:
            print("Invalid choice range")
            continue

        return choice


def textval(prompt):
    while True:
        text = input(prompt).strip()
        backish(text)

        if not text:
            print("Input cannot be empty")
            continue

        return text


def courseval(prompt):
    while True:
        text = input(prompt).strip()
        backish(text)

        if not text:
            print("Input cannot be empty")
            continue

        courses = []

        for course in text.split(","):
            course = course.strip().upper()

            if course:
                courses.append(course)

        if not courses:
            print("Enter at least one course")
            continue

        return courses


def addcourseval():
    course = textval("Enter course code (back for menu): ")
    print(exam.addcourse(course))


def registerval():
    student = textval("Enter student name (back for menu): ")
    selected = courseval("Enter courses separated by comma (back for menu): ")
    print(exam.register(student, selected))


while True:
    menu()

    try:
        choice = menchoice("Enter your choice: ", 1, 8)

        if choice == 1:
            addcourseval()

        elif choice == 2:
            registerval()

        elif choice == 3:
            print(exam.generate())

        elif choice == 4:
            print(exam.viewtimetable())

        elif choice == 5:
            print(exam.viewconflicts())

        elif choice == 6:
            print(exam.viewcourses())

        elif choice == 7:
            print(exam.viewstudents())

        elif choice == 8:
            print("Thank you for using Orbit Exam Timetable!")
            break

    except back:
        continue

    except Exception as e:
        print("Unexpected error:", e)
