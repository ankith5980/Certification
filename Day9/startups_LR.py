import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score

# 1. Load dataset
df = pd.read_csv("Day9/50_startups_sample.csv")  # use full dataset if available
print(df.head())

# 2. Features & Target
X = df[["R&D Spend", "Administration", "Marketing Spend", "State"]]
y = df["Profit"]

# One-hot encode categorical "State"
ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), ["State"])],
)
X = ct.fit_transform(X)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
print("\n Model trained successfully")
print("R² Score:", r2_score(y_test, y_pred))


# 6. User Input Prediction
print("\n--- Startup Profit Prediction ---")
rd = float(input("Enter R&D Spend: "))
admin = float(input("Enter Administration Spend: "))
marketing = float(input("Enter Marketing Spend: "))
state = input("Enter State (New York/California/Florida): ")

# Prepare user input
user_df = pd.DataFrame([[rd, admin, marketing, state]],
                       columns=["R&D Spend", "Administration", "Marketing Spend", "State"])
user_X = ct.transform(user_df)

# Prediction
predicted_profit = model.predict(user_X)[0]
print(f"\nPredicted Profit: ${predicted_profit:,.2f}")