# import modules
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load datasets
columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safty', 'class']
df = pd.read_csv("Day11/car.data", names = columns)

# preprocessing
df.info()
df.describe()
df.head()

# Null value checking
print(df.isnull().sum())
print("Duplicates :: ", df.duplicated().sum())

df['doors'] = df['doors'].replace({'5more':'5'}).astype(int)
df['persons'] = df['persons'].replace({'more':'5','5more':'5'}).astype(int)

df = pd.get_dummies(df, columns=['buying','maint','lug_boot','safty'])
le = LabelEncoder()
df['class'] = le.fit_transform(df['class'])

# Training and Testing
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Feature Scaling
scaler = StandardScaler()
X_train[['doors','persons']] = scaler.fit_transform(X_train[['doors','persons']])
X_test[['doors','persons']] = scaler.transform(X_test[['doors','persons']])

# Logistic Regression
log_reg = LogisticRegression(max_iter=500, random_state=42)
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

# Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))