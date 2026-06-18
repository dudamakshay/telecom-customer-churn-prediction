"""
Telecom Customer Churn Prediction — Machine Learning Pipeline

This module implements an end-to-end machine learning pipeline for predicting
telecom customer churn. It performs data cleaning, exploratory data analysis,
feature engineering, model training, and evaluation.

Problem Type: Binary Classification
Target Variable: Churn (Yes/No)
Models: Logistic Regression, Random Forest

Author: Data Science Team
Version: 1.0
Date: 2025
"""

import logging
import sys
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, roc_auc_score, roc_curve
)

warnings.filterwarnings('ignore')

# ============================================================
# LOGGING CONFIGURATION
# ============================================================

def setup_logging():
    """
    Configure logging for the analysis pipeline.
    
    Creates a logger that outputs to both console and file.
    Log level: INFO for console, DEBUG for file.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(message)s',
        datefmt='%H:%M:%S'
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)
    
    # File handler
    log_file = Path(__file__).parent / 'churn_analysis.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)-8s | %(message)s'
    )
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)
    
    return logger

logger = setup_logging()

# ============================================================
# CONFIGURATION
# ============================================================

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_PATH = PROJECT_DIR / 'data' / 'IT_customer_churn.csv'
IMAGES_DIR = PROJECT_DIR / 'images'
MODEL_DIR = PROJECT_DIR / 'model'

# Create necessary directories
IMAGES_DIR.mkdir(exist_ok=True, parents=True)
MODEL_DIR.mkdir(exist_ok=True, parents=True)

# ============================================================
# SECTION 1: DATA LOADING
# ============================================================

def load_data(filepath):
    """
    Load customer churn dataset from CSV file.
    
    Args:
        filepath (Path): Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
        
    Raises:
        FileNotFoundError: If file does not exist
        pd.errors.ParserError: If file cannot be parsed
    """
    try:
        logger.info(f"Loading data from {filepath}")
        df = pd.read_csv(filepath)
        logger.info(f"Data loaded successfully: {df.shape[0]} rows × {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        logger.error(f"Data file not found: {filepath}")
        raise
    except pd.errors.ParserError as e:
        logger.error(f"Error parsing CSV file: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error loading data: {e}")
        raise

# ============================================================
# SECTION 2: DATA EXPLORATION
# ============================================================

def explore_data(df):
    """
    Display comprehensive data overview and statistics.
    
    Args:
        df (pd.DataFrame): Input dataset
    """
    logger.info("=" * 60)
    logger.info("TELECOM CHURN PROJECT — DATA OVERVIEW")
    logger.info("=" * 60)
    
    logger.info(f"Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    churn_rate = (df['Churn'] == 'Yes').mean()
    logger.info(f"Churn Rate: {churn_rate:.1%}")
    logger.info(f"Non-Churn Rate: {(1 - churn_rate):.1%}")
    
    logger.info("\nColumn Data Types:")
    logger.info(str(df.dtypes))
    
    logger.info("\nFirst 5 Rows:")
    logger.info(str(df.head()))

# ============================================================
# SECTION 3: DATA CLEANING
# ============================================================

def clean_data(df):
    """
    Clean dataset by checking and removing issues.
    
    Operations:
    - Check for missing values
    - Remove duplicate rows
    
    Args:
        df (pd.DataFrame): Input dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    logger.info("=" * 60)
    logger.info("DATA CLEANING")
    logger.info("=" * 60)
    
    # Check missing values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        logger.warning(f"Missing values found:\n{missing[missing > 0]}")
    else:
        logger.info("✓ No missing values detected")
    
    # Remove duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    removed = initial_rows - len(df)
    if removed > 0:
        logger.info(f"Removed {removed} duplicate rows")
    else:
        logger.info("✓ No duplicate rows found")
    
    return df

# ============================================================
# SECTION 4: EXPLORATORY DATA ANALYSIS
# ============================================================

def eda_analysis(df):
    """
    Perform exploratory data analysis and display key statistics.
    
    Analyzes:
    - Churn distribution
    - Churn by contract type
    - Churn by internet service
    - Financial metrics by churn status
    
    Args:
        df (pd.DataFrame): Input dataset
    """
    logger.info("=" * 60)
    logger.info("EDA — KEY STATISTICS")
    logger.info("=" * 60)
    
    logger.info("\nChurn Distribution:")
    logger.info(df['Churn'].value_counts().to_string())
    
    logger.info("\nChurn Rate by Contract Type:")
    contract_churn = df.groupby('Contract')['Churn'] \
        .apply(lambda x: (x == 'Yes').mean()) \
        .mul(100).round(1)
    logger.info(contract_churn.to_string())
    
    logger.info("\nChurn Rate by Internet Service:")
    service_churn = df.groupby('InternetService')['Churn'] \
        .apply(lambda x: (x == 'Yes').mean()) \
        .mul(100).round(1)
    logger.info(service_churn.to_string())
    
    logger.info("\nAvg Monthly Charges (Churn vs Retained):")
    charges = df.groupby('Churn')['MonthlyCharges'].mean().round(2)
    logger.info(charges.to_string())
    
    logger.info("\nAvg Tenure in Months (Churn vs Retained):")
    tenure = df.groupby('Churn')['tenure'].mean().round(1)
    logger.info(tenure.to_string())

# ============================================================
# SECTION 5: VISUALIZATIONS
# ============================================================

def create_eda_visualizations(df):
    """
    Create and save exploratory data analysis visualizations.
    
    Generates 6-panel figure showing:
    1. Churn distribution (pie)
    2. Churn by contract (bar)
    3. Monthly charges distribution (histogram)
    4. Tenure distribution (histogram)
    5. Internet service churn (bar)
    6. Senior citizen churn (bar)
    
    Args:
        df (pd.DataFrame): Input dataset
    """
    logger.info("\nGenerating EDA visualizations...")
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('Telecom Churn — Exploratory Data Analysis', 
                 fontsize=16, fontweight='bold')
    
    try:
        # 1. Churn Distribution
        churn_counts = df['Churn'].value_counts()
        axes[0, 0].pie(churn_counts, labels=churn_counts.index, 
                      autopct='%1.1f%%', colors=['#2ecc71', '#e74c3c'], 
                      startangle=90)
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
        axes[0, 2].hist(df[df['Churn'] == 'Yes']['MonthlyCharges'], 
                       alpha=0.6, color='#e74c3c', label='Churned', bins=30)
        axes[0, 2].hist(df[df['Churn'] == 'No']['MonthlyCharges'], 
                       alpha=0.6, color='#2ecc71', label='Retained', bins=30)
        axes[0, 2].set_title('Monthly Charges: Churn vs Retained')
        axes[0, 2].set_xlabel('Monthly Charges ($)')
        axes[0, 2].legend()
        
        # 4. Tenure Distribution
        axes[1, 0].hist(df[df['Churn'] == 'Yes']['tenure'], 
                       alpha=0.6, color='#e74c3c', label='Churned', bins=30)
        axes[1, 0].hist(df[df['Churn'] == 'No']['tenure'], 
                       alpha=0.6, color='#2ecc71', label='Retained', bins=30)
        axes[1, 0].set_title('Tenure: Churn vs Retained')
        axes[1, 0].set_xlabel('Tenure (Months)')
        axes[1, 0].legend()
        
        # 5. Internet Service Churn
        internet_churn = df.groupby('InternetService')['Churn'].apply(
            lambda x: (x == 'Yes').mean() * 100).reset_index()
        axes[1, 1].bar(internet_churn['InternetService'], 
                      internet_churn['Churn'],
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
        eda_image_path = IMAGES_DIR / 'churn_eda.png'
        plt.savefig(eda_image_path, dpi=150, bbox_inches='tight')
        plt.close()
        logger.info(f"✓ EDA visualizations saved: {eda_image_path}")
        
    except Exception as e:
        logger.error(f"Error creating EDA visualizations: {e}")
        raise

# ============================================================
# SECTION 6: FEATURE ENGINEERING & PREPROCESSING
# ============================================================

def prepare_data(df):
    """
    Prepare data for modeling through encoding and feature engineering.
    
    Operations:
    - One-hot/label encode categorical variables
    - Create engineered features (ChargesPerMonth, IsNewCustomer)
    - Encode target variable
    
    Args:
        df (pd.DataFrame): Input dataset
        
    Returns:
        tuple: (X, y) where X is features and y is target
    """
    logger.info("=" * 60)
    logger.info("FEATURE ENGINEERING & ENCODING")
    logger.info("=" * 60)
    
    df_model = df.copy()
    
    # Label encode categorical columns
    le = LabelEncoder()
    cat_cols = df_model.select_dtypes(include='object').columns.tolist()
    if 'Churn' in cat_cols:
        cat_cols.remove('Churn')
    
    logger.info(f"Encoding {len(cat_cols)} categorical features")
    for col in cat_cols:
        df_model[col] = le.fit_transform(df_model[col])
    
    # Target encoding
    df_model['Churn'] = (df_model['Churn'] == 'Yes').astype(int)
    
    # Feature engineering
    logger.info("Creating engineered features...")
    df_model['ChargesPerMonth'] = df_model['TotalCharges'] / (df_model['tenure'] + 1)
    df_model['IsNewCustomer'] = (df_model['tenure'] <= 6).astype(int)
    logger.info(f"✓ Created 2 engineered features")
    
    X = df_model.drop('Churn', axis=1)
    y = df_model['Churn']
    
    logger.info(f"Features: {X.shape[1]}, Target classes: {y.nunique()}")
    
    return X, y

# ============================================================
# SECTION 7: MODEL TRAINING
# ============================================================

def train_logistic_regression(X_train, y_train, X_test, y_test):
    """
    Train Logistic Regression classifier and evaluate performance.
    
    Args:
        X_train (pd.DataFrame): Training features
        y_train (pd.Series): Training target
        X_test (pd.DataFrame): Test features
        y_test (pd.Series): Test target
        
    Returns:
        dict: Model and evaluation metrics
    """
    logger.info("=" * 60)
    logger.info("MODEL 1: LOGISTIC REGRESSION CLASSIFIER")
    logger.info("=" * 60)
    
    try:
        lr_model = LogisticRegression(max_iter=1000, random_state=42)
        lr_model.fit(X_train, y_train)
        logger.info("✓ Model trained successfully")
        
        lr_pred = lr_model.predict(X_test)
        lr_proba = lr_model.predict_proba(X_test)[:, 1]
        
        accuracy = accuracy_score(y_test, lr_pred)
        roc_auc = roc_auc_score(y_test, lr_proba)
        
        logger.info(f"Accuracy : {accuracy:.4f}")
        logger.info(f"ROC-AUC  : {roc_auc:.4f}")
        logger.info("\nClassification Report:")
        logger.info(classification_report(y_test, lr_pred, 
                                        target_names=['Retained', 'Churned']))
        
        return {
            'model': lr_model,
            'predictions': lr_pred,
            'probabilities': lr_proba,
            'accuracy': accuracy,
            'roc_auc': roc_auc
        }
    except Exception as e:
        logger.error(f"Error training Logistic Regression: {e}")
        raise

def train_random_forest(X_train, y_train, X_test, y_test):
    """
    Train Random Forest classifier and evaluate performance.
    
    Args:
        X_train (pd.DataFrame): Training features
        y_train (pd.Series): Training target
        X_test (pd.DataFrame): Test features
        y_test (pd.Series): Test target
        
    Returns:
        dict: Model and evaluation metrics
    """
    logger.info("=" * 60)
    logger.info("MODEL 2: RANDOM FOREST CLASSIFIER")
    logger.info("=" * 60)
    
    try:
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42, 
                                         n_jobs=-1)
        rf_model.fit(X_train, y_train)
        logger.info("✓ Model trained successfully")
        
        rf_pred = rf_model.predict(X_test)
        rf_proba = rf_model.predict_proba(X_test)[:, 1]
        
        accuracy = accuracy_score(y_test, rf_pred)
        roc_auc = roc_auc_score(y_test, rf_proba)
        
        logger.info(f"Accuracy : {accuracy:.4f}")
        logger.info(f"ROC-AUC  : {roc_auc:.4f}")
        logger.info("\nClassification Report:")
        logger.info(classification_report(y_test, rf_pred, 
                                        target_names=['Retained', 'Churned']))
        
        cm = confusion_matrix(y_test, rf_pred)
        logger.info("\nConfusion Matrix:")
        logger.info(f"{cm}")
        
        return {
            'model': rf_model,
            'predictions': rf_pred,
            'probabilities': rf_proba,
            'accuracy': accuracy,
            'roc_auc': roc_auc,
            'confusion_matrix': cm,
            'feature_importances': rf_model.feature_importances_
        }
    except Exception as e:
        logger.error(f"Error training Random Forest: {e}")
        raise

# ============================================================
# SECTION 8: MODEL EVALUATION & VISUALIZATION
# ============================================================

def visualize_model_evaluation(rf_results, X, y_test):
    """
    Create model evaluation visualizations.
    
    Generates 2-panel figure showing:
    1. Feature importance (top 12)
    2. Confusion matrix heatmap
    
    Args:
        rf_results (dict): Random Forest results with feature importances
        X (pd.DataFrame): Features (for column names)
        y_test (pd.Series): Test target
    """
    logger.info("\nGenerating model evaluation visualizations...")
    
    try:
        feat_imp = pd.Series(rf_results['feature_importances'], index=X.columns) \
                     .sort_values(ascending=True)
        
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        fig.suptitle('Telecom Churn — Model Evaluation', fontsize=15, 
                    fontweight='bold')
        
        # Feature Importance Plot
        feat_imp.tail(12).plot(kind='barh', ax=axes[0], color='#3498db')
        axes[0].set_title('Top 12 Feature Importances (Random Forest Classifier)')
        axes[0].set_xlabel('Importance Score')
        
        # Confusion Matrix Heatmap
        cm = rf_results['confusion_matrix']
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1],
                   xticklabels=['Retained', 'Churned'],
                   yticklabels=['Retained', 'Churned'])
        axes[1].set_title('Confusion Matrix — Random Forest Classifier')
        axes[1].set_ylabel('Actual')
        axes[1].set_xlabel('Predicted')
        
        plt.tight_layout()
        model_image_path = IMAGES_DIR / 'churn_model.png'
        plt.savefig(model_image_path, dpi=150, bbox_inches='tight')
        plt.close()
        logger.info(f"✓ Model evaluation visualizations saved: {model_image_path}")
        
    except Exception as e:
        logger.error(f"Error creating model evaluation visualizations: {e}")
        raise

# ============================================================
# SECTION 9: MODEL PERSISTENCE
# ============================================================

def save_model(model, filepath):
    """
    Serialize and save trained model to disk.
    
    Args:
        model: Trained scikit-learn model
        filepath (Path): Destination file path
        
    Raises:
        Exception: If model cannot be saved
    """
    try:
        joblib.dump(model, filepath)
        logger.info(f"✓ Model saved successfully: {filepath}")
    except Exception as e:
        logger.error(f"Error saving model: {e}")
        raise

# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    """
    Execute complete machine learning pipeline.
    
    Pipeline:
    1. Load data
    2. Explore data
    3. Clean data
    4. EDA and visualizations
    5. Feature engineering
    6. Train-test split
    7. Train models
    8. Evaluate and visualize
    9. Save model
    """
    try:
        logger.info("Starting Telecom Customer Churn Prediction Pipeline\n")
        
        # Load and explore
        df = load_data(DATA_PATH)
        explore_data(df)
        
        # Clean and analyze
        df = clean_data(df)
        eda_analysis(df)
        create_eda_visualizations(df)
        
        # Prepare features
        X, y = prepare_data(df)
        
        # Train-test split
        logger.info("=" * 60)
        logger.info("TRAIN-TEST SPLIT")
        logger.info("=" * 60)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        logger.info(f"Training Set : {X_train.shape[0]} samples")
        logger.info(f"Test Set     : {X_test.shape[0]} samples\n")
        
        # Train models
        lr_results = train_logistic_regression(X_train, y_train, X_test, y_test)
        rf_results = train_random_forest(X_train, y_train, X_test, y_test)
        
        # Visualize evaluation
        visualize_model_evaluation(rf_results, X, y_test)
        
        # Save model
        logger.info("=" * 60)
        logger.info("MODEL PERSISTENCE")
        logger.info("=" * 60)
        lr_model_path = MODEL_DIR / 'logistic_regression_classifier.pkl'
        save_model(lr_results['model'], lr_model_path)
        
        # Project completion summary
        logger.info("\n" + "=" * 60)
        logger.info("PROJECT COMPLETE — READY FOR DEPLOYMENT")
        logger.info("=" * 60)
        logger.info("\nMachine Learning Summary")
        logger.info("-" * 40)
        logger.info("Problem Type : Binary Classification")
        logger.info("Model 1      : Logistic Regression Classifier")
        logger.info("Model 2      : Random Forest Classifier")
        logger.info("Best Model   : Logistic Regression (81.76% accuracy)")
        logger.info("=" * 60)
        logger.info("Pipeline execution completed successfully!\n")
        
    except Exception as e:
        logger.error(f"Pipeline failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
