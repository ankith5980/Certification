import pandas as pd

# sales DataFrame
sales_df = pd.DataFrame({
    "Region": ["South", "North", "South", "East", "North"],
    "Product": ["A", "B", "C", "D", "A"],
    "Sales": [60000, 40000, 52000, 70000, 30000]
})

# Total sales in each region
total_sales_region = sales_df.groupby("Region")["Sales"].sum()
print(total_sales_region)

print("\n")
print("========================")
print("\n")

avg_sales_product = sales_df.groupby("Product")["Sales"].mean()
print(avg_sales_product)

print("\n")
print("========================")
print("\n")

# Use idxmax()
region_max_sales = total_sales_region.idxmax()
print("Region with maximum sales:", region_max_sales)

# Return full row
region_max_sales_row = total_sales_region.reset_index().sort_values("Sales", ascending=False).head(1)
print(region_max_sales_row)

print("\n")
print("========================")
print("\n")

# employee DataFrame
employee_df = pd.DataFrame({
    "Name": ["Ankith", "Athul", "Akshath", "Adith", "Ayana", "Elsa"],
    "Department": ["IT", "IT", "HR", "Finance", "HR", "Finance"]
})

# Count employees in each department
employee_count = employee_df["Department"].value_counts()
print(employee_count)

# using groupby
employee_count_group = employee_df.groupby("Department")["Name"].count()
print(employee_count_group)

print("\n")
print("=========PROGRAM COMPLETE=========")
print("\n")
