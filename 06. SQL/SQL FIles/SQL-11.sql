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





