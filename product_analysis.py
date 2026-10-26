import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Customer_ID": [
        101, 102, 103, 101, 104,
        102, 105, 103, 101, 104,
        105, 102, 106, 103, 101
    ],
    "Order_ID": [
        1001, 1002, 1003, 1004, 1005,
        1006, 1007, 1008, 1009, 1010,
        1011, 1012, 1013, 1014, 1015
    ],
    "Amount": [
        120, 80, 200, 150, 90,
        110, 300, 175, 250, 130,
        220, 160, 75, 210, 180
    ]
}

df = pd.DataFrame(data)

df = df.drop_duplicates(subset=["Order_ID"])
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df = df.dropna(subset=["Customer_ID", "Order_ID", "Amount"])
df = df[df["Amount"] >= 0]

customer_summary = (
    df.groupby("Customer_ID")
    .agg(
        Total_Spent=("Amount", "sum"),
        Number_Of_Orders=("Order_ID", "nunique"),
        Average_Order=("Amount", "mean")
    )
    .round(2)
)

customer_summary["Customer_Segment"] = customer_summary["Total_Spent"].apply(
    lambda amount: (
        "High Value" if amount >= 400
        else "Medium Value" if amount >= 200
        else "Low Value"
    )
)

customer_summary = customer_summary.sort_values(
    "Total_Spent",
    ascending=False
)

total_customers = df["Customer_ID"].nunique()
total_orders = df["Order_ID"].nunique()
total_revenue = df["Amount"].sum()
average_order_value = df["Amount"].mean()

print(f"Total Customers: {total_customers}")
print(f"Total Orders: {total_orders}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Average Order Value: ${average_order_value:.2f}")

print("\nCustomer Summary:")
print(customer_summary)

customer_summary.to_csv("customer_analysis_report.csv")

customer_summary["Total_Spent"].plot(
    kind="bar",
    title="Total Spending by Customer",
    xlabel="Customer ID",
    ylabel="Total Spending ($)"
)

plt.tight_layout()
plt.savefig("customer_spending.png", dpi=150)
plt.show()

print("\nCustomer report created successfully!")