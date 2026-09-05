-- order by :
-- Default order => ascending

-- Select products from lowest selling price to the highest
select
  ProductID,
  SellingPrice
from `e1.products`
order by SellingPrice ;

-- show the most expensive products first
select
  ProductID,
  SellingPrice
from `e1.products`
order by SellingPrice desc ;






