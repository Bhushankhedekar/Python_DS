create database shopping_db;
use shopping_db;
create table products (
p_id int ,
p_name varchar(50),
category varchar(20),
brand varchar(20),
price int ,
quantity float ,
rating float );

INSERT INTO products (p_id, p_name, category, brand, price, quantity, rating) VALUES
(1, 'Laptop', 'Electronics', 'Dell', 800, 50, 4.5),
(2, 'Smartphone', 'Electronics', 'Samsung', 600, 100, 4.7),
(3, 'Tablet', 'Electronics', 'Apple', 500, 30, 4.6),
(4, 'Headphones', 'Electronics', 'Sony', 100, 200, 4.3),
(5, 'T-Shirt', 'Clothing', 'Nike', 25, 150, 4.1),
(6, 'Jeans', 'Clothing', 'Levi\'s', 60, 80, 4.4),
(7, 'Sneakers', 'Footwear', 'Adidas', 90, 60, 4.5),
(8, 'Watch', 'Accessories', 'Casio', 40, 120, 4.0),
(9, 'Backpack', 'Accessories', 'Samsonite', 70, 40, 4.2),
(10, 'Water Bottle', 'Accessories', 'Hydro Flask', 30, 200, 4.8);   

 update products set price = 30 where p_id = 5;
 
 update products set price = price * 1.1 where category = 'Electronics';
 
 update products set quantity = 100 and rating = 5 where p_id = 1;
 
 delete from products where p_id = 10;
 
 delete from products where category = 'Clothing';

delete from products where quantity = 0;

SELECT DISTINCT category FROM products;   

 SELECT DISTINCT brand FROM products;  
 
 SELECT DISTINCT rating FROM products;   
 
 select * from products order by price;
--------------------------------------------------------------------------

create table student(
s_id int ,
s_name varchar(20),
course varchar(20),
percentage decimal(2)
);

insert into student (s_id, s_name, course, percentage) values 
( 101, "ABC", "CSE", 85),
(102, "PQR", "IT", 88),
(103, "XYZ", "EXTC", 79);


