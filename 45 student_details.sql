CREATE DATABASE student;
use student;
create table student(id int,name text,age int);
insert into student(id,name,age) values(1,"Radha",23);
insert into student values(2,"Krushna",24);
insert into student values(3,"Rani",22),(4,"Seeta",21),(5,"Ram",25);
select * from student;
/*-----------------------------------------------------------------------------------*/

show databases;
use batch_k_1319;
show tables;
desc student;
select * from student;

create database batch_k_1319;
show databases;
use batch_k_1319;
show tables;
create table student(id int,name text,age int);
show tables;
describe student;
desc student;
insert into student(id,name,age) values(1,"Radha",23);
select * from student;
insert into student values(2,"Krushna",24);
select * from student;
insert into student values(3,"Rani",22),(4,"Seeta",21),(5,"Ram",25);
select * from student;

/*-----------------------------------------------------------------------------------*/

show databases;
use batch_k_1319;
show tables;
desc student;
select * from student;

alter table student add city text;
alter table student drop location;
alter table student drop location;

create table student(id int,name text,age int);
INSERT INTO student (id, name, age, city) VALUES
(1, 'Aarav Sharma', 20, 'Mumbai'),
(2, 'Isha Verma', 21, 'Delhi'),
(3, 'Rohan Gupta', 19, 'Bangalore'),
(4, 'Sneha Patil', 22, 'Pune'),
(5, 'Aditya Singh', 20, 'Lucknow'),
(6, 'Neha Reddy', 23, 'Hyderabad'),
(7, 'Karan Mehta', 21, 'Ahmedabad'),
(8, 'Priya Nair', 22, 'Kochi'),
(9, 'Rahul Das', 20, 'Kolkata'),
(10, 'Ananya Iyer', 19, 'Chennai'),
(11, 'Vikram Joshi', 24, 'Nagpur'),
(12, 'Pooja Kapoor', 21, 'Chandigarh'),
(13, 'Siddharth Jain', 22, 'Jaipur'),
(14, 'Meera Kulkarni', 20, 'Pune'),
(15, 'Arjun Mishra', 23, 'Varanasi'),
(16, 'Kavya Shetty', 21, 'Mangalore'),
(17, 'Nikhil Bansal', 22, 'Delhi'),
(18, 'Divya Bhatt', 20, 'Surat'),
(19, 'Manish Yadav', 24, 'Patna'),
(20, 'Ritika Saxena', 19, 'Bhopal'),
(21, 'Harsh Vardhan', 23, 'Indore'),
(22, 'Tanvi Desai', 21, 'Mumbai'),
(23, 'Abhishek Roy', 22, 'Kolkata'),
(24, 'Simran Kaur', 20, 'Amritsar'),
(25, 'Deepak Choudhary', 24, 'Jodhpur'),
(26, 'Shreya Ghosh', 21, 'Durgapur'),
(27, 'Amit Tiwari', 23, 'Kanpur'),
(28, 'Nisha Agarwal', 22, 'Ranchi'),
(29, 'Yash Thakur', 20, 'Shimla'),
(30, 'Komal Pawar', 21, 'Nashik');

select * from student;

select min(age) from student;
select max(age) from student;

select count(id) from student;

select count(age)as "Total Student" from student;

select * from student;

SET SQL_SAFE_UPDATES = 0;  
 
update student set city="Pune";
update student set city="Mumbai" where id=15;
update student set city="Delhi" where id=10 and name="Ananya Iyer";
update student set city="Jodhpur" where id=17 or age=22;

delete from student where city="kochi";

select * from student where age>20;
select * from student where age>=20;
select * from student where age<20;
select * from student where age<=20;

select * from student where age != 20;
select * from student where age <> 20;

select * from student where age>20 and city = "pune";

select * from student where age!=20 or age!=21 or age !=22;

/*-----------------------------------------------------------------------------------*/

show databases;
use batch_k_1319;
show tables;
desc student;
select * from student;

select * from student where age between 20 and 23;

select * from student where age not between 20 and 23;

select * from student where age in(20,21,22);

select * from student where age not in (20,21,22);

select * from student where city in('mumbai','pune','delhi') and age between 21 and 23;

select * from student where name like 'a%';

select * from student where name like '%a';

select * from student where name like '_o_%';

select * from student where name like '_o%';

select * from student where city is null;

select * from student where city is not null;

select city from student;

select distinct city from student;

select * from student order by age;

select * from student order by age desc;

select * from student order by name;

select * from student order by name desc;

select * from student order by city;

select * from student order by city desc;

select count(city) from student;

select count(city) from student group by city;

select count(city) as 'total student', city from student group by city;

select count(city) as 'total student', city from student group by city having count(city)>=2;

select count(age) from student;

select * from student limit 5;

select * from student limit 5, 10;

select * from student order by age limit 5;

select * from student where age=(select min(age) from student);

select * from student where age=(select age where age<23);

select * from student where age=(select age where age<23 and city = 'Pune');

-- show 2nd Highest age in table
select max(age) from student;
select max(age) from student where age<(select max(age) from student);

-- show 2nd lowest age in table
select min(age) from student where age>(select min(age) from student);

-- show student record whose age is 2nd lowest age in table
select * from student where age=(select min(age) from student where age>(select min(age) from student));

-- show student record whose age is 2nd Highest age in table
select * from student where age=(select max(age) from student where age<(select max(age) from student));

/*-----------------------------------------------------------------------------------*/

show databases;
use batch_k_1319;
show tables;
desc student;
select * from student;

CREATE DATABASE employee;
use employee;
create table employee(id int,name text,profile text,email text,salary int,age int,experience int);
insert into employee values
(1,"rani","dev","rani@gmail.com",11000,43,27),
(2,"raj","test","raj@gmail.com",21000,33,17),
(3,"radha","test","radha@gmail.com",26000,38,21),
(4,"raj","dev","raj12@gmail.com",51000,32,12),
(5,"john","dev","john@gmail.com",51000,39,27);

select * from employee;

select * from employee where salary > 20000;

select * from employee where salary = 51000;

select * from employee where profile = "dev";

select * from employee where profile = "test";

select email from employee where salary<>51000; 
-- !=
SET SQL_SAFE_UPDATES = 0;  

update employee set salary = salary+10000 where experience = 20;

delete from employee where salary = 21000; 

update employee set salary = salary - 21000 where name = "john";

alter table employee add branch_location text;

select * from employee;

select sum(salary) from employee;

select max(salary) from employee where profile = 'test';

select avg(salary) from employee;

select avg (experience) from employee;

select name,experience from employee where salary = (select max(salary) from employee);

/*-----------------------------------------------------------------------------------*/

show databases;
use batch_k_1319;
show tables;

create table department2(id int primary key , name text);
create table employee2 (id int primary key, name text, age int, salary double, d_id int,foreign key(d_id) references department2(id));

INSERT INTO department (id, name) 
VALUES 
    (101, 'Human Resources'),
    (102, 'Finance'),
    (103, 'Marketing'),
    (104, 'Information Technology'),
    (105, 'Sales'),
    (106, 'Operations'),
    (107, 'Legal'),
    (108, 'Customer Service'),
    (109, 'Research and Development'),
    (110, 'Quality Assurance');


INSERT INTO employee2 (id, name, age, salary, d_id) VALUES
(1, 'James Smith', 30, 75000, 101),
(2, 'Mary Johnson', 28, 68000, 102),
(3, 'Robert Brown', 45, 95000, 103),
(4, 'Patricia Garcia', 32, 72000, 101),
(5, 'Michael Miller', 38, 88000, 104),
(6, 'Linda Davis', 26, 62000, 102),
(7, 'William Rodriguez', 41, 91000, 103),
(8, 'Elizabeth Martinez', 29, 69000, 105),
(9, 'David Hernandez', 35, 82000, 101),
(10, 'Barbara Lopez', 40, 85000, 104),
(11, 'Richard Gonzalez', 33, 74000, 102),
(12, 'Susan Wilson', 27, 60000, 105),
(13, 'Joseph Anderson', 44, 98000, 103),
(14, 'Jessica Thomas', 31, 71000, 101),
(15, 'Thomas Taylor', 36, 80000, 104),
(16, 'Sarah Moore', 25, 58000, 102),
(17, 'Charles Jackson', 39, 87000, 103),
(18, 'Karen Martin', 34, 76000, 105),
(19, 'Christopher Lee', 42, 92000, 101),
(20, 'Nancy Perez', 29, 67000, 102),
(21, 'Matthew Thompson', 37, 84000, 104),
(22, 'Margaret White', 46, 105000, 103),
(23, 'Anthony Harris', 28, 69500, 101),
(24, 'Betty Sanchez', 32, 73000, 105),
(25, 'Mark Clark', 30, 70000, 102),
(26, 'Lisa Ramirez', 33, 75500, 104),
(27, 'Donald Lewis', 41, 89000, 103),
(28, 'Dorothy Robinson', 27, 61000, 101),
(29, 'Steven Walker', 35, 83000, 105),
(30, 'Sandra Young', 31, 72500, 102);

drop table employee2;
/*-----------------------------------------------------------------------------------*/

show databases;
use batch_k_1319;
show tables;

create table student2(id int primary key,name text,age int,city text);

-- create table student(id int primary key,name text,age int check(age>=18 and age<=30),city text);
-- alter table student add constraint check_student_age check(age>=18 and age<=30);
-- alter table student drop check check_student_age;

INSERT INTO student (id, name, age, city) VALUES
(1, 'Aarav Sharma', 20, 'Mumbai'),
(2, 'Isha Verma', 21, 'Delhi'),
(3, 'Rohan Gupta', 19, 'Bangalore'),
(4, 'Sneha Patil', 22, 'Pune'),
(5, 'Aditya Singh', 20, 'Lucknow'),
(6, 'Neha Reddy', 23, 'Hyderabad'),
(7, 'Karan Mehta', 21, 'Ahmedabad'),
(8, 'Priya Nair', 22, 'Kochi'),
(9, 'Rahul Das', 20, 'Kolkata'),
(10, 'Ananya Iyer', 19, 'Chennai'),
(11, 'Vikram Joshi', 24, 'Nagpur'),
(12, 'Pooja Kapoor', 21, 'Chandigarh'),
(13, 'Siddharth Jain', 22, 'Jaipur'),
(14, 'Meera Kulkarni', 20, 'Pune'),
(15, 'Arjun Mishra', 23, 'Varanasi'),
(16, 'Kavya Shetty', 21, 'Mangalore'),
(17, 'Nikhil Bansal', 22, 'Delhi'),
(18, 'Divya Bhatt', 20, 'Surat'),
(19, 'Manish Yadav', 24, 'Patna'),
(20, 'Ritika Saxena', 19, 'Bhopal'),
(21, 'Harsh Vardhan', 23, 'Indore'),
(22, 'Tanvi Desai', 21, 'Mumbai'),
(23, 'Abhishek Roy', 22, 'Kolkata'),
(24, 'Simran Kaur', 20, 'Amritsar'),
(25, 'Deepak Choudhary', 24, 'Jodhpur'),
(26, 'Shreya Ghosh', 21, 'Durgapur'),
(27, 'Amit Tiwari', 23, 'Kanpur'),
(28, 'Nisha Agarwal', 22, 'Ranchi'),
(29, 'Yash Thakur', 20, 'Shimla'),
(30, 'Komal Pawar', 21, 'Nashik');

drop table student2;
drop database student
/*-----------------------------------------------------------------------------------*/