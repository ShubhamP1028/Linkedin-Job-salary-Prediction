# 💼 Job Salary Prediction Model (LinkedIn & ML)

A machine learning project that predicts salary ranges based on LinkedIn job listings by extracting relevant skills using NLP, feature engineering, and training a Logistic Regression classifier. This end-to-end pipeline includes web scraping, data preprocessing, skills extraction, model training, and evaluation.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-EDA-purple?logo=pandas)
![Logistic Regression](https://img.shields.io/badge/Model-Logistic_Regression-brightgreen)

---

## 📂 Project Structure
├── data/ 

│ └── linkedin.csv # Raw or cleaned job data 

├── cleandata.py

├── skills_extraction.py # NLP + regex-based skills extraction 

├── model.py # Data prep + model training + evaluation, Boxplots, confusion matrix, and metric plots
  
├── README.md # Project documentation


---

## 🧠 Problem Statement

LinkedIn job listings often lack standardized salary information. This project predicts **job salary ranges** based on:
- Skills extracted from descriptions
- Experience level
- Contract type
- Location

---

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/-Python-blue?logo=python)
![Pandas](https://img.shields.io/badge/-Pandas-yellow?logo=pandas)
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy)
![scikit-learn](https://img.shields.io/badge/-Scikit--learn-f7931e?logo=scikit-learn)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-orange?logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-3f3f3f?logo=seaborn)

---

## 🔄 Pipeline Overview

### 1. **Data Cleaning**
- Removed null values from `salary`, `salary1`, `contractType`, etc.
- Created `avg_salary` column from `salary` and `salary1`
- Removed outliers using IQR filtering

### 2. **Skills Extraction**
- Cleaned job descriptions using regex
- Extracted skills using a curated list of keywords from 13 job roles
- Created a `top_skill` feature using most frequent skill per description

### 3. **Model Building**
- Binned `avg_salary` into 3 salary classes: `low`, `medium`, `high`
- Used `top_skill`, `experienceLevel`, `location`, `contractType` as features
- Encoded features using OneHotEncoding
- Trained a **Logistic Regression** model with 80:20 train-test split

### 4. **Evaluation**
- Metrics: Accuracy, Precision, Recall, F1-Score, MSE
- Visuals: Confusion Matrix (heatmap), Classification Report Bar Chart, Salary Distribution

---

## 📈 Model Performance

| Metric     | Score      |
|------------|------------|
| Accuracy   | 98.1%      |
| Precision  | 96.4%      |
| Recall     | 94.1%      |
| F1-Score   | 0.96       |
| MSE        | 1.13       |

> Confusion matrix and classification report plots included in `/visuals`
![image](https://github.com/user-attachments/assets/bae9ae18-ae58-4d71-96a2-3edaf5442d71)

> Actual vs Prediction `/visuals`

![image](https://github.com/user-attachments/assets/67283d38-cb33-4d52-aa99-de05988a05a7)


---

## 🙋‍♂️ Author
Shubham Pandey
3rd year Data Science Student

## 📜 License
This project is licensed under the MIT License — feel free to use and extend

---

## ⭐ If you like this project, don’t forget to star it on GitHub!
