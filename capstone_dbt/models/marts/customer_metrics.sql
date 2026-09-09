{{ config(materialized='table') }}

select
    c.customer_id,
    c.name,
    c.city,
    sum(o.amount) as total_spent,
    count(*) as order_count,
    avg(o.amount) as avg_order_value
from {{ ref('stg_orders') }} o
inner join {{ ref('stg_customers') }} c
    on o.customer_id = c.customer_id
group by c.customer_id, c.name, c.city