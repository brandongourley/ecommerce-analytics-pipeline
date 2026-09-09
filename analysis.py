import pandas as pd
import pandas_gbq

project_id = "project-ad136c05-fb28-45e6-9a9"

# Pull the finished marts down from BigQuery
customer_metrics = pandas_gbq.read_gbq("SELECT * FROM capstone_dbt.customer_metrics", project_id=project_id)
revenue = pandas_gbq.read_gbq("SELECT * FROM capstone_dbt.revenue_over_time", project_id=project_id)

print(customer_metrics.sort_values(by="total_spent", ascending=False).head(5))

print(customer_metrics["avg_order_value"].mean())

print(customer_metrics.groupby("city")["total_spent"].sum().sort_values(ascending=False).head(5))

print(revenue.sort_values(by="total_revenue", ascending=False).head())

revenue["avg_order_value"] = revenue["total_revenue"] / revenue["order_count"]
print(revenue.sort_values(by="avg_order_value", ascending=False).head())