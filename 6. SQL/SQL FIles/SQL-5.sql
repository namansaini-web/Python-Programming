-- Find Average selling price
select avg(SellingPrice)
from `e1.products` ;

select avg(SellingPrice) as avg_selling_price
from `e1.products` ;

-- The Finance team wants a summary of all payments tansactions
select count(*) as no_of_payments,
  sum(amount) as total_payments_amt,
  avg(amount) as avg_payments,
  min(amount) as min_payments,
  max(amount) as max_paymets
from `e1.payments` ;


-- Give the count of the number of products within each catrgory
select 
  CategoryID,
  count(*) as prod_cnt
from `e1.products`
group by CategoryID ;

-- How many units of each products have been sold?
select
  sum(Quantity) as total_Qty
from `e1.order_items`
group by ProductID ;

-- What is the total sales value genrated by each products?
select 
  ProductID,
  sum(Total) as Sales
from `e1.order_items`
group by ProductID ;  

-- What was the average selling price at which each product was sold?
select 
  ProductID,
  avg(SellingPrice) as Avg_Selling_Price
from `e1.order_items`
group by ProductID ;

-- Product Sales summary --> for every product, what is the statatics summary
select
  ProductID,
  count(*) as TotalOrders,
  sum(Total) as TotalSales,
  max(Total) as MaxSale,
  min(Total) as MinSale,
  round(avg(Total),2) as AvgSellingPrice
from `e1.order_items`
group by ProductID ;

-- For each customer, how many orders are there for each of their different order status
select 
  CustomerID,
  Status,
  count(*) as NoOfOrders
from `e1.orders`
group by Status, CustomerID ;