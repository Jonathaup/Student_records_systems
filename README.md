# Overview

As a software engineer, my goal with this project was to deepen my understanding of integrating SQL relational databases with Python applications. The software I developed is a console-based Student Records Management System that interacts with a SQLite database to manage student information and their grades. Users can perform essential database operations such as inserting, updating, deleting, and querying records through dynamically generated SQL commands in Python.

The program features an interactive menu-driven interface that supports CRUD (Create, Read, Update, Delete) operations on students and their grades, performs JOIN queries to display combined student-grade information, and calculates statistical summaries including average and highest grades along with pass/fail status.

This project helps me practice real-world database interaction and data management using Python, preparing me for more complex software development challenges involving databases.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

This project uses SQLite, a lightweight, file-based relational database engine that does not require a separate server. SQLite is ideal for embedding within applications and for learning database concepts.

The database contains two main tables:

- **students**: stores student records with fields:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT): unique identifier for each student
  - `name` (TEXT NOT NULL): the student's name

- **grades**: stores grade records associated with students, with fields:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT): unique identifier for each grade entry
  - `student_id` (INTEGER): foreign key linking to `students.id`
  - `grade` (REAL): numerical grade value

These tables are linked via a foreign key constraint, allowing JOIN operations to combine student and grade data effectively.

# Development Environment

The software was developed using:

- **Programming Language:** Python 3.x
- **Database Library:** `sqlite3` (Python's built-in SQLite interface)
- **Development Tools:** Any Python-supporting IDE or text editor (e.g., Visual Studio Code, PyCharm)
- **Execution:** Console-based application run from the command line or terminal

# Useful Websites

- [Oracle Database](https://www.oracle.com/database/)  
- [MySQL](https://www.mysql.com/)  
- [Microsoft SQL Server 2022](https://www.microsoft.com/en-us/sql-server/sql-server-2022)  
- [PostgreSQL](https://www.postgresql.org/)  
- [SQLite Official Site](https://www.sqlite.org/index.html)  
- [IBM Db2 Database](https://www.ibm.com/products/db2-database)  
- [Python sqlite3 Module Documentation](https://docs.python.org/3/library/sqlite3.html)  

# Future Work

- Improve input validation and error handling to increase robustness  
- Add functionality to search for students by name  
- Support multiple grades per student and implement GPA calculation  
- Develop a graphical user interface (GUI) for more user-friendly interaction  
- Implement data export features, such as CSV or PDF reports  
