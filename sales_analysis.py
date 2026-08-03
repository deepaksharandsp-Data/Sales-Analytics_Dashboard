# ================================
# Sales Data Analysis Project
# Author : Deepak Sharan
# ================================


import pandas as pd
import matplotlib.pyplot as plt
print("Welcome to Sales Data Analysis Project")

# Read the CSV file
df = pd.read_csv("data/Global_Superstore.csv")
print(df.columns)

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())
print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nMaximum Sales:")
print(df["Sales"].max())

print("\nMinimum Sales:")
print(df["Sales"].min())
print("\nTop 10 Highest Sales:")

top_sales = df.nlargest(10, "Sales")

print(top_sales[["Order ID", "Customer Name", "Category", "Sales"]])
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())
# Sales by Category Chart

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.savefig("output/sales_by_category.png")
plt.show()
# Top 10 Highest Sales Chart

top_sales = df.nlargest(10, "Sales")

plt.figure(figsize=(12,6))

plt.bar(top_sales["Customer Name"], top_sales["Sales"])

plt.title("Top 10 Highest Sales")
plt.xlabel("Customer Name")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("output/top_10_highest_sales.png")

plt.show()
# Profit by Region

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))

plt.bar(region_profit.index, region_profit.values)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("output/profit_by_region.png")

plt.show()
# Sales by Segment

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.bar(segment_sales.index, segment_sales.values)

plt.title("Sales by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("output/sales_by_segment.png")

plt.show()

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")

# Create Month column
df["Month"] = df["Order Date"].dt.month_name()

monthly_sales = df.groupby("Month") ["Sales"].sum()

plt.figure(figsize=(10,5))

plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("output/monthly_sales_trend.png")

plt.show()
#
print(df.columns)
# Top 10 Products by Sales

top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10)

plt.figure(figsize=(12,6))

plt.bar(top_products.index, top_products.values)

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("output/top_10_products.png")

plt.show()
# Top 10 Customers by Sales

top_customers = df.groupby("Customer Name")["Sales"].sum().nlargest(10)

plt.figure(figsize=(12,6))

plt.bar(top_customers.index, top_customers.values)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("output/top_10_customers.png")

plt.show()
# Top 10 Customers by Sales

top_customers = df.groupby("Customer Name")["Sales"].sum().nlargest(10)

print("\nTop 10 Customers by Sales:")
print(top_customers)
plt.figure(figsize=(12,6))

plt.bar(top_customers.index, top_customers.values)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("output/top_10_customers.png")

plt.show()

# Profit by Category
profit_category = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(profit_category)
plt.figure(figsize=(8,5))

plt.bar(profit_category.index, profit_category.values)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("output/profit_by_category.png")

plt.show()

# Monthly Profit trend
monthly_profit = df.groupby("Month")["Profit"].sum()
print("\nMonthly Profit:")
print(monthly_profit)
plt.figure(figsize=(10,5))

plt.plot(monthly_profit.index, monthly_profit.values, marker="o")

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Total Profit")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("output/monthly_profit_trend.png")

plt.show()

# Top 10 Products by Profit

top_profit_products = df.groupby("Product Name")["Profit"].sum().nlargest(10)
print("\nTop 10 Products by Profit:")
print(top_profit_products)
plt.figure(figsize=(12,6))

plt.bar(top_profit_products.index, top_profit_products.values)

plt.title("Top 10 Products by Profit")
plt.xlabel("Product Name")
plt.ylabel("Total Profit")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("output/top_10_products_profit.png")

plt.show()

# Top 10 Customers by Profit
top_profit_customers = df.groupby("Customer Name")["Profit"].sum().nlargest(10)
print("\nTop 10 Customers by Profit:")
print(top_profit_customers)
plt.figure(figsize=(12,6))

plt.bar(top_profit_customers.index, top_profit_customers.values)

plt.title("Top 10 Customers by Profit")
plt.xlabel("Customer Name")
plt.ylabel("Total Profit")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("output/top_10_customers_profit.png")

plt.show()

# Average Sales by Category

average_sales = df.groupby("Category")["Sales"].mean()
print("\nAverage Sales by Category:")
print(average_sales)
plt.figure(figsize=(8,5))

plt.bar(average_sales.index, average_sales.values)

plt.title("Average Sales by Category")
plt.xlabel("Category")
plt.ylabel("Average Sales")

plt.tight_layout()

plt.savefig("output/average_sales_by_category.png")

plt.show()

# Sales by Ship Mode
shipmode_sales = df.groupby("Ship Mode")["Sales"].sum()
print("\nSales by Ship Mode:")
print(shipmode_sales)
plt.figure(figsize=(8,5))

plt.bar(shipmode_sales.index, shipmode_sales.values)

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Total Sales")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("output/sales_by_ship_mode.png")

plt.show()