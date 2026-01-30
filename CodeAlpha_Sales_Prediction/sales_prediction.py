# =====================================
# TASK 4: SALES PREDICTION
# =====================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load dataset
df = pd.read_csv("Advertising.csv")

print("First 5 rows of dataset:")
print(df.head())

# Step 2: Drop unnecessary column
if 'Unnamed: 0' in df.columns:
    df.drop('Unnamed: 0', axis=1, inplace=True)

# Step 3: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Exploratory Data Analysis
sns.pairplot(df)
plt.show()

# Step 5: Feature selection
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining size:", X_train.shape)
print("Testing size:", X_test.shape)

# Step 7: Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully")

# Step 8: Predictions
y_pred = model.predict(X_test)

# Step 9: Model evaluation
print("\nModel Performance:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 10: Actual vs Predicted Sales
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()

# Step 11: Advertising impact analysis
plt.figure(figsize=(8,5))
sns.regplot(x=df['TV'], y=df['Sales'])
plt.title("Impact of TV Advertising on Sales")
plt.show()

print("\n--- Sales Prediction Completed Successfully ---")
