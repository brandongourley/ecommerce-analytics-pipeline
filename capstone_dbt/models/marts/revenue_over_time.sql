{{config(materialized='table')}}

select 
  date_trunc(date(order_date), month) as order_month,
  sum(amount) as total_revenue,
  count(*) as order_count
from {{ ref('stg_orders')}}
group by order_month
order by order_month