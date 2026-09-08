CREATE DATABASE school_assignment;

\c school_assignment

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age > 0),
    grade INT DEFAULT 1,
    city VARCHAR(50),
    marks INT
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(50) UNIQUE NOT NULL,
    teacher VARCHAR(50),
    max_seats INT
);

CREATE TABLE enrollments (
    student_id INT REFERENCES students(id),
    course_id INT REFERENCES courses(id),
    score INT,
    PRIMARY KEY (student_id, course_id)
);

INSERT INTO students (name, age, grade, city, marks) VALUES
('Aisha', 10, 5, 'Hyderabad', 92),
('Ravi', 11, 6, 'Chennai', 78),
('Meera', 10, 5, 'Hyderabad', 92),
('Arjun', 12, 7, 'Mumbai', 65),
('Sara', 11, 6, 'Delhi', NULL),
('Kabir', 12, 7, 'Chennai', 88),
('Zoya', 10, 5, 'Delhi', 71),
('Dev', 13, 8, 'Mumbai', 55);

INSERT INTO courses (course_name, teacher, max_seats) VALUES
('Math', 'Ms. Rao', 30),
('Science', 'Mr. Khan', 25),
('Art', 'Ms. Iyer', 15),
('Music', 'Mr. Das', 20),
('Robotics', 'Ms. Rao', 10);

INSERT INTO enrollments (student_id, course_id, score) VALUES
(1, 1, 95),
(1, 2, 88),
(1, 3, 90),
(2, 1, 70),
(2, 4, 85),
(3, 2, 93),
(3, 3, 80),
(4, 1, 60),
(4, 4, 72),
(5, 3, NULL),
(6, 1, 90),
(6, 2, 84),
(6, 4, 79),
(7, 3, 74);


-- PART - 1

-- 1.1	Show every column of every student.	
SELECT * FROM students;

-- 1.2 Show name and city of students older than 10
SELECT name, city FROM students
WHERE age > 10;

-- 1.3 Using OR: Grade 5 or Grade 7 
SELECT * FROM students
WHERE grade = 5 OR grade = 7
ORDER BY name ASC;

-- 1.4 Students whose name starts with A 
SELECT * FROM students
WHERE name LIKE 'A%';

-- 1.5 Correct: Find students with missing marks 
SELECT * FROM students
WHERE marks IS NULL;

-- 1.6 Correct: Put NULL values last
SELECT * FROM students
ORDER BY marks DESC NULLS LAST
LIMIT 3;

-- 1.7 Show distinct cities 
SELECT DISTINCT city
FROM students;

-- 1.8 Insert Priya
INSERT INTO students (name, age, grade, city, marks)
VALUES ('Priya', 11, 6, 'Pune', 81);

-- 1.8 Count after INSERT
SELECT COUNT(*)
FROM students;

-- 1.8 Update Priya marks
UPDATE students
SET marks = 85
WHERE name = 'Priya';

-- 1.8 Count after UPDAT
SELECT COUNT(*)
FROM students;

-- 1.8 Delete Priya
DELETE FROM students
WHERE name = 'Priya';

-- Count after DELETE
SELECT COUNT(*)
FROM students;

-- PART - 2

-- 2.1 Add a new column email VARCHAR(100) to the students table.
ALTER TABLE students
ADD column email VARCHAR(100);

-- 2.2 Rename the email column to email_id.
ALTER TABLE students
RENAME COLUMN email TO email_id;

-- 2.3 Try to insert a student with no name
 -- Answer:- error is NOT NULL constraint on column

 -- 2.4 Try to insert a student with age -3
 -- Answer: CHECK constraint on the age column. that is age should be greater than 0

 -- 2.5 Try to enroll student 99 in course 1. INSERT INTO enrollments VALUES (99, 1, 50);	
-- Question: Which constraint stopped you, and why is this rule useful?
-- Answer: error is foreign key constraint on student_id.

-- 2.6 Remove the email_id column.
ALTER TABLE students
DROP COLUMN email_id;

----- PART - 3 

 -- 3.1 Students count and their Average 
SELECT COUNT(*) AS total_students,
AVG(age) AS average_age
FROM students;

-- 3.2 Highest and Lowest marks in Class?
SELECT MAX(marks) AS highest_marks,
MIN(marks) AS lowest_marks
FROM students;

-- 3.3 Run COUNT(*) and COUNT(marks).
-- Explain why the two numbers are different?.
--  Answer: COUNT(*) counts all rows, while COUNT(marks) count only not null values

-- 3.4 Count how many students are in each grade. Sort by grade.
SELECT grade, COUNT(*) AS student_count
FROM students
GROUP BY grade
ORDER BY grade;

-- 3.5 Show the average marks per city, rounded to 1 decimal. Highest city average first.

SELECT city, ROUND(AVG(marks), 1) AS average_marks
FROM students
GROUP BY city
ORDER BY average_marks DESC;

-- 3.6 Show only cities whose average marks are above 75.
SELECT city, AVG(marks) AS average_marks
FROM students
GROUP BY city
HAVING AVG(marks) > 75;

-- 3.7 Show grades that have at least 2 students.
SELECT grade, COUNT(*) AS student_count 
FROM students
GROUP BY grade
HAVING COUNT(*) >= 2
ORDER BY grade;

-- 3.8 Count students in each course_id
SELECT course_id, COUNT(*) AS student_count
FROM enrollments
GROUP BY course_id;

--3.9 — Highest score in each course_id
SELECT course_id, MAX(score) AS highest_score
FROM enrollments
GROUP BY course_id;

-- 3.10 Number of students and number who have marks per city

SELECT city, COUNT(*) AS total_students,
COUNT(marks) AS students_with_marks
FROM students
GROUP BY city;

------ Part - 4

-- 4.1 — Every enrollment with student name, course name, score

SELECT s.name AS student_name, c.course_name, e.score
FROM enrollments e
INNER JOIN students s
ON e.student_id = s.id
INNER JOIN courses c
ON e.course_id = c.id;

-- 4.2 — All students with their course names

SELECT s.name AS student_name, c.course_name
FROM students s
LEFT JOIN enrollments e
ON s.id = e.student_id
LEFT JOIN courses c
ON e.course_id = c.id;


-- 4.3 Find students not enrolled in any course
SELECT s.name FROM students s
LEFT JOIN enrollments e
ON s.id = e.student_id
WHERE e.student_id IS NULL;

-- 4.4 — Every course with number of students

SELECT c.course_name, COUNT(*) AS student_count
FROM courses c
LEFT JOIN enrollments e
ON c.id = e.course_id
GROUP BY c.course_name;    -- The problem is Robotics has no matching enrollment

-- 4.4  COUNT(e.student_id)
SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM courses c
LEFT JOIN enrollments e
ON c.id = e.course_id
GROUP BY c.course_name;  it shows expected results

-- 4.5 — Number of courses each student takes

SELECT s.name, COUNT(e.course_id) AS courses
FROM students s
LEFT JOIN enrollments e
ON s.id = e.student_id
GROUP BY s.id, s.name
ORDER BY course_count DESC, s.name ASC;


-- 4.6 Enrollments with score >= 85

SELECT s.name, c.course_name, e.score
FROM enrollments e
JOIN students s
ON e.student_id = s.id
JOIN courses c
ON e.course_id = c.id
WHERE e.score >= 85
ORDER BY e.score DESC;

-- 4.7 Average score per course, rounded to 1 decimal

SELECT c.course_name, ROUND(AVG(e.score), 1) AS average_score
FROM courses c
JOIN enrollments e
ON c.id = e.course_id
GROUP BY c.id, c.course_name
ORDER BY average_score DESC;

-- 4.8 Courses taught by Ms. Rao with number of students

SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
ON c.id = e.course_id
WHERE c.teacher = 'Ms. Rao'
GROUP BY c.course_name;

-- 4.9 Self join: pairs of students from the same city

SELECT a.name AS student1, b.name AS student2, a.city
FROM students a
JOIN students b
ON a.city = b.city
AND a.id < b.id;

-- 4.10 CROSS JOIN
SELECT * FROM students
CROSS JOIN courses;


-- Part 5

-- 5.1 Students whose marks are above the class average
SELECT name, marks
FROM students
WHERE marks > (SELECT AVG(marks)FROM students );

-- 5.2 Student(s) with the highest marks

SELECT name, marks
FROM students
WHERE marks = (SELECT MAX(marks) FROM students);


-- 5.3	—	Students enrolled in Art (subquery with IN,	no JOIN)
SELECT name FROM students
WHERE id IN (
    SELECT student_id FROM enrollments
    WHERE course_id = (
        SELECT id
        FROM courses
        WHERE course_name = 'Art'
    )
);

-- 5.4 Students not enrolled in Math
SELECT name FROM students
WHERE id NOT IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT id
        FROM courses
        WHERE course_name = 'Math'
    )
);

-- 5.5	—	Courses	with no	students (NOT EXISTS)
SELECT course_name
FROM courses c
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.id
);

-- 5.6 Correlated subquery the	highest	marks in their own grade

SELECT name, grade, marks
FROM students s
WHERE marks = (
    SELECT MAX(marks)
    FROM students
    WHERE grade = s.grade
);

-- 5.7 Subquery in FROM Build a table of highest average from it

SELECT course_name, avg_score
FROM (
    SELECT c.course_name,
           AVG(e.score) AS avg_score
    FROM courses c
    JOIN enrollments e
        ON c.id = e.course_id
    GROUP BY c.course_name
) AS course_averages
ORDER BY avg_score DESC
LIMIT 1;


 -- 5.8 UPDATE with a subquery + transaction: Inside BEGIN; ... ROLLBACK; give +5 score to every enrollment in the
-- course taught by Mr. Das. Check the scores after the UPDATE, then after the ROLLBACK. How many rows changed, and did
-- the change survive?

BEGIN;
UPDATE enrollments
SET score = score + 5
WHERE course_id = (SELECT id FROM courses WHERE teacher = 'Mr. Das');
SELECT * FROM enrollments
WHERE course_id = (SELECT id FROM courses WHERE teacher = 'Mr. Das');
ROLLBACK;
SELECT * FROM enrollments
WHERE course_id = (SELECT id FROM courses WHERE teacher = 'Mr. Das');


-- Part - 6

-- 6.1 Student name and marks label marks >= 85 -> 'Excellent', >= 70 -> 'Good', otherwise -> 'Needs practice'. Students
-- with no marks must show 'No marks'.

SELECT name,
       CASE
           WHEN marks IS NULL THEN 'No marks'
           WHEN marks >= 85 THEN 'Excellent'
           WHEN marks > 70 THEN 'Good'
           ELSE 'Needs practice'
       END AS label
FROM students;

-- 6.2	Show each name in UPPER	CASE along	with the length	of the name.	
SELECT	UPPER(name), LENGTH(name)
FROM students;

-- 6.3 Produce one sentence per student like: Aisha from Hyderabad is 10 years old.
SELECT name || ' from ' || city || ' is ' || age || ' years old.' AS sentence
FROM students;

-- 6.4 Create a VIEW called top_scorers that shows (expected rows: 6) name, course_name, score for scores >= 85. 
-- Select from it, then drop it

CREATE VIEW top_scorers AS
SELECT s.name, c.course_name, e.score
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
WHERE e.score >= 85;
SELECT * FROM top_scorers;
DROP VIEW top_scorers;