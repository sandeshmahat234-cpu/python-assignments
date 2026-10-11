students = [
    {"name": "Asha", "marks": {"Math": 85, "Science": 78, "English": 90}},
    {"name": "Bikash", "marks": {"Math": 62, "Science": 70, "English": 58}},
    {"name": "Sita", "marks": {"Math": 91, "Science": 88, "English": 94}},
    {"name": "Ram", "marks": {"Math": 45, "Science": None, "English": 60}},
    {"name": "Maya", "marks": {"Math": 73, "Science": 80}},
]

SUBJECTS = ["Math", "Science", "English"]


def calculate_total(marks):
    # Missing marks (None or not entered) count as 0
    return sum(marks.get(subject) or 0 for subject in SUBJECTS)


def calculate_percentage(total):
    return (total / (len(SUBJECTS) * 100)) * 100


def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    raise LookupError(f"Student '{name}' does not exist.")


def main():
    name = input("Enter a student name: ").strip()

    try:
        student = find_student(name)
    except LookupError as error:
        print(error)
        return

    marks = student["marks"]

    for subject in SUBJECTS:
        if marks.get(subject) is None:
            print(f"Warning: {subject} mark is missing and counted as 0.")

    total = calculate_total(marks)
    percentage = calculate_percentage(total)

    print(f"\nStudent: {student['name']}")
    print(f"Total marks: {total} out of {len(SUBJECTS) * 100}")
    print(f"Percentage: {percentage:.2f}%")


