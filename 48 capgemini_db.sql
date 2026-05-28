create database capgemini;

use capgemini;

create table employee (
	id int,
    name varchar(10),
    profile varchar(10),
    email varchar(25),
    salary int,
    age int,
    experience int
);

insert into employee (id, name, profile, email, salary, age, experience) values
(1, 'rani', 'dev', 'rani@gmail.com', 11000, 43, 27),
(2, 'raj', 'test', 'raj@gmail.com', 21000, 33, 17),
(3, 'radha', 'test', 'radha@gmail.com', 26000, 38, 21),
(4, 'raj', 'dev', 'raj12@gmail.com', 51000, 32, 12),
(5, 'john', 'dev', 'john@gmail.com', 51000, 39, 27);

select name from employee where salary > 20000;

select * from employee where salary = 51000;

select name, experience from employee where age > 35;

select * from employee where profile = 'dev';

select * from employee where profile = 'test';

select * from employee where salary >= 25000;

select name, email from employee where salary != 51000;


update employee set salary = salary + 10000 where experience < 20;

delete from employee where id = 27;

update employee set salary = salary - 21000 where id = 4;

-------------------------------------------------------------------------------

alter table employee add column branch_location varchar(25);

select sum(salary) as total_salary from employee;

select max(salary) as max_salary from employee where profile = 'test';

select avg(experience) as avg_experience from employee;

select name, salary from employee where salary = (select max(salary) from employee);

select name, experience, salary from employee where salary = (select min(salary) from employee);

select count(distinct name) from employee;

select name, salary from employee where profile = 'test' and salary > 25000;

update employee set profile = 'support' where name = 'radha';

select * from employee where salary < (select max(salary) from employee);

select * from employee where salary < (select min(salary) from employee);
SELECT * FROM employee WHERE salary = (SELECT MIN(salary) FROM employee WHERE salary > (SELECT MIN(salary) FROM employee));   

select avg(salary) as avg_salary from employee where profile = 'dev';

select name, salary from employee where experience = (select min(experience) from employee);

select name, salary from employee where experience = (select min(experience) from employee) and salary = (select max(salary) from employee);

----------------------------------------------------------------------------------------------------------------------------------------------------------

create table employee3 (
	id int,
    name varchar(10),
    salary int,
    department varchar(25),
    location varchar(25)
);

insert into employee2 (id, name, salary, department, location) values
(1, 'anup', 10000, 'dev', 'pune'),
(2, 'rani', 26000, 'test', 'nashik'),
(3, 'jay', 18000, 'dev', 'nagpur'),
(4, 'vishal', 22000, 'support', 'pune'),
(5, 'shina', 35000, 'test', 'nagpur'),
(6, 'rony', 11000, 'support', 'nagpur'),
(7, 'pooja', 38000, 'dev', 'nashik');

select name from employee2;   

select count(*) from employee2;   

select distinct department from employee2;   

select department, count(*) as emp_count from employee2 group by department;   

select name, salary from employee2 order by salary desc limit 1;   

select name, salary from employee2 order by salary asc limit 1;   

select count(*) from employee2 where salary > 20000;   

select avg(salary) from employee2;   

select name, salary from employee2 order by salary desc limit 5;   

select name from employee2 where department = 'marketing';   

select count(*) from employee2 where salary between 15000 and 25000;   

select name from employee2 where salary is null;   

select name from employee2 where name like 'j%';  

select salary from employee2 order by salary desc;   

select sum(salary) from employee2;   
 
select name, count(*) from employee2 group by name having count(*) > 1;   

select count(*) from employee2 where location = 'pune';   

select avg(salary) from employee2 where department = 'dev';   

select name, salary from employee2 where salary > (select avg(salary) from employee2);   

select name, salary from employee2 where department = 'test' order by salary asc limit 1;   

select count(*) from employee2 where extract(year from hire_date) = 2023;   

select sum(salary) from employee2 where department in ('dev', 'support');   

select name, salary from employee2 where salary > (select avg(salary) from employee2 where department = 'dev');   

select sum(salary) from employee2 where location = 'pune';   

------------------------------------------------------------------------------------------------------------------------

drop table if exists employee4;

create table employee4 (
    id int,
    name varchar(20),
    salary int,
    department_id int,
    location_id int,
    hire_date date
);   

insert into employee4 (id, name, salary, department_id, location_id, hire_date) 
values 
(1, 'alice', 25000, 1, 1, '2022-01-15'),
(2, 'bob', 22000, 1, 2, '2022-02-20'),
(3, 'charlie', 28000, 2, 1, '2022-03-10'),
(4, 'david', 20000, 2, 2, '2022-04-05'),
(5, 'eve', 30000, 1, 1, '2023-01-07');   


create table departments (
	department_id int,
    department_name varchar (20));
    
insert into departments (department_id, department_name) values
	(1, 'marketing'),
    (2, 'development'),
    (3, 'support');


create table locations (
	location_id int,
    city varchar (20));
    
insert into locations (location_id, city) values
	(1, 'pune'),
    (2, 'mumbai');

select e.name, e.salary
from employee4 e
join departments d on e.department_id = d.department_id
where d.department_name = 'marketing';   

select e.name, d.department_name, e.salary
from employee4 e
join departments d on e.department_id = d.department_id
where e.salary > (select avg(salary) from employee4);   

select e.name, e.salary
from employee4 e
join departments d on e.department_id = d.department_id
where d.department_name = 'test'
order by e.salary asc
limit 1;   

select sum(salary) from employee4;   

select avg(e.salary)
from employee4 e
join departments d on e.department_id = d.department_id
where d.department_name = 'development';   

select sum(e.salary)
from employee4 e
join departments d on e.department_id = d.department_id
where d.department_name in ('development', 'support');   

select e.name, e.salary
from employee4 e
where e.salary > (
    select avg(e2.salary)
    from employee4 e2
    join departments d2 on e2.department_id = d2.department_id
    where d2.department_name = 'development'
);   

select sum(e.salary)
from employee4 e
join locations l on e.location_id = l.location_id
where l.city = 'pune';   

select e.name, d.department_name, e.hire_date
from employee4 e
join departments d on e.department_id = d.department_id
where year(e.hire_date) = 2023;   

select count(*)
from employee4 e
join locations l on e.location_id = l.location_id
where l.city = 'pune';   
----------------------------------------------------------------------------------
