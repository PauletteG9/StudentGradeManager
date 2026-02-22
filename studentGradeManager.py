import csv
import os

FILENAME = "students.csv"


def load_students():
    students = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                marks = list(map(float, row[1:]))
                students[name] = marks
    return students


def save_students(students):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for name, marks in students.items():
            writer.writerow([name] + marks)


def add_student(students):
    name = input("Enter student name: ")
    marks = list(map(float, input("Enter marks separated by space: ").split()))
    students[name] = marks
    print("Student added successfully!")


def calculate_average(students):
    if not students:
        print("No data available.")
        return

    total = 0
    count = 0
    for marks in students.values():
        total += sum(marks)
        count += len(marks)

    print("Class Average:", round(total / count, 2))


def find_topper(students):
    if not students:
        print("No data available.")
        return

    topper = max(students, key=lambda name: sum(students[name]) / len(students[name]))
    avg = sum(students[topper]) / len(students[topper])
    print(f"Topper: {topper} with average {round(avg,2)}")


def search_student(students):
    name = input("Enter student name to search: ")
    if name in students:
        print("Marks:", students[name])
        print("Average:", round(sum(students[name]) / len(students[name]), 2))
    else:
        print("Student not found.")


def menu():
    students = load_students()

    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add Student")
        print("2. Calculate Class Average")
        print("3. Find Topper")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
            save_students(students)

        elif choice == "2":
            calculate_average(students)

        elif choice == "3":
            find_topper(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            save_students(students)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()