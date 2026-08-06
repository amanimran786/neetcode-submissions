-- Write your query below
Select c.name 
from customers AS c
Where Not Exists (
    Select 1 
    From orders AS o
    Where o.customer_id = c.id
);
