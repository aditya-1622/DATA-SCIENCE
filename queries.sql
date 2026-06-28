runners: runner_id, registration_date

runner_orders: order_id, runner_id, pickup_time, distance_km, duration_min, cancellation (NULL or empty string = successful delivery; any text = cancellation reason)

customer_orders: order_id, customer_id, pizza_id, order_time

pizza_names: pizza_id, pizza_name, price (₹: Meatlovers = 120, Vegetarian = 100)


-- TASK 1..

SELECT DISTINCT p.pizza_name
from customer_orders c 
join pizza_names p 
on c.pizza_id = p.pizza_id 
order by p.pizza ASC;



-- TASK 2..

SELECT p.pizza_name ,
sum (
    case 
    when p.pizza_id = 1 then 120
    when p.pizza_id = 2 then 100
    end
) as total_revenue
from customer_orders c
join runner_orders r
on c.order_id - r.order_id
join pizza_names p
on c.pizza_id = p.pizza_id
where r.cancellation is NULL or r.cancellation = ''
group by p.pizza_name;


--TASK 3..

select customer_id,
count(order_id) as total_orders,
case 
when count (order_id) >= 3 then 'frequent'
when count (order_id) = 2 then 'Regular'
else 'Occasional'
end as frequency_category
from customer_orders
group by customer_id;


--TASK 4..

select 
customer_id,
total_revenue,
dense_rank() over (order by total_revenue DESC) AS revenue_rank
from (
    select 
    c.customer_id,
    sum(
        case
        when c.pizza_id = 1 then 120
        when c.pizza_id = 2 then 100
        end
    ) as total_revenue
    from customer_orders c
    join runner_orders r
on c.order_id = r.order_id
    where r.cancellation is NULL or r.cancellation = ''
    group by c.customer_id
) t 
order by revenue_rank;




























-- TASK 1..

import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'secret99',
    database = 'retail_db'

)
cursor = conn.cursor()


-- TASK 2..

query = """
select 
o.order_id,
p.product_name,
p.category,
p.price,
o.quantity
from orders o
join products p
on o.product_id = p.product_id
where p.price> 500
order by p.price DESC
"""

cursor.execute(query)

rows = cursor.fetchall()

-- TASK 3..

columns = [col[0] for col in cursor.description]

df = pd.DataFrame(rows, columns = columns)
print("DataFrame:")
print(df)

-- TASK 4..

revenue = {}

for row in rows:
order_id, product_name, category,price_quantity = row
total = price * quantity

if category in revenue:
revenue[category] += total
else:
revenue[category] = total

print("\nRevenue Per Category:")
print(revenue)

-- TASK 5..

cursor.close()
conn.close()
