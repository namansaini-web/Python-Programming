select *
from `e1.customers`
limit 

-- Show the names of all the customers
select Name
from `e1.customers`

-- Show customer cities.
select City
from `e1.customers`

-- Finance wants only payment methods.
select *
from `e1.payments`
limit 

select Method
from `e1.payments`

-- HR wants employee names.
select *
from `e1.employees`
limit 10

select name
from `e1.employees`

-- Change column names in employee table
Alter table `e1.employees`
rename column string_field_0 to EmployeeID
Alter table `e1.employees`
rename column string_field_1 to Name
Alter table `e1.employees`
rename column string_field_2 to Department

delete from `e1.employees`
where EmployeeID = "EmployeeID"

select *
from `e1.products`

-- Select multiple coulmns at one time
select
  ProductID,
  ProductName
from `e1.products`

select
  ProductID,
  ProductName,
  CategoryID
from `e1.products`

-- Select different cities 
select distinct City
from `e1.customers`

-- Select different payments methode 
select distinct method
from `e1.payments`


-- Select Different states
select *
from `e1.suppliers`
select distinct state
from `e1.suppliers`

-- Change column names in suppliers table
alter table `e1.suppliers`
rename column string_field_0 to SupplierID

alter table `e1.suppliers`
rename column string_field_1 to SupplierName

alter table `e1.suppliers`
rename column string_field_2 to State

-- how many distinct amounts do we have in this table?
select distinct amount
from `e1.payments`

-- On which dates there has been atleast 1 cutomers who signed up
select distinct SignupDate
from `e1.customers`

-- using distinct for multiple columns
select distinct age,City
from `e1.customers`

-- What are the unique combinations of payments methodes and payment status
select distinct Method,Status
from `e1.payments`
