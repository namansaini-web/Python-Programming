--Display all products and any order-item sales associated with them.
select
  p.ProductID,
  p.ProductName,
  sum(o.Total) as TotalSale
from `e1.products` as p  
inner join `e1.order_items` as o   
on p.ProductID = o.ProductID
group by p.ProductID, p.ProductName
order by TotalSale desc ;

-- Find Products With No Sales.
select
  p.ProductID,
  p.ProductName
from `e1.productID` as p  
left join `e1.order_items` oi  
on p.ProductID = oi.ProductID
where o.ProductID is Null  
group by p.ProductID, p.ProductName ;

-- Customers who registered but have never placed an order.
select
  c.CustomerID,
  c.CustomerName,
  o.CustomerID,
  o.OrderID
from `e1.customers` as c  
left join `e1.orders` as o  
on c.CustomerID = o.CustomerID 
where o.OrderID is null ;

-- For every customer, show the number of orders they have placed, including customers with zero orders.
select
  c.CustomerID,
  c.Name,
  count(o.OrderID) as NoOfOrders
from `e1.customers` as c  
left join `e1.orders` as o   
on c.CustomerID = o.OrderID 
group by c.CustomerID, c.Name
order by NoOfOrders asc ; 

select
  c.CustomerID,
  c.Name,
count(o.OrderID) as no_of_orders
from `e1.orders` as o
right join `e1.customers` as c
on c.CustomerID = o.CustomerID
group by c.CustomerID, c.Name
order by no_of_orders asc ;

-- For every customer, calculate: Customer ID, Customer name, Number of orders placed. Total amount paid through successful payments only. Display only customers whose successful payment amount is greater than ₹50,000. Sort customers from highest to lowest successful payment amount.
select
  c.CustomerID,
  c.CustomerName,
  o.CustomeriD,
  count(o.OrderID) as NoOfOrders,
  sum(p.Total) as AmountPaid
from `e1.customers` as c   
inner join `e1.order` as o   
on c.CustomerID = o.CustomerID
inner join `e1.payments` as p   
on p.OrderID = o.OrderID
group by c.CustomerID, c.CustomerName
where AmountPaid > 50000
order by NoOfOrders desc ;
