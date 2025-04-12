# Churn Classifier

This project predicts whether a customer is likely to churn based on their tenure (how long they’ve been with the company).

## 🔧 What It Does
- Loads customer data from `review_data.csv`
- Trains a logistic regression model using `scikit-learn`
- Accepts user input for tenure (in months)
- Predicts churn status (`Churn` or `No Churn`) with confidence

## 📁 Files
- `churn_classifier.py` &mdash; Runs the logistic regression model and prediction script
- `review_data.csv` &mdash; Input training data for customer churn

## ⚖️ Requirements
- Python 3.12+
- pandas
- scikit-learn

Install dependencies:
```bash
pip install pandas scikit-learn
```

## 🔄 How to Use
1. Run the script in your terminal or Python IDE.
2. Enter a tenure value in months when prompted.
3. View predicted churn status and model confidence.

## 🚀 Sample Output
```
Model accuracy: 100.00%
Enter tenure in months: 5
Customer will churn. (Confidence: 87.23%)
