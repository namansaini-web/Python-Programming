-- Give me information of the customer with ID C014
select *
from `e1.customers`
where CustomerID = "C014"

-- Customers Support team wants a list of all customers with their city and states
select
  CustomerID, 
  City,
from `e1.customers`

-- Show all product categories available 
select distinct CategoryID 
from `e1.products`

--Display customers from nagpur
select *
from `e1.customers`
where city = "Nagpur" 

--Display Female customers
select *
from `e1.customers`
where Gender = "F"

-- display Customers older then 30
select *
from `e1.customers`
where Age > 30

-- Display products costing at most rupees 50000
select *
from `e1.payments`
where Amount <= 50000

-- Display Delivered Orders 
select *
from `e1.orders`
where status = "Delivered"

-- Display Orders that are not Delivered
select *
from `e1.orders`
where status != "Delivered"

-- Count Total Customers 
select CustomerID
from `e1.customers`

select count(*)     -- Counting number of rows
from `e1.customers`

-- Count customers from mumbai
select count(*)
from `e1.customers`
where City = "Mumbai"

-- Find the names of the employees works in the Operations department
select Name
from `e1.employees`
where Department = "Operations"

-- Display all products supplied by supplier ID 3
select *
from `e1.products`
where SupplierID = "SUP003"

-- The inventory team wants to see products having stock less than 30 units
select *
from `e1.inventory`
where stock < 30

-- Find all customers who signed up after 2024-01-05
select *
from `e1.customers`
where SignupDate > '2024-01-05'

-- Count how many different product category exits in the product table 
select count(distinct CategoryID) 
from `e1.products`












