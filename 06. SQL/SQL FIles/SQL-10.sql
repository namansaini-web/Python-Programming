-- For each supplier, calculate: Number of products supplied, Average MRP of those products, Maximum MRP of those products, Display only suppliers who supply at least 3 products. Sort them by the number of products supplied from highest to lowest.
select
  SupplierID,
  count(*) as NoOfProducts,
  avg(MRP) as  AvgMRP,
  max(MRP) as MaxMRP
from `e1.products`
group by SupplierID
having NoOfProducts >= 3
order by NoOfProducts desc ;

-- Find each CategoryID where the average MRP of products is greater than ₹100. Display: CategoryID, Number of products, Average, Maximum MRP. Sort categories by average MRP from highest to lowest.
select
  CategoryID, 
  count(*) NoOfProducts,
  avg(MRP) as AvgMRP,
  max(MRP) as MaxMRP
from `e1.products`
group by CategoryID
having AvgMRP > 100
order by AvgMRP desc ;

-- Using order_items, calculate the total quantity sold and total sales value for every product. Display only products where: Total quantity sold is at least 10, Total sales value is greater than ₹1,00,000, Sort by total sales value descending.
select
  ProductID,
  sum(Quantity) as QuantitySold,
  sum(Total) as TotalSale
from `e1.order_items`
group by ProductID
having QuantitySold >= 10 and TotalSale > 100000
order by TotalSale desc ; 

-- Find products where the selling price is lower than the MRP. Display: ProductID, ProductName, MRP, SellingPrice, Discount amount. Sort products by the highest discount amount first.
select
  ProductID,
  ProductName,
  MRP,
  SellingPrice,
  (MRP - SellingPrice) as DiscountAmount
from `e1.products`
where MRP > SellingPrice
order by DiscountAmount desc ;

-- Find products where the discount is at least 10% of MRP. Display: ProductID, ProductName, MRP, SellingPrice, Discount percentage. Sort by discount percentage from highest to lowest.
select
  ProductID,
  ProductName,
  MRP,
  SellingPrice,
  round(((MRP - SellingPrice)/MRP),2)*100 as DiscountPercentage
from `e1.products`
where round(((MRP - SellingPrice)/MRP),2)*100 >= 10
order by DiscountPercentage desc ;

-- Consider only successful payments. For each payment method, calculate: Number of successful transactions, Total payment amount, Average payment amount, Maximum payment amount, Display only methods where the total successful payment amount exceeds ₹1,00,000.
select
  Method,
  count(*) as SuccessfulPayments,
  sum(Amount) as TotalPayment,
  round(avg(Amount),2) as AvgPayments,
  max(Amount) as MaxAmount
from `e1.payments`
where Status = "Success"
group by Method
having TotalPayment > 100000 ; 

-- Find customers who have placed between 4 and 8 orders, inclusive. Display: CustomerID, Number of orders. Sort customers by order count descending and display only the top 10.
select
  CustomerID,
  count(*) as NoOfOrders
from `e1.orders`
group by CustomerID
having NoOfOrders between 4 and 8 
order by NoOfOrders desc 
limit 10 ;

-- For each warehouse, calculate: Total stock, Average stock, Highest stock for a product, Lowest stock for a product. Display only warehouses where total stock is greater than 500. Sort by total stock descending
select
  WarehouseID,
  sum(Stock) as TotalStock,
  round(avg(Stock),2) as AvgStock,
  max(Stock) as HighestStock,
  min(Stock) as LowestStock
from `e1.inventory`
group by WarehouseID
having TotalStock > 500
order by TotalStock desc ;

-- Find products that have at least one inventory record where stock is below 20 units. Display: ProductID, Number of inventory records, Minimum stock, Maximum stock. Show only products whose minimum stock is below 20
select
  ProductID,
  count(*) as NoOfRecords,
  max(Stock) as MaximumStock,
  min(Stock) as MinimumStock
from `e1.inventory`
group by ProductID
having MinimumStock < 20 ;
