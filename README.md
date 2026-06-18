# 📡 Telecom Customer Churn Prediction
### End-to-End Data Analytics & Machine Learning Portfolio Project

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Advanced-336791?style=flat&logo=postgresql&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-MachineLearning-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat&logo=powerbi&logoColor=black)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)

---

# 📌 Project Overview

Customer churn is one of the most critical business challenges in the telecom industry. This project analyzes telecom customer behavior and builds machine learning models to identify customers at high risk of churn before they leave.

The project combines:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL Analytics
- Machine Learning Classification
- Power BI Dashboarding
- Business Insights & Recommendations

---

# 🚀 Quick Start

## Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd customer-churn-prediction
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

All required packages with pinned versions will be installed automatically.

---

# 📁 Project Structure

```
customer-churn-prediction/
│
├── data/
│   └── IT_customer_churn.csv          # Raw customer data (7,043 records)
│
├── scripts/
│   └── churn_analysis.py              # Main ML pipeline (Python script)
│
├── notebooks/
│   └── customer_churn_analysis.ipynb  # Interactive Jupyter notebook
│
├── sql/
│   └── advanced_churn_queries.sql     # Advanced SQL analytics queries
│
├── model/
│   └── logistic_regression_classifier.pkl  # Trained ML model
│
├── images/
│   ├── churn_eda.png                  # EDA visualizations
│   └── churn_model.png                # Model evaluation charts
│
├── dashboard/
│   ├── Telecom Customer Churn Dashboard.pbix  # Power BI dashboard
│   └── dashboard preview.png          # Dashboard screenshot
│
├── presentation/
│   └── customer_churn_presentation.pptx  # Business presentation
│
├── requirements.txt                    # Python dependencies
├── .gitignore                         # Git ignore rules
└── README.md                          # This file
```

---

# 🏃 How to Run

### Option 1: Run Python Script (Recommended for Quick Results)
```bash
cd scripts
python churn_analysis.py
```

**Expected Runtime:** ~2-3 minutes

**Outputs Generated:**
- Console output with data overview and model metrics
- `../images/churn_eda.png` — EDA visualizations
- `../images/churn_model.png` — Model evaluation and confusion matrix
- `../model/logistic_regression_classifier.pkl` — Trained model

### Option 2: Run Jupyter Notebook (Recommended for Exploration)
```bash
cd notebooks
jupyter notebook customer_churn_analysis.ipynb
```

Then click "Run All" or execute cells sequentially to see:
- Data loading and cleaning steps
- Exploratory data analysis
- Model training and evaluation
- Interactive visualizations

### Option 3: Explore SQL Queries (For Analytics)
Open `sql/advanced_churn_queries.sql` in your database tool (PostgreSQL, MySQL, or SQL Server) to run advanced analytics queries for:
- Revenue impact analysis
- Window function calculations
- Customer segmentation
- Risk scoring

---

# 📊 Expected Outputs

## Console Output
```
============================================================
TELECOM CHURN PROJECT — DATA OVERVIEW
============================================================
Dataset Shape    : 7043 rows × 20 columns
Churn Rate       : 26.5%
Non-Churn Rate   : 73.5%

Column List:
[Data types for all 20 features]

============================================================
DATA CLEANING
============================================================
Missing Values: None
Duplicates removed: 0

============================================================
EDA — KEY STATISTICS
============================================================
Churn Distribution:
No     5174
Yes    1869
Name: Churn, dtype: int64

[Additional EDA statistics...]

============================================================
MODEL 1: LOGISTIC REGRESSION CLASSIFIER
============================================================
Accuracy : 0.8176
ROC-AUC  : 0.8500

Classification Report:
              precision    recall  f1-score   support
    Retained       0.85      0.93      0.89      1048
     Churned       0.71      0.52      0.60       400
    accuracy                           0.82      1448
   macro avg       0.78      0.73      0.74      1448
weighted avg       0.82      0.82      0.81      1448

============================================================
MODEL 2: RANDOM FOREST CLASSIFIER
============================================================
Accuracy : 0.7984
ROC-AUC  : 0.8300

[Full classification report...]

============================================================
PROJECT COMPLETE — READY FOR DEPLOYMENT
============================================================
```

## Generated Files

| File | Location | Purpose |
|---|---|---|
| `churn_eda.png` | `images/` | 6-panel EDA visualization |
| `churn_model.png` | `images/` | Feature importance & confusion matrix |
| `logistic_regression_classifier.pkl` | `model/` | Serialized ML model for predictions |

---

# 🎯 Business Problem

Telecom companies lose significant revenue when customers discontinue services. Early identification of high-risk customers enables retention teams to take proactive actions such as:

- Personalized retention offers
- Contract conversion strategies
- Loyalty incentives
- Service quality improvements

---

# 📊 Key Results

| Metric | Value |
|---|---|
| Dataset Size | 7,043 Customers |
| Features | 20 |
| Churn Rate | 26.5% |
| Monthly Revenue at Risk | $139,131 |
| Annual Revenue at Risk | $1.67M |
| Best Performing Model | Logistic Regression Classifier |
| Model Accuracy | 81.76% |
| ROC-AUC Score | 0.85 |

---

# 🔍 Key Business Insights

| Finding | Churn Rate | Business Impact |
|---|---|---|
| Month-to-month contracts | 42.7% | High churn risk |
| Fiber optic customers | 41.9% | Premium customer churn |
| Electronic check users | 45.3% | Payment-related churn |
| New customers (0–6 months) | 53.3% | Early-stage retention problem |
| Two-year contracts | 2.8% | Strong retention segment |

---

# 🛠️ Technologies Used

| Category | Tools & Libraries |
|---|---|
| Programming | Python |
| Data Analysis | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Machine Learning | scikit-learn |
| Dashboarding | Power BI |
| Database Querying | SQL |
| Notebook Workflow | Jupyter Notebook |
| Version Control | Git & GitHub |

---

# 🤖 Machine Learning Models

## Problem Type
Binary Classification

## Models Implemented

- Logistic Regression Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

---

# 📈 Model Performance

| Model | Accuracy | ROC-AUC | Purpose |
|---|---|---|---|
| Logistic Regression Classifier | 81.76% | 0.85 | Best explainability |
| Random Forest Classifier | 79.84% | 0.83 | Feature importance analysis |
| Gradient Boosting Classifier | 80.12% | 0.84 | Performance optimization |

---

# 📌 Top Churn Drivers

The Random Forest Classifier identified the following key churn factors:

1. Monthly Charges
2. Tenure
3. Total Charges
4. Contract Type
5. Payment Method

---

# 📊 Exploratory Data Analysis

The project includes detailed exploratory data analysis to identify customer churn patterns and business trends.

## Analysis Performed

- Churn distribution analysis
- Contract type analysis
- Tenure segmentation
- Internet service comparison
- Payment method analysis
- Correlation analysis
- Revenue loss estimation

---

# 📊 Power BI Dashboard

The Power BI dashboard provides interactive business intelligence visualizations for churn monitoring and decision-making.

## Dashboard Features

- KPI Cards
- Churn Rate Analysis
- Revenue at Risk
- Contract Type Segmentation
- Customer Risk Analysis
- Retention Insights

---

# 📂 Project Structure

```text
customer-churn-prediction/
│
├── data/
├── images/
├── model/
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
├── powerbi/
│   └── customer_churn_dashboard.pbix
│
├── scripts/
│   └── churn_analysis.py
│
├── sql/
│   └── advanced_churn_queries.sql
│
├── README.md
├── requirements.txt
└── customer_churn_presentation.pptx
```

---

# 📓 Jupyter Notebook Workflow

The project notebook includes:

- Data preprocessing
- EDA visualizations
- Feature engineering
- ML model training
- Model evaluation
- Business insights
- Recommendations

Notebook:
```text
notebooks/customer_churn_analysis.ipynb
```

---

# 📈 SQL Analysis Highlights

Advanced SQL analysis includes:

- Customer segmentation
- Revenue analysis
- Churn risk categorization
- Window functions
- Trend analysis
- Retention-focused queries

---

# 💼 Business Recommendations

1. Encourage long-term contracts through retention discounts.
2. Improve onboarding for new customers during the first 90 days.
3. Provide loyalty incentives for high-risk customers.
4. Improve service quality for fiber optic users.
5. Promote auto-pay methods to reduce churn probability.

---

# 🎯 Using the Trained Model

The trained Logistic Regression model is saved as `model/logistic_regression_classifier.pkl` and can be loaded for predictions.

### Load and Make Predictions

```python
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model/logistic_regression_classifier.pkl')

# Prepare your customer data (must match training features)
# Example: customer_data should have all 20 features used in training
customer_data = pd.read_csv('new_customers.csv')

# Make predictions
predictions = model.predict(customer_data)
probabilities = model.predict_proba(customer_data)

# Get churn probability for each customer
churn_probability = probabilities[:, 1]

print(f"Predicted churn: {predictions}")
print(f"Churn probability: {churn_probability}")
```

### Model Input Features

The model expects 20 features matching the training dataset:
- Customer demographics (age, gender, etc.)
- Service information (internet type, contract, tenure)
- Financial metrics (monthly charges, total charges)
- Service add-ons (tech support, online security, etc.)
- Payment information (payment method)

---

# 📝 Resume Project Summary

- Built an end-to-end telecom customer churn prediction system using Python, SQL, Machine Learning, and Power BI.
- Performed exploratory data analysis and customer segmentation on 7,043 telecom customers.
- Developed classification models achieving 81.76% accuracy with ROC-AUC score of 0.85.
- Identified high-risk churn segments causing approximately $1.67M annual revenue loss.
- Created interactive Power BI dashboard for business intelligence and retention analysis.

---

# 👤 Author

**Dudam Akshay**  
Data Analyst | Data Science Enthusiast

- GitHub: https://github.com/dudamakshay
- LinkedIn: https://www.linkedin.com/in/dudamakshay

---

⭐ If you found this project useful, consider starring the repository.