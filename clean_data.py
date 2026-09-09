import pandas as pd

# --- Clean customers ---
customers = pd.read_csv("raw_customers.csv")
customers = customers.drop_duplicates()
customers["city"] = customers["city"].str.strip().str.lower()
customers["email"] = customers["email"].str.strip().str.lower()
customers["email"] = customers["email"].fillna("unknown")
customers["signup_date"] = pd.to_datetime(customers["signup_date"], format="mixed")

# --- Clean orders ---
orders = pd.read_csv("raw_orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"], format="mixed")
orders["status"] = orders["status"].str.strip().str.lower()
orders["status"] = orders["status"].fillna("unknown")
orders["amount"] = orders["amount"].str.replace("$", "", regex=False)
orders["amount"] = orders["amount"].astype(float)

# --- Save cleaned data ---
customers.to_csv("cleaned_customers.csv", index=False)
orders.to_csv("cleaned_orders.csv", index=False)

print("Cleaning complete. Saved cleaned_customers.csv and cleaned_orders.csv")