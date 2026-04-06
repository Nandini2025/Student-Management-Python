import csv
import os

# Configuration
FILE_NAME = 'students.csv'
FIELDS = ['Roll No', 'Name', 'Course', 'Marks']

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)

def add_student():
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course (e.g., BCA): ")
    marks = input("Enter Marks: ")
    
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, course, marks])
    print("✔ Record added successfully!")

def view_students():
    print("\n--- Student List ---")
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            records = list(reader)
            if not records:
                print("No records found.")
            else:
                print(f"{'Roll':<10} {'Name':<20} {'Course':<10} {'Marks':<10}")
                print("-" * 50)
                for row in records:
                    print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10} {row[3]:<10}")
    except FileNotFoundError:
        print("No database found. Add a student first!")

def search_student():
    roll_to_find = input("\nEnter Roll Number to search: ")
    found = False
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll_to_find:
                print(f"\n✔ Found: Name: {row[1]}, Course: {row[2]}, Marks: {row[3]}")
                found = True
                break
    if not found:
        print("❌ Student not found.")

def delete_student():
    roll_to_delete = input("\nEnter Roll Number to delete: ")
    temp_data = []
    found = False
    
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        temp_data.append(header)
        for row in reader:
            if row[0] != roll_to_delete:
                temp_data.append(row)
            else:
                found = True
                
    if found:
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(temp_data)
        print("✔ Record deleted successfully!")
    else:
        print("❌ No such record exists.")

def main():
    initialize_file()
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1': add_student()
        elif choice == '2': view_students()
        elif choice == '3': search_student()
        elif choice == '4': delete_student()
        elif choice == '5': 
            print("Exiting... Good luck with your internship applications!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()