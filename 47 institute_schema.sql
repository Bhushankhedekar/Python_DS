create database institute_db;

use institute_db;
SELECT * FROM institute_db.courses;
SELECT * FROM institute_db.student_admission;
SELECT * FROM institute_db.student_marks;

SELECT student_admission.student_id, name, city, test1_marks, test2_marks 
FROM student_admission
INNER JOIN student_marks 
ON student_admission.student_id = student_marks.student_id;   

SELECT student_admission.student_id, name, city, test1_marks, test2_marks 
FROM student_admission
LEFT JOIN student_marks 
ON student_admission.student_id = student_marks.student_id;  

SELECT student_admission.student_id, name, city, test1_marks, test2_marks 
FROM student_admission
RIGHT JOIN student_marks 
ON student_admission.student_id = student_marks.student_id;  
  