CREATE DATABASE AttendanceTracker;
USe AttendanceTracker;

Create Table students
(Student_ID INT NOT NULL, 
 Student_First_name varchar(20),
 Student_last_name varchar(20),
 CONSTRAINT students_pk PRIMARY KEY (student_ID));

CREATE TABLE courses 
   (CRN INT NOT NULL,
    start_end_time varchar(20),
    course_name varchar(20),
    CONSTRAINT courses_pk PRIMARY KEY (CRN));

CREATE TABLE attendance
	( CRN INT NOT NULL, 
	Student_id INT NOT NULL, 
Date_of_attendance DATE NOT NULL,
Attended varchar(10), 
CONSTRAINT attendance_pk PRIMARY KEY (CRN, Student_ID, Date_of_attendance), 
CONSTRAINT attendance_fk1 FOREIGN KEY (CRN) REFERENCES courses(CRN), 
CONSTRAINT attendance_fk2 FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID));
