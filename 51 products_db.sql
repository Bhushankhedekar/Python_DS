create database product_db;

show databases;

use product_db;

create table products2 (
	p_id int,
    p_name varchar (25),
    category varchar (25),
    price float 
);

drop table products;

INSERT INTO products2 (p_id, p_name, category, price) VALUES
(1, 'Wireless Mouse', 'Electronics', 29.99),
(2, 'USB-C Hub', 'Electronics', 45.50),
(3, 'Bluetooth Speaker', 'Electronics', 89.00),
(4, 'LED Monitor 24"', 'Electronics', 199.99),
(5, 'Mechanical Keyboard', 'Electronics', 120.00),
(6, 'Office Chair', 'Furniture', 150.75),
(7, 'Standing Desk', 'Furniture', 350.00),
(8, 'Bookshelf', 'Furniture', 85.20),
(9, 'Coffee Table', 'Furniture', 110.00),
(10, 'Filing Cabinet', 'Furniture', 95.50);   

select * from products2;

select category, sum(price) as total_price from products2 group by category;

alter table products2 add column discount float;

alter table products2 drop column discount;

alter table products2 modify price int;

alter table products2 change price cost int;

alter table products2 rename to products;

