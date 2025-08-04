# Overview

As a software developer, my goal in this project was to advance my skills in integrating SQL relational databases and Python applications. The software I developed is a console-type Student Records Management System that interacts with a SQLite database to keep and process student information and their grades. The users can perform basic database operations such as record insertion, updating, deletion, and querying through dynamically generated SQL statements in Python.

The application features an interactive menu-driven interface offering CRUD (Create, Read, Update, Delete) operations on students and grades, JOIN queries to display composite student-grade information, and statistical summaries like average and top grades and pass/fail status.

The project enables me to get hands-on practice with database interaction and data management in real life using Python and prepares me for larger software

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

This project uses SQLite, which is a file-based, lightweight relational database engine that does not require an external server. SQLite is a good choice for embedding in programs and for studying database concepts.

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

- Make input validation and error checking more robust
- Add the feature to search students by name
- Support multiple grades per student and calculate GPA
- Develop a graphical user interface (GUI) for simplicity of use
- Incorporate data export features, such as CSV or PDF reports