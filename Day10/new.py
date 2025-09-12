# Create a house price prediction dataset using numpy

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings("ignore")

# 1. Generate synthetic dataset
np.random.seed(42)
n_samples = 1000
sizes = np.random.randint(500, 3500, n_samples)  # in sqft
bedrooms = np.random.randint(1, 6, n_samples)
ages = np.random.randint(0, 30, n_samples)  # in years
locations = np.random.choice(['Downtown', 'Suburb', 'Countryside'], n_samples)
base_prices = sizes * 150 + bedrooms * 10000 - ages * 5000
location_factors = {'Downtown': 50000, 'Suburb': 20000, 'Countryside': -10000}
prices = base_prices + [location_factors[loc] for loc in locations] + np.random.normal(0, 20000, n_samples)
data = pd.DataFrame({
    'Size': sizes,
    'Bedrooms': bedrooms,
    'Age': ages,
    'Location': locations,
    'Price': prices
})
data.to_csv('house_prices.csv', index=False)
print(data.head())

# 2. Load dataset
df = pd.read_csv('house_prices.csv')
print(df.head())

# 3. Features & Target
X = df[['Size', 'Bedrooms', 'Age', 'Location']]
y = df['Price']

# One-hot encode categorical "Location"
X = pd.get_dummies(X, columns=['Location'], drop_first=True)

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train Linear Regression with Polynomial Features
pipeline = Pipeline([
    ('poly_features', PolynomialFeatures(degree=2, include_bias=False)),
    ('scaler', StandardScaler()),
    ('lin_reg', LinearRegression())
])
pipeline.fit(X_train, y_train)

# 6. Evaluate
y_pred = pipeline.predict(X_test)
print("\n Model trained successfully")
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))


# 8. User Input Prediction
print("\n--- House Price Prediction ---")
try:
    size = float(input("Enter house size (in sqft): "))
    bedrooms = int(input("Enter number of bedrooms: "))
    age = int(input("Enter house age (in years): "))
    location = input("Enter location (Downtown, Suburb, Countryside): ").strip()
except (ValueError, EOFError, KeyboardInterrupt) as e:
    print(f"Input error or interrupted: {e}")
    print("Using default values for demonstration...")
    size, bedrooms, age, location = 2000, 3, 5, "Suburb"

# Validate location input
valid_locations = ['Downtown', 'Suburb', 'Countryside']
if location not in valid_locations:
    print(f"Invalid location. Please choose from: {valid_locations}")
    location = 'Suburb'  # Default fallback

# Prepare input data
input_data = pd.DataFrame({
    'Size': [size],
    'Bedrooms': [bedrooms],
    'Age': [age],
    'Location': [location]
})

# Get the same dummy variables as the training data
input_encoded = pd.get_dummies(input_data, columns=['Location'], drop_first=True)

# Ensure all training columns are present
training_columns = X_train.columns.tolist()
for col in training_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

# Reorder columns to match training data
input_encoded = input_encoded[training_columns]

# Make prediction
predicted_price = pipeline.predict(input_encoded)
print(f"Predicted house price: ${predicted_price[0]:,.2f}")

# 9. Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.plot([y.min(), y.max()], [y.min(), y.max()], linestyle='--', color='red')
plt.show()

# 10. Clean up generated dataset file
if os.path.exists('house_prices.csv'):
    os.remove('house_prices.csv')
    print("Temporary dataset file cleaned up.")

print("\nProgram completed successfully!")
