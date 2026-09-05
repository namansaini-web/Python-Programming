-- Task: Display SupplierID and the number of products supplied by each supplier. Show suppliers with the highest number of products first.
select
  SupplierID,
count(*) as no_of_products
from `e1.products`
group by SupplierID
order by no_of_products desc ;

-- Task: Calculate the total sales value for each ProductID using the Total column from order_items. Display the products from highest to lowest sales value and show only the top 10.
select
  ProductID,
  sum(Total) as total_sales,
from `e1.order_items`
group by ProductID
order by total_sales desc
limit 10 ;

-- Task: For only payments where Status = 'Success', calculate the number of transactionsand total payment amount for each Method. Display methods with the highest total payment amount first.
select
  Method,
  count(*) as NoOfPaymemnt,
  sum(Amount) as TotalPayment
from `e1.payments`
where Status = "Success"
group by Method 
order by TotalPayment DESC;

-- Task: Calculate the number of orders placed by every CustomerID. Display only customers who have placed more than 3 orders.
select 
  CustomerID,
  count(*) as NoOfOrders
from `e1.orders`
group by CustomerID
having NoOfOrders > 3 ;

-- Task: Consider only products having an MRP greater than ₹20,000. For each CategoryID, count the number of such products. Display only categories having more than 2 qualifying products.
select
  CategoryID,
  count(*) as NoOfProducts
from `e1.products`
where MRP > 2000
group by CategoryID 
having NoOfProducts > 2 
order by NoOfProducts desc ; 

-- Task: For each WarehouseID, calculate: Total stock, Average stock per inventory record, Maximum stock in an inventory record, Minimum stock in an inventory record, Sort warehouses by total stock from highest to lowest.
select
  WarehouseID,
  sum(Stock) as TotalStock,
  round(avg(Stock), 2) as AvgStock ,
  max(Stock) as MaximumStock,
  min(Stock) as MinimumStock
from `e1.inventory`
group by WarehouseID
order by TotalStock desc ;

-- Task: For every Status in the orders table, calculate the number of orders. Display the most common order status first.
select
  Status,
  count(*) as NoOfOrders 
from `e1.orders`
group by Status 
order by NoOfOrders desc ;

-- Task: Consider only order-item records where SellingPrice > 10000. For each ProductID, calculate: Number of order-item records, Total quantity sold, Total sales value, Average selling price, Display only products whose total sales value is greater than ₹50,000, sorted by total sales value from highest to lowest.
select
  ProductID,
  count(*) as NoOfProducts,
  sum(Quantity) as QuantitySold,
  sum(Total) as TotalSale,
  round(avg(SellingPrice), 2) as AvgSellingPrice
from `e1.order_items`
where SellingPrice > 10000
group by ProductID
having TotalSale > 50000
order by TotalSale desc ;

