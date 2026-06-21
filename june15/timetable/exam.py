courses = ["MTH101", "PHY101", "CSC101", "ENG101"]

students = {
    "Student A": ["MTH101", "PHY101"],
    "Student B": ["PHY101", "CSC101"],
    "Student C": ["CSC101", "ENG101"]
}

slots = [
    "Monday Morning",
    "Monday Afternoon",
    "Tuesday Morning",
    "Tuesday Afternoon"
]

timetable = {}


def clean(code):
    return code.strip().upper()


def addcourse(code):
    code = clean(code)

    if not code:
        return "Course cannot be empty"

    if code in courses:
        return "Course already exists"

    courses.append(code)
    return f"{code} added successfully"


def register(student, selected):
    student = student.strip()
    selected = [clean(course) for course in selected if clean(course)]

    if not student:
        return "Student name cannot be empty"

    if len(selected) < 1:
        return "Select at least one course"

    for course in selected:
        if course not in courses:
            return f"{course} does not exist"

    students[student] = selected
    return f"{student} registered successfully"


def detectconflicts():
    conflicts = []
    seen = set()

    for selected in students.values():
        for first in range(len(selected)):
            for second in range(first + 1, len(selected)):
                course1 = selected[first]
                course2 = selected[second]
                pair = tuple(sorted((course1, course2)))

                if pair not in seen:
                    seen.add(pair)
                    conflicts.append((course1, course2))

    return conflicts


def hasconflict(course, slotcourses, conflicts):
    for other in slotcourses:
        pair = tuple(sorted((course, other)))

        if pair in conflicts:
            return True

    return False


def generate():
    global timetable

    conflicts = set(detectconflicts())
    timetable = {slot: [] for slot in slots}

    for course in courses:
        placed = False

        for slot in slots:
            if not hasconflict(course, timetable[slot], conflicts):
                timetable[slot].append(course)
                placed = True
                break

        if not placed:
            return f"No available slot for {course}"

    return "Timetable generated successfully"


def viewcourses():
    if not courses:
        return "No courses yet"

    return "\n".join(courses)


def viewstudents():
    if not students:
        return "No students registered yet"

    rows = []

    for student, selected in students.items():
        rows.append(f"{student}: {', '.join(selected)}")

    return "\n".join(rows)


def viewconflicts():
    conflicts = detectconflicts()

    if not conflicts:
        return "No conflicts detected"

    rows = []

    for course1, course2 in conflicts:
        rows.append(f"{course1} <-> {course2}")

    return "\n".join(rows)


def viewtimetable():
    if not timetable:
        return "No timetable generated yet"

    rows = []

    for slot, scheduled in timetable.items():
        rows.append(slot)

        if scheduled:
            for course in scheduled:
                rows.append(course)
        else:
            rows.append("No exam")

        rows.append("")

    return "\n".join(rows).strip()
