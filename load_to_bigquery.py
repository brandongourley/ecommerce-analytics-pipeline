import pandas as pd
import pandas_gbq

# Read the cleaned data back in
customers = pd.read_csv("cleaned_customers.csv")
orders = pd.read_csv("cleaned_orders.csv")

# Where it's going
project_id = "project-ad136c05-fb28-45e6-9a9"
dataset = "capstone_raw"

# Push each DataFrame up to BigQuery
pandas_gbq.to_gbq(customers, f"{dataset}.customers", project_id=project_id, if_exists="replace")
pandas_gbq.to_gbq(orders, f"{dataset}.orders", project_id=project_id, if_exists="replace")

print("Loaded customers and orders into BigQuery.")