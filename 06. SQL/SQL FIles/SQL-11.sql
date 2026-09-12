-- Calculate the number of orders and percentage of total orders represented by each order status.
select
  Status,
  count(*) as NoOfOrders,
  round(count(*)*100.0/(select count(*) from `e1.orders`), 2) as TotalOrders,
from `e1.orders`
group by Status
order by NoOfOrders desc ;  

-- Using order_items, find the top 5 products based on total quantity sold. Display: ProductID, Total quantity sold, Number of order-item records, Total sales value.
select
  ProductID,
  sum(Quantity) as TotalQuantitySold,
  count(*) as NoOfOrders,
  sum(Total) as TotalSales
from `e1.order_items`
group by ProductID
limit 5 ;


-- Consider only order-item records where the total value of that item is greater than ₹2500. For each product, calculate: Number of such records, Total quantity, Total sales value. Display products having at least 3 qualifying records.
select
  ProductID,
  count(*) as NoOfRecords,
  sum(Quantity) as TotalQuantity,
  sum(Total) as TotalSale
from `e1.order_items`
where Total > 2500
group by ProductID
having NoOfRecords >= 3 ;

-- For each product, calculate: Minimum selling price, Maximum selling price, Average selling price, Number of order-item records. Display only products where the minimum selling price is greater than ₹10,000. Sort by average selling price descending.
select
  ProductID,
  min(SellingPrice) as MinSellingPrice,
  max(SellingPrice) as MaxSellingPrice,
  count(*) as NoOfItems,
  avg(SellingPrice) as AvgSellingPrice
from `e1.order_items`
group by ProductID
having MinSellingPrice > 10000
order by AvgSellingPrice desc ;

-- For every warehouse, calculate: Number of different products stored, Total stock, Average stock per product. Display only warehouses storing at least 5 different products. Sort by total stock descending
select
  WarehouseID,
  count(distinct ProductID) as NoOfProducts,
  sum(Stock) as TotalStock, 
  round(avg(Stock),2) as AvgStock
from `e1.inventory`
group by WarehouseID
having NoOfProducts > 5 
order by NoOfProducts desc ;

--Find products whose MRP is greater than the average MRP of all products.
select *
from `e1.products`
where MRP >= (
  select
    avg(MRP)
  from `e1.products`
) ;

-- Find the product or products having the highest MRP.
select *
from `e1.products`
where MRP = (
  select
    max(MRP)
  from `e1.products`
);



