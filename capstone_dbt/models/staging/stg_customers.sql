{{ config(materialized='view') }}

select customer_id, name, city, signup_date, email
from {{ source('capstone_raw', 'customers') }}