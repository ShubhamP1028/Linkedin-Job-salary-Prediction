# -*- coding: utf-8 -*-
"""Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1juimTp-NnkOAFcY4x4FcsAnxufT_OhtI

#### Step 2: Training Logistic Regression model to predict salary range from top skills and job info
Step 2.1: Import skill extraction functions. Load dataset and process using skills_extraction

Step 2.2: Bin salary into 3 classes (low, medium, high)

Step 2.3: Select features and target

Step 2.4: One-hot encode categorical features

Step 2.5: Train-test split

Step 2.6: Training Logistic Regression model

Step 2.7: Evaluate the model
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.metrics import classification_report, f1_score, mean_squared_error

raw_df = pd.read_csv("final.csv")

import nltk
nltk.download('punkt_tab')
df = process_dataframe(raw_df)

import matplotlib.pyplot as plt

plt.hist(df['avgsal'], bins=30, edgecolor='k')
plt.title("Salary Distribution")
plt.xlabel("Average Salary")
plt.ylabel("Frequency")
plt.show()

salary_bins = [0, 12.5, 15, np.inf]
salary_labels = ['low', 'medium', 'high']
df['salary_class'] = pd.cut(df['avgsal'], bins=salary_bins, labels=salary_labels)

features = ['top_skill', 'experienceLevel', 'location', 'contractType']
target = 'salary_class'

df_model = df[features + [target]].dropna()

ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_encoded = ohe.fit_transform(df_model[features])
y = df_model[target]

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

print("Model Evaluation")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")

# Confusion Matrix heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=salary_labels, yticklabels=salary_labels)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix Heatmap")
plt.tight_layout()
plt.show()



y_test_codes = y_test.cat.codes
y_pred_series = pd.Series(y_pred, dtype='category')
y_pred_codes = y_pred_series.cat.codes

# Now compute metrics
mse = mean_squared_error(y_test_codes, y_pred_codes)
f1 = f1_score(y_test_codes, y_pred_codes, average='macro')

print("F1-Score:", round(f1 * 100, 2), "%")
print("Mean Squared Error:", round(mse, 2))

print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Bar plot of actual vs predicted
plt.figure(figsize=(6, 4))
pd.Series(y_test).value_counts().sort_index().plot(kind='bar', alpha=0.6, label='Actual', color='#9b59b6')
pd.Series(y_pred).value_counts().sort_index().plot(kind='bar', alpha=0.6, label='Predicted', color='#720cac')
plt.title("Actual vs Predicted Class Counts")
plt.xlabel("Salary Class")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()

