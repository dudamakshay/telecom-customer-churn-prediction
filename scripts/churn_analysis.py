# ============================================================
# TELECOM CUSTOMER CHURN PREDICTION
# Machine Learning Problem Type: Binary Classification
# Target Variable: Churn (Yes/No)
# Models Used:
# 1. Logistic Regression Classifier
# 2. Random Forest Classifier
# Company: TelecomCorp Analytics Team
# Author: Senior Data Scientist
# Version: 1.0  |  Date: 2025
# ============================================================

# ─────────────────────────────────────────
# SECTION 1: IMPORT LIBRARIES
# ─────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, roc_auc_score, roc_curve
)

# ─────────────────────────────────────────
# SECTION 2: LOAD DATA
# ─────────────────────────────────────────
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(BASE_DIR, 'data', 'IT_customer_churn.csv')

df = pd.read_csv(data_path)

print("=" * 60)
print("TELECOM CHURN PROJECT — DATA OVERVIEW")
print("=" * 60)
print(f"Dataset Shape    : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Churn Rate       : {(df['Churn'] == 'Yes').mean():.1%}")
print(f"Non-Churn Rate   : {(df['Churn'] == 'No').mean():.1%}")
print("\nColumn List:")
print(df.dtypes)
print("\nFirst 5 Rows:")
print(df.head())

# ─────────────────────────────────────────
# SECTION 3: DATA CLEANING
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
print(f"\nDuplicates removed: {before - len(df)}")

# ─────────────────────────────────────────
# SECTION 4: EXPLORATORY DATA ANALYSIS (EDA)
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("EDA — KEY STATISTICS")
print("=" * 60)

print("\nChurn Distribution:")
print(df['Churn'].value_counts())

print("\nChurn Rate by Contract Type:")
print(df.groupby('Contract')['Churn']
      .apply(lambda x: (x == 'Yes').mean())
      .mul(100).round(1)
      .rename('Churn%'))

print("\nChurn Rate by Internet Service:")
print(df.groupby('InternetService')['Churn']
      .apply(lambda x: (x == 'Yes').mean())
      .mul(100).round(1)
      .rename('Churn%'))

print("\nAvg Monthly Charges (Churn vs No-Churn):")
print(df.groupby('Churn')['MonthlyCharges'].mean().round(2))

print("\nAvg Tenure in Months (Churn vs No-Churn):")
print(df.groupby('Churn')['tenure'].mean().round(1))

# ─────────────────────────────────────────
# SECTION 5: VISUALIZATIONS
# ─────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Telecom Churn — Exploratory Data Analysis', fontsize=16, fontweight='bold')

# 1. Churn Distribution
churn_counts = df['Churn'].value_counts()
axes[0, 0].pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%',
               colors=['#2ecc71', '#e74c3c'], startangle=90)
axes[0, 0].set_title('Churn Distribution')

# 2. Churn by Contract
contract_churn = df.groupby('Contract')['Churn'].apply(
    lambda x: (x == 'Yes').mean() * 100).reset_index()
axes[0, 1].bar(contract_churn['Contract'], contract_churn['Churn'],
               color=['#3498db', '#e67e22', '#2ecc71'])
axes[0, 1].set_title('Churn Rate by Contract Type')
axes[0, 1].set_ylabel('Churn Rate (%)')
axes[0, 1].tick_params(axis='x', rotation=15)

# 3. Monthly Charges Distribution
axes[0, 2].hist(df[df['Churn'] == 'Yes']['MonthlyCharges'], alpha=0.6,
                color='#e74c3c', label='Churned', bins=30)
axes[0, 2].hist(df[df['Churn'] == 'No']['MonthlyCharges'], alpha=0.6,
                color='#2ecc71', label='Retained', bins=30)
axes[0, 2].set_title('Monthly Charges: Churn vs Retained')
axes[0, 2].set_xlabel('Monthly Charges ($)')
axes[0, 2].legend()

# 4. Tenure Distribution
axes[1, 0].hist(df[df['Churn'] == 'Yes']['tenure'], alpha=0.6,
                color='#e74c3c', label='Churned', bins=30)
axes[1, 0].hist(df[df['Churn'] == 'No']['tenure'], alpha=0.6,
                color='#2ecc71', label='Retained', bins=30)
axes[1, 0].set_title('Tenure: Churn vs Retained')
axes[1, 0].set_xlabel('Tenure (Months)')
axes[1, 0].legend()

# 5. Internet Service Churn
internet_churn = df.groupby('InternetService')['Churn'].apply(
    lambda x: (x == 'Yes').mean() * 100).reset_index()
axes[1, 1].bar(internet_churn['InternetService'], internet_churn['Churn'],
               color=['#9b59b6', '#3498db', '#e74c3c'])
axes[1, 1].set_title('Churn Rate by Internet Service')
axes[1, 1].set_ylabel('Churn Rate (%)')

# 6. Senior Citizen Churn
senior_churn = df.groupby('SeniorCitizen')['Churn'].apply(
    lambda x: (x == 'Yes').mean() * 100).reset_index()
axes[1, 2].bar(['Non-Senior', 'Senior'], senior_churn['Churn'],
               color=['#2ecc71', '#e74c3c'])
axes[1, 2].set_title('Churn Rate by Senior Citizen Status')
axes[1, 2].set_ylabel('Churn Rate (%)')

plt.tight_layout()
plt.savefig('churn_eda.png', dpi=150, bbox_inches='tight')
plt.show()
print("EDA chart saved: churn_eda.png")

# ─────────────────────────────────────────
# SECTION 6: ENCODING & FEATURE ENGINEERING
# ─────────────────────────────────────────
df_model = df.copy()

# Label Encode all categorical columns
le = LabelEncoder()
cat_cols = df_model.select_dtypes(include='object').columns.tolist()
cat_cols.remove('Churn')

for col in cat_cols:
    df_model[col] = le.fit_transform(df_model[col])

# Target encoding
df_model['Churn'] = (df_model['Churn'] == 'Yes').astype(int)

# Feature engineering
df_model['ChargesPerMonth'] = df_model['TotalCharges'] / (df_model['tenure'] + 1)
df_model['IsNewCustomer'] = (df_model['tenure'] <= 6).astype(int)

X = df_model.drop('Churn', axis=1)
y = df_model['Churn']

# ─────────────────────────────────────────
# SECTION 7: TRAIN-TEST SPLIT
# ─────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\nTraining Set : {X_train.shape[0]} samples")
print(f"Test Set     : {X_test.shape[0]} samples")

# ─────────────────────────────────────────
## SECTION 8: MODEL 1 — LOGISTIC REGRESSION CLASSIFIER
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("MODEL 1: LOGISTIC REGRESSION CLASSIFIER")
print("=" * 60)
# Classification Model
# Algorithm: Logistic Regression Classifier
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_proba = lr_model.predict_proba(X_test)[:, 1]

print(f"Accuracy : {accuracy_score(y_test, lr_pred):.4f}")
print(f"ROC-AUC  : {roc_auc_score(y_test, lr_proba):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, lr_pred, target_names=['Retained', 'Churned']))

# ─────────────────────────────────────────
# SECTION 9: MODEL 2 — RANDOM FOREST
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print("MODEL 2: RANDOM FOREST CLASSIFIER")
print("=" * 60)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_proba = rf_model.predict_proba(X_test)[:, 1]

print(f"Accuracy : {accuracy_score(y_test, rf_pred):.4f}")
print(f"ROC-AUC  : {roc_auc_score(y_test, rf_proba):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, rf_pred, target_names=['Retained', 'Churned']))

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, rf_pred)
print(cm)

# ─────────────────────────────────────────
# Feature Importance (Random Forest Classifier)
# ─────────────────────────────────────────
feat_imp = pd.Series(rf_model.feature_importances_, index=X.columns) \
             .sort_values(ascending=True)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Telecom Churn — Model Evaluation', fontsize=15, fontweight='bold')

# Feature Importance Plot
feat_imp.tail(12).plot(kind='barh', ax=axes[0], color='#3498db')
axes[0].set_title('Top 12 Feature Importances (Random Forest Classifier)')
axes[0].set_xlabel('Importance Score')

# Confusion Matrix Heatmap
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1],
            xticklabels=['Retained', 'Churned'],
            yticklabels=['Retained', 'Churned'])
axes[1].set_title('Confusion Matrix — Random Forest Classifier')
axes[1].set_ylabel('Actual')
axes[1].set_xlabel('Predicted')

plt.tight_layout()
plt.savefig('churn_model.png', dpi=150, bbox_inches='tight')
plt.show()
print("Model chart saved: churn_model.png")

print("\n" + "=" * 60)
print("PROJECT COMPLETE — READY FOR DEPLOYMENT")
print("\nMachine Learning Summary")
print("-" * 40)
print("Problem Type : Binary Classification")
print("Model 1      : Logistic Regression Classifier")
print("Model 2      : Random Forest Classifier")
print("=" * 60)

import os
import joblib

# Ensure model folder exists
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(lr_model, "model/logistic_regression_classifier.pkl")

print("Model saved successfully in model/churn_model.pkl")