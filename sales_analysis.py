import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# 1. Create sample data
# -------------------------

data = {
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Laptop", "Mouse", "Keyboard", "Monitor"
    ],
    "Month": [
        "January", "January", "January", "January",
        "February", "February", "February", "February",
        "March", "March", "March", "March"
    ],
    "Quantity": [5, 20, 12, 7, 8, 25, 15, 10, 6, 18, 20, 12],
    "Unit_Price": [800, 20, 50, 200, 800, 20, 50, 200, 800, 20, 50, 200],
    "Unit_Cost": [600, 10, 30, 140, 600, 10, 30, 140, 600, 10, 30, 140]
}

df = pd.DataFrame(data)

# -------------------------
# 2. Data calculations
# -------------------------

df["Revenue"] = df["Quantity"] * df["Unit_Price"]

df["Cost"] = df["Quantity"] * df["Unit_Cost"]

df["Profit"] = df["Revenue"] - df["Cost"]

# -------------------------
# 3. Business analysis
# -------------------------

total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .idxmax()
)

monthly_revenue = df.groupby("Month")["Revenue"].sum()

product_profit = (
    df.groupby("Product")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

# -------------------------
# 4. Print results
# -------------------------

print("=" * 40)
print("SALES ANALYSIS REPORT")
print("=" * 40)

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Items Sold: {total_quantity}")
print(f"Best Selling Product: {best_product}")

print("\nMonthly Revenue:")
print(monthly_revenue)

print("\nProfit by Product:")
print(product_profit)

# -------------------------
# 5. Export results
# -------------------------

df.to_csv("sales_analysis_results.csv", index=False)

monthly_revenue.to_csv("monthly_revenue.csv")

product_profit.to_csv("product_profit.csv")

# -------------------------
# 6. Visualize monthly revenue
# -------------------------

monthly_revenue.plot(
    kind="bar",
    title="Monthly Sales Revenue",
    xlabel="Month",
    ylabel="Revenue ($)"
)

plt.tight_layout()
plt.savefig("monthly_revenue.png", dpi=150)
plt.show()

print("\nReports exported successfully!")