import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/demodb.db")

def create_table():
    con.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, major string)")
    con.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, name TEXT, major string, year INTEGER)")
    con.execute("DROP TABLE students_on_courses")
    con.execute("CREATE TABLE students_on_courses (student_id INTEGER, course_id INTEGER, "
                 "FOREIGN KEY (student_id) REFERENCES students(id), "
                 "FOREIGN KEY (course_id) REFERENCES courses(id))")

if __name__ == "__main__":
    # create_table()
    con.execute("INSERT INTO students (name, major) VALUES ('Serg',	    'DS')")
    con.execute("INSERT INTO students (name, major) VALUES ('Drake',	'CS')")
    con.execute("INSERT INTO students (name, major) VALUES ('Jess',	    'CS')")
    con.execute("INSERT INTO students (name, major) VALUES ('Jake',	    'DS')")

    # insert course
    con.execute("INSERT INTO courses (name, major, year) VALUES ('PY1', 'CS', 2024)")
    con.execute("INSERT INTO courses (name, major, year) VALUES ('PY2', 'CS', 2024)")
    con.execute("INSERT INTO courses (name, major, year) VALUES ('PY3', 'CS', 2025)")
    con.execute("INSERT INTO courses (name, major, year) VALUES ('Data visuals', 'DS', 2025)")
    con.execute("INSERT INTO courses (name, major, year) VALUES ('Intro ML', 'DS', 2024)")
    con.execute("INSERT INTO courses (name, major, year) VALUES ('PY1', 'CS', 2023)")

    con.commit()
