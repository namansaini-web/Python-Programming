-- Which payment method represents the highest total payment amount?
select 
  Method,
  sum(Amount) as TotalPayment
from `e1.payments`
where Status = "Success"
group by Method 
order by TotalPayment desc ;

-- Sort customers by city alphabetically, and within each city sort customers by age from oldest to youngest.
select
  CustomerID,
  City,
  Age
from `e1.customers`
order by City asc, Age desc ;


-- Display the SuppliersIDs with Highest number of products first.
-- If tied, Highest average selling price first.
select 
  SupplierID,
  count(*) as NoOfProducts,
  avg(SellingPrice) as AvgSellingPrice
from `e1.products`
group by SupplierID
order by NoOfProducts desc, AvgSellingPrice desc ;

-- Sort products by category first and within each category sort by selling price from highest to lowest
select
  ProductID,
  CategoryID,
  SellingPrice
from `e1.products`
order by CategoryID, SellingPrice desc ;

-- Give me indiviual products whose MRP is greater than Rs20000
select *
from `e1.products`
where MRP > 20000 ;


-- HAVING :

-- Which suppliers have more then 3 products
select
  SupplierID,
  count(*) as NoOfProducts
from `e1.products`
group by SupplierID
having NoOfProducts > 3 ;

-- Which customers have placed more then 5 orders?
select
  CustomerID,
  count(*) as OrderPlaced
from `e1.orders`
group by CustomerID
having OrderPlaced > 5 ;     

-- Suppliers with 5 or fewer Products
select
  SupplierID,
  count(*) as ProductSold
from `e1.products`
group by SupplierID
having ProductSold <= 5 ;

-- Products with sales Above 50000
select
  ProductID,
  sum(Total) as Sales
from `e1.order_items`
group by ProductID
having Sales > 50000 ;

-- Take Products, Keep MRP>500, create supplier groups, count Products, keep suppliers with > 2, 
-- Sort Highest count first , Show top 5.
select 
  SupplierID,
  count(*) NoOfProducts
from `e1.products` 
where MRP > 500
group by SupplierID
having NoOfProducts > 2
order by NoOfProducts desc
limit 5 ;

