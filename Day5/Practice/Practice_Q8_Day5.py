import pandas as pd

students = pd.DataFrame({
    "Name": ["Ankith", "Athul", "Akshath", "Adith", "Ayana", "Elsa"],
    "Class": ["10A", "10B", "10A", "10C", "10C", "10A"],
    "Marks": [95, 82, 91, 76, 88, 92]
})

# Select students with Marks > 90
top_students = students[students["Marks"] > 90]
print(top_students)

print("\n")
print("========================")
print("\n")

sales = pd.DataFrame({
    "Region": ["South", "North", "South", "East", "West"],
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": [60000, 40000, 52000, 70000, 48000]
})

# Filter condition & select only columns Product and Sales
south_sales = sales[(sales["Region"] == "South") & (sales["Sales"] > 50000)][["Product", "Sales"]]
print(south_sales)

print("\n")
print("==========PROGRAM COMPLETE=========")
print("\n")
