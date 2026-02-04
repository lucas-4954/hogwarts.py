STUDENTS = ["Harry", "Ron", "Hermione"]


def main():
    if not STUDENTS:
        print("No students found.")
        return

    for student in STUDENTS:
        print(student)


if __name__ == "__main__":
    main()
