-- How many different cities do the customers belong to?
select count(distinct City)
from `e1.customers` ;

-- How many different products do we have
select count(*)
from `e1.products` ;

-- How many customers are from Mumbai
select *
from `e1.customers`
where City = "Mumbai" ;

-- Count the number of different customers that we have
select count(*)           -- Counts all number of row.
from `e1.customers` ;

select count(CustomerID)  -- Counts only non-null value.
from `e1.customers` ;

-- How many different supplier states exits
select count(distinct string_field_2)
from `e1.suppliers` ;

-- find total sales value
-- What is the total value represented by all-order item record
select sum(Total)
from `e1.order_items` ;

-- How many individual products units were sold across all order-item records 
select sum(Quantity)
from `e1.order_items` ;

-- Total quantity sold where order item have a quantity greater than 1
select sum(Quantity)
from `e1.order_items`
where Quantity > 1 ;













