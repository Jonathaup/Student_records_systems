import sqlite3

def create_database():
    """
    Creates the SQLite database and tables if they do not exist.
    - students table stores student names.
    - grades table stores grades linked to students by student_id.
    """
    conn = sqlite3.connect("students.db")  # Connect to SQLite database file (creates if not exists)
    cursor = conn.cursor()

    # Create the students table with columns: id (auto-increment primary key), name (text, required)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create the grades table with columns: id (auto-increment primary key),
    # student_id (foreign key to students.id), and grade (real number)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            grade REAL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')

    conn.commit()  # Save changes to database
    conn.close()   # Close the connection

def add_student():
    """
    Adds a new student and their grade.
    Gives user the option to continue or return to the main menu.
    """
    print("\n--- Add Student and Grade ---")
    print("1. Continue")
    print("2. Return to Main Menu")
    choice = input("Select an option: ")
    if choice != "1":  # If user does not want to continue, return to menu
        return

    name = input("Enter student name: ")
    try:
        grade = float(input("Enter grade Number: "))  # Convert input to float
    except ValueError:
        print("Invalid grade, Needs to be a Number.")  # Handle invalid input
        return

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    try:
        # Insert new student into the students table
        cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
        student_id = cursor.lastrowid  # Get the newly created student's ID

        # Insert the student's grade linked by student_id
        cursor.execute("INSERT INTO grades (student_id, grade) VALUES (?, ?)", (student_id, grade))
        conn.commit()
        print("Student and grade added successfully.")
    except Exception as e:
        print("Error inserting student and grade:", e)
    finally:
        conn.close()

def update_grade():
    """
    Updates the grade of an existing student.
    Gives user option to continue or return to the main menu.
    """
    print("\n--- Update Grade ---")
    print("1. Continue")
    print("2. Return to Main Menu")
    choice = input("Select an option: ")
    if choice != "1":
        return

    try:
        student_id = int(input("Enter student ID: "))  # ID must be integer
        new_grade = float(input("Enter new grade Number: "))  # New grade as float
    except ValueError:
        print("Invalid input, Needs to be a Number.")  # Handle invalid input
        return

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    # Update the grade for the given student_id
    cursor.execute("UPDATE grades SET grade = ? WHERE student_id = ?", (new_grade, student_id))
    conn.commit()
    conn.close()
    print("Grade updated.")

def delete_student():
    """
    Deletes a student and their related grades.
    Gives user option to continue or return to the main menu.
    Asks for confirmation before deleting.
    """
    print("\n--- Delete Student ---")
    print("1. Continue")
    print("2. Return to Main Menu")
    choice = input("Select an option: ")
    if choice != "1":
        return

    try:
        student_id = int(input("Enter student ID to delete: "))  # Student ID to delete
    except ValueError:
        print("Invalid ID.")
        return

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # Get student name by ID
    cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
    result = cursor.fetchone()

    if result is None:
        print(f"No student found with ID {student_id}.")
        conn.close()
        return

    student_name = result[0]

    # Ask for confirmation with student name
    confirm = input(f"Are you sure you want to delete student named '{student_name}'? (y/n): ").lower()
    if confirm != 'y':
        print("Deletion canceled.")
        conn.close()
        return

    # Delete grades associated with the student first
    cursor.execute("DELETE FROM grades WHERE student_id = ?", (student_id,))
    # Delete the student record
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print(f"Student '{student_name}' deleted.")


def list_students_and_grades():
    """
    Lists all students and their grades.
    Uses a LEFT JOIN to include students even if they have no grades.
    """
    print("\n--- List of Students and Grades ---")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    # LEFT JOIN ensures all students appear, even those without grades
    cursor.execute('''
        SELECT students.id, students.name, grades.grade
        FROM students
        LEFT JOIN grades ON students.id = grades.student_id
    ''')

    rows = cursor.fetchall()  # Fetch all results
    if rows:
        for row in rows:
            grade_display = row[2] if row[2] is not None else "No grade"  # Handle students with no grades
            print(f"ID: {row[0]} | Name: {row[1]} | Course Grade: {grade_display}")
    else:
        print("No records found.")
    conn.close()

def show_statistics():
    """
    Shows statistics: average and highest grade for each student.
    Assigns a letter grade based on average and indicates pass/fail status.
    """
    print("\n--- Grade Statistics ---")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    # Aggregate functions AVG and MAX to compute average and highest grades per student
    cursor.execute('''
        SELECT students.name,
               AVG(grades.grade) AS average_grade,
               MAX(grades.grade) AS highest_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        GROUP BY students.id
    ''')

    rows = cursor.fetchall()
    if rows:
        for row in rows:
            name = row[0]
            avg = row[1]
            max_grade = row[2]

            # Assign letter grade based on average score
            if avg >= 90:
                letter = "A"
            elif avg >= 80:
                letter = "B"
            elif avg >= 70:
                letter = "C"
            elif avg >= 60:
                letter = "D"
            else:
                letter = "F"

            # Determine pass/fail based on letter grade
            status = "Pass" if letter != "F" else "Fail"

            print(f"Name: {name} | Average: {avg:.2f} | Max: {max_grade} | Letter: {letter} | Status: {status}")
    else:
        print("No statistics available.")
    conn.close()

def menu():
    """
    Main menu loop.
    Creates database on startup and allows the user to select options.
    """
    create_database()  # Ensure database and tables exist

    while True:
        # Display menu options
        print("\n=== Student Records Menu ===")
        print("1. Add student and grade")
        print("2. Update grade")
        print("3. Delete student")
        print("4. List students and grades")
        print("5. Show statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # Call appropriate function based on user input
        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            list_students_and_grades()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()  # Start the program by calling menu
