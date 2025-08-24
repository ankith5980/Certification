import pandas as pd

# Create DataFrame
data = {
    "Name": ["Virat Kohli", "Rohit Sharma", "Steve Smith", "Joe Root", "Kane Williamson"],
    "Team": ["India", "India", "Australia", "England", "New Zealand"],
    "Runs": [12000, 9500, 8700, 10500, 7200],
    "Matches": [250, 230, 150, 200, 180]
}

df = pd.DataFrame(data)

# Calculate batting average
df["Batting_Average"] = df["Runs"] / df["Matches"]

print(df)

print("\n")
print("========================")
print("\n")

# Load CSV
employees = pd.read_csv("employees.csv")

# Display first 5 rows
print(employees.head())

# Show column names and data types
print("\nColumn names and data types:")
print(employees.dtypes)

# Find the number of employees (rows)
print("\nNumber of employees:", len(employees))

print("\n")
print("=========PROGRAM COMPLETE=========")
print("\n")
