import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Iris.csv")

# Show first 5 rows
print(df.head())
# Check dataset shape
print("Shape:", df.shape)

# Column names
print("Columns:", df.columns)

# Count of each flower type
print(df['Species'].value_counts())
from sklearn.model_selection import train_test_split

# Separate input and output
X = df.drop('Species', axis=1)
y = df['Species']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training size:", X_train.shape)
print("Testing size:", X_test.shape)
# Drop Id and output column
X = df.drop(['Id', 'Species'], axis=1)

# Output label
y = df['Species']
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("Model trained successfully")
# Predict on test data
y_pred = model.predict(X_test)

print("First 5 Predictions:", y_pred[:5])
print("Actual Values:", y_test.values[:5])
from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
