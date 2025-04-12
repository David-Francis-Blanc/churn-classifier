import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("churn_data.csv")

# Convert 'Churn' column to binary (Yes=1, No=0)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Features and label
X = df[['Tenure', 'MonthlySpend']]
y = df['Churn']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# User input
while True:
    try:
        tenure = float(input("Enter tenure in months: "))
        spend = float(input("Enter monthly spend: "))
        prediction = model.predict([[tenure, spend]])[0]
        print("Churn Prediction:", "Yes" if prediction == 1 else "No")
    except:
        break
