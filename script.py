# Retail_Transaction_Insights.py
# Terminal-friendly analysis of retail transactions

import pandas as pd
from collections import Counter

# =========================
# Task 1: Data Preparation
# =========================

# Load dataset
file_path = 'Retail_Transactions_Dataset.csv'  # Change path if needed
df = pd.read_csv(file_path)

# Display basic info
print("\n=== Dataset Info ===")
print(df.info())
print("\n=== First 5 Rows ===")
print(df.head())

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Extract Year, Month, DayOfWeek
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Ensure numeric columns
df['Total_Cost'] = pd.to_numeric(df['Total_Cost'], errors='coerce')
df['Total_Items'] = pd.to_numeric(df['Total_Items'], errors='coerce')

# =========================
# Task 2: Basic Exploration
# =========================
print("\n=== Basic Exploration ===")
total_transactions = df.shape[0]
unique_customers = df['Customer_Name'].nunique()

print(f"Total Transactions: {total_transactions}")
print(f"Unique Customers: {unique_customers}")

# Top 5 products sold
all_products = [item.strip() for sublist in df['Product'].dropna().str.split(',') for item in sublist]
top_products = Counter(all_products).most_common(5)
print("\nTop 5 Products Sold:")
for product, count in top_products:
    print(f"{product}: {count} sold")

# Cities with highest transactions
top_cities = df['City'].value_counts().head(5)
print("\nTop 5 Cities by Transactions:")
print(top_cities.to_string())

# =========================
# Task 3: Customer Behaviour
# =========================
print("\n=== Customer Behaviour Analysis ===")
avg_spending = df.groupby('Customer_Category')['Total_Cost'].mean().sort_values(ascending=False)
print("\nAverage Spending per Customer Category:")
print(avg_spending.to_string())

payment_pref = df.groupby(['Customer_Category', 'Payment_Method']).size().unstack(fill_value=0)
print("\nPayment Method Preferences per Customer Category:")
print(payment_pref.to_string())

avg_items_per_store = df.groupby('Store_Type')['Total_Items'].mean()
print("\nAverage Items per Transaction per Store Type:")
print(avg_items_per_store.to_string())

# =========================
# Task 4: Promotion & Discount Impact
# =========================
print("\n=== Promotion & Discount Impact ===")
avg_cost_discount = df.groupby('Discount_Applied')['Total_Cost'].mean()
print("\nAverage Total Cost with/without Discount:")
print(avg_cost_discount.to_string())

avg_items_promo = df.groupby('Promotion')['Total_Items'].mean().sort_values(ascending=False)
print("\nAverage Number of Items per Promotion Type:")
print(avg_items_promo.to_string())

best_promo = df.groupby('Promotion')['Total_Cost'].mean().sort_values(ascending=False)
print("\nPromotion Type Most Effective (by Avg Total Cost):")
print(best_promo.to_string())

# =========================
# Task 5: Seasonality Trends
# =========================
print("\n=== Seasonality Trends ===")
season_revenue = df.groupby('Season')['Total_Cost'].sum().sort_values(ascending=False)
print("\nTotal Revenue per Season:")
print(season_revenue.to_string())

season_store = df.groupby(['Season','Store_Type'])['Total_Cost'].sum().unstack(fill_value=0)
print("\nRevenue per Season & Store Type:")
print(season_store.to_string())

season_avg = df.groupby('Season')['Total_Cost'].mean()
print("\nAverage Spending per Season:")
print(season_avg.to_string())

# =========================
# Task 6: Simple Terminal Plots
# =========================
print("\n=== Terminal Plots ===")

# Bar plot: transactions per city
print("\nTransactions per City:")
for city, count in df['City'].value_counts().items():
    bar = '*' * (count // max(1, df['City'].value_counts().max() // 50))  # scale to max 50 stars
    print(f"{city:20} | {bar} ({count})")

# Pie chart replacement: payment methods (text)
print("\nPayment Methods Distribution:")
total = df['Payment_Method'].value_counts().sum()
for method, count in df['Payment_Method'].value_counts().items():
    pct = (count / total) * 100
    print(f"{method:15} | {'*' * int(pct // 2)} ({pct:.1f}%)")

# Monthly revenue trend (text)
print("\nMonthly Revenue Trend:")
monthly_rev = df.groupby(df['Date'].dt.to_period('M'))['Total_Cost'].sum()
max_stars = 50
for period, rev in monthly_rev.items():
    stars = '*' * int((rev / monthly_rev.max()) * max_stars)
    print(f"{period} | {stars} ({rev:.2f})")

# Revenue heatmap replacement: season x customer category (text)
print("\nRevenue by Season & Customer Category:")
heatmap_data = df.pivot_table(index='Season', columns='Customer_Category', values='Total_Cost', aggfunc='sum', fill_value=0)
for season, row in heatmap_data.iterrows():
    row_display = " | ".join(f"{int(val):6}" for val in row)
    print(f"{season:10} | {row_display}")

# =========================
# Summary of Insights
# =========================
print("\n=== Summary of Insights ===")
print("- Highest spending customer category:", avg_spending.idxmax())
print("- Season with highest revenue:", season_revenue.idxmax())
print("- Most effective promotion type:", best_promo.idxmax())
print("- Cities with most transactions:", ', '.join(top_cities.index))
print("- Top products sold:", ', '.join([p[0] for p in top_products]))