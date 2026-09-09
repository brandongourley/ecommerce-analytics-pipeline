# E-Commerce Analytics: Key Findings

## Overview
This was an analysis of customer and revenue data from a purposefully messy e-commerce dataset. Transformed through a dbt pipeline on BigQuery, with insights and cleaning via Python.

## Key Findings & Next Questions

### 1. Denver is the largest market, but Miami has the biggest spenders
Denver leads total spend (~$15,356) but Miami has the top individual customers (3 of the top 5). What products are selling in Miami and not other markets? Why are they? Are the Miami buyers buying big ticket items or many smaller items? Can we use these answers to apply that strategy elsewhere?

### 2. Order volume is stable, but revenue is driven by order value
Monthly order counts stay fairly steady, but revenue swings based on average order value. March 2025 had few orders (11) but the highest avg order value ($257). What may be causing higher order values in certain months? Is this a consistent trend over time or too small of a sample to claim?

### 3. Prioritize the "whales"
All of Miami's spend comes from a small group who make up 3 of the top 5 customers as shown above. What can we learn about Miami's big spenders? How can we retain their business? Can we leverage their connections to acquire more customers like them? 

## Bottom Line
Focus on order value, not order count. That's what actually moves revenue here. And protect the handful of high-value customers who drive a disproportionate share of spend.