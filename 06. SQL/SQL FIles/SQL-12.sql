-- Find all the products whose MRP is among the top 5 distinct highest MRPs
select *
from `e1.products`
where MRP in (
  select distinct MRP
  from `e1.products`
  order by MRP desc
  limit 5 
);

-- Find the product or products having the highest MRP
select * 
from `e1.products`
where MRP in (
  select max(MRP)
  from `e1.products`
);

-- Find products supplied by suppliers who supply at least 5 products.
select *
from `e1.products`
where SupplierID in(
  select 
    SupplierID,
  from `e1.products`
  group by SupplierID 
  having count(*) > 5 
);

--Display details of those customer who have plcaced atleast 3 orders.
select *
from `e1.orders`
where CustomerID in (
  select 
    CustomerID,
  from `e1.orders`
  group by CustomerID
  having count(*) >= 3
) ;

--Find suppliers whose number of products is greater than the average number of products supplied per supplier.
select
  SupplierID,
  count(*) as NoOfProd
from `e1.products`
group by SupplierID
having NoOfProd  >= (
                  select 
                    avg(NoOfProducts)
                  from (
                        select 
                          SupplierID,
                          count(*) as NoOfProducts
                        from `e1.products`
                        group by SupplierID
                        )
                  );
