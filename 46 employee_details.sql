show databases;

create database Employee_db;

use Employee_db;

CREATE TABLE employee_details (
	emp_id int ,
    emp_Name VARCHAR(100),
    city varchar(10),
    department varchar(50),
    salary int
);  

INSERT INTO employee_details (emp_id, emp_name, city, department, salary) VALUES
(1001, 'Alice Johnson', 'New York', 'HR', 55000),
(1002, 'Bob Smith', 'Chicago', 'IT', 75000),
(1003, 'Carol Davis', 'Seattle', 'IT', 80000),
(1004, 'David Wilson', 'Austin', 'Finance', 68000),
(1005, 'Eva Brown', 'Denver', 'Marketing', 60000),
(1006, 'Frank Miller', 'Boston', 'IT', 72000),
(1007, 'Grace Lee', 'Miami', 'Sales', 50000),
(1008, 'Henry Taylor', 'Atlanta', 'Sales', 52000),
(1009, 'Irene Moore', 'Phoenix', 'Finance', 70000),
(1010, 'Jack Anderson', 'Dallas', 'HR', 54000),
(1011, 'Kate White', 'San Diego', 'Marketing', 58000),
(1012, 'Liam Harris', 'Portland', 'IT', 78000),
(1013, 'Mia Clark', 'Denver', 'Finance', 66000),
(1014, 'Noah Lewis', 'Austin', 'Sales', 53000),
(1015, 'Olivia Hall', 'Seattle', 'IT', 82000),
(1016, 'Paul Young', 'Chicago', 'HR', 56000),
(1017, 'Quinn King', 'New York', 'Marketing', 61000),
(1018, 'Rachel Scott', 'Boston', 'Sales', 51000),
(1019, 'Steve Green', 'Phoenix', 'Finance', 69000),
(1020, 'Tina Wright', 'Dallas', 'IT', 77000);     

select * from employee_details;

select * from employee_details where department = "sales";

select * from employee_details where salary > 20000 and salary < 50000;

select * from employee_details where department ="marketing" and salary<30000;

select * from employee_details where department ="sales" and department = "hr";

-----------------------------------------------------------------------------------------------------------------
select * from employee_details;

SET SQL_SAFE_UPDATES = 0;   

update employee_details set department = 'Sales' where salary < 20000;

update employee_details set department = 'finance' where emp_id = 2;

update employee_details set department = 'HR' where salary between 20000 and 30000;

update employee_details set department = 'sales' where salary between 20000 and 27000;

update employee_details set department = 'sales' where salary > 50000 ;

select * from employee_details order by Salary;

update employee_details set department = 'it' where salary between 20000 and 30000;

select * from employee_details limit 5;

-----------------------------------------------------------------------------------------------------------------

select emp_name, Salary + 2000 as increment from employee_details;

select emp_name, Salary - 2000 as decrement from employee_details;

select emp_name, Salary * 0.2 as percent from employee_details;

select * from employee_details where department = 'sales';

select * from employee_details where department <> 'hr';
