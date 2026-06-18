# 📦 Installation & Setup Guide

Complete step-by-step instructions to set up and run the Telecom Customer Churn Prediction project.

---

## ✅ System Requirements

### 1. **Python**
- **Minimum Version:** Python 3.9+
- **Recommended:** Python 3.10 or 3.11
- **Check your version:**
  ```bash
  python --version
  ```

### 2. **Git** (Optional but Recommended)
- Required to clone the repository
- [Download Git](https://git-scm.com/downloads)
- **Check your version:**
  ```bash
  git --version
  ```

### 3. **Power BI Desktop** (Optional)
- Required to view the interactive dashboard
- [Download Power BI Desktop](https://powerbi.microsoft.com/en-us/downloads/)
- Windows 7 Service Pack 1 or newer required

### 4. **Text Editor or IDE** (Optional)
- **Recommended:** VS Code, PyCharm, or Jupyter
- [Download VS Code](https://code.visualstudio.com/)

---

## 🚀 Installation Steps

### **Step 1: Clone the Repository**

```bash
# Using Git
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction

# OR download as ZIP and extract manually
```

### **Step 2: Create a Virtual Environment**

A virtual environment isolates project dependencies and prevents conflicts.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Expected output:** Your terminal shows `(venv)` prefix, indicating the virtual environment is active.

### **Step 3: Upgrade pip**

```bash
python -m pip install --upgrade pip
```

### **Step 4: Install Required Packages**

```bash
pip install -r requirements.txt
```

**This installs:**
- pandas (data processing)
- numpy (numerical computing)
- scikit-learn (machine learning)
- matplotlib & seaborn (visualization)
- plotly (interactive charts)
- jupyter (notebook environment)
- joblib (model serialization)

**Installation time:** ~2-3 minutes on a standard internet connection

### **Step 5: Verify Installation**

```bash
python -c "import pandas, numpy, sklearn; print('✅ All packages installed successfully!')"
```

---

## 📂 Repository Structure

```
customer-churn-prediction/
│
├── data/
│   └── IT_customer_churn.csv          # Main dataset (7,043 customer records)
│
├── scripts/
│   └── churn_analysis.py              # Main ML pipeline (executable Python script)
│
├── notebooks/
│   └── customer_churn_analysis.ipynb  # Interactive Jupyter notebook
│
├── sql/
│   └── advanced_churn_queries.sql     # Advanced SQL analytics and segmentation
│
├── model/
│   └── logistic_regression_classifier.pkl  # Trained ML model (binary classifier)
│
├── images/
│   ├── churn_eda.png                  # EDA visualization (6 subplots)
│   └── churn_model.png                # Model evaluation and feature importance
│
├── dashboard/
│   ├── Telecom Customer Churn Dashboard.pbix  # Interactive Power BI dashboard
│   └── dashboard preview.png          # Dashboard screenshot
│
├── presentation/
│   ├── customer_churn_presentation.pptx  # Business presentation slides
│   └── README.md                      # Presentation documentation
│
├── docs/
│   ├── INSTALL.md                     # Installation guide (this file)
│   ├── DATA_DICTIONARY.md             # Dataset column documentation
│   ├── MODEL_CARD.md                  # Model documentation and limitations
│   └── README.md                      # Docs index
│
├── requirements.txt                   # Python package dependencies with versions
├── .gitignore                         # Git ignore rules
└── README.md                          # Main project documentation
```

---

## ▶️ Running the Project

### **Option 1: Run Python Script** (Recommended for quick execution)

```bash
cd scripts
python churn_analysis.py
```

**What happens:**
1. Loads 7,043 customer records from `data/IT_customer_churn.csv`
2. Performs data cleaning (removes duplicates, handles missing values)
3. Executes exploratory data analysis
4. Trains Logistic Regression and Random Forest classifiers
5. Evaluates model performance
6. Saves visualizations to `images/` folder
7. Saves trained model to `model/` folder

**Expected Runtime:** 2-3 minutes

**Output files created:**
- `../images/churn_eda.png` — EDA visualizations
- `../images/churn_model.png` — Feature importance and confusion matrix
- `../model/logistic_regression_classifier.pkl` — Trained model

**Expected console output:**
```
============================================================
TELECOM CHURN PROJECT — DATA OVERVIEW
============================================================
Dataset Shape    : 7043 rows × 20 columns
Churn Rate       : 26.5%
Non-Churn Rate   : 73.5%
...
============================================================
MODEL 1: LOGISTIC REGRESSION CLASSIFIER
============================================================
Accuracy : 0.8176
ROC-AUC  : 0.8500
...
```

### **Option 2: Run Jupyter Notebook** (Recommended for exploration and learning)

```bash
cd notebooks
jupyter notebook customer_churn_analysis.ipynb
```

**What happens:**
1. Jupyter opens in your browser (usually http://localhost:8888)
2. You can execute cells individually or use "Run All"
3. See code, outputs, and visualizations interactively
4. Modify and re-run cells as needed

**How to use:**
- Click ▶️ to run individual cells
- Click ⏩ (Run All) to execute entire notebook
- Outputs appear below each cell

### **Option 3: Explore SQL Queries** (For database analysts)

1. Install a SQL client:
   - **PostgreSQL:** psql
   - **MySQL:** MySQL Workbench
   - **SQL Server:** SQL Server Management Studio

2. Open `sql/advanced_churn_queries.sql` in your SQL client

3. Execute queries to analyze:
   - Revenue impact
   - Customer segmentation
   - Churn risk scoring
   - Tenure-based trends

### **Option 4: Open Power BI Dashboard** (For business intelligence)

1. Install **Power BI Desktop** (Windows only)
2. Open `dashboard/Telecom Customer Churn Dashboard.pbix`
3. Explore interactive visualizations:
   - Churn rate by contract type
   - Revenue impact analysis
   - Customer risk segmentation
   - Payment method insights

---

## ✅ Expected Outputs

### **Console Output (from Python script)**

```text
============================================================
TELECOM CHURN PROJECT — DATA OVERVIEW
============================================================
Dataset Shape    : 7043 rows × 20 columns
Churn Rate       : 26.5%
Non-Churn Rate   : 73.5%

Column List:
[Shows all 20 column data types]

First 5 Rows:
[Sample of first 5 customers]

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

Churn Rate by Contract Type:
Contract            Churn%
Month-to-month      42.7%
One year            11.3%
Two year            2.8%

Average Monthly Charges (Churn vs Retained):
Churn    74.44
No      61.27

Average Tenure (Churn vs Retained):
Churn     17.98
No       37.57

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

[Similar classification report...]

EDA chart saved: ../images/churn_eda.png
Model chart saved: ../images/churn_model.png

============================================================
PROJECT COMPLETE — READY FOR DEPLOYMENT
============================================================
Model saved successfully: ../model/logistic_regression_classifier.pkl
```

### **Generated Files**

| File | Location | Size | Purpose |
|------|----------|------|---------|
| `churn_eda.png` | `images/` | ~200 KB | 6-panel exploratory data analysis |
| `churn_model.png` | `images/` | ~180 KB | Feature importance & confusion matrix |
| `logistic_regression_classifier.pkl` | `model/` | ~50 KB | Trained ML model for predictions |

---

## 🔧 Troubleshooting

### **Issue: "Python not found"**
- **Solution:** Ensure Python is installed and added to PATH
  ```bash
  python --version
  ```

### **Issue: "No module named 'pandas'"**
- **Solution:** Activate virtual environment and reinstall requirements
  ```bash
  venv\Scripts\activate  # Windows
  pip install -r requirements.txt
  ```

### **Issue: "FileNotFoundError: data/IT_customer_churn.csv"**
- **Solution:** Ensure working directory is the project root
  ```bash
  cd c:\Users\cwmbn\Downloads\customer-churn-prediction
  python scripts/churn_analysis.py
  ```

### **Issue: Jupyter won't start**
- **Solution:** Reinstall jupyter
  ```bash
  pip install --upgrade jupyter
  jupyter notebook
  ```

### **Issue: Power BI file won't open**
- **Solution:** Ensure Power BI Desktop is installed (Windows only)
- **Alternative:** View `dashboard/dashboard preview.png` for a screenshot

### **Issue: "Permission denied" on macOS/Linux**
- **Solution:** Make script executable
  ```bash
  chmod +x scripts/churn_analysis.py
  ```

---

## 📚 Next Steps

1. **Run the Python script** to see data analysis and model training
2. **Open the Jupyter notebook** for interactive exploration
3. **Review the Power BI dashboard** for business intelligence insights
4. **Read the main README** for project context and findings
5. **Check DATA_DICTIONARY.md** to understand each feature
6. **Review MODEL_CARD.md** for model details and limitations

---

## ❓ Need Help?

- **Installation issues:** Check Python version and virtual environment
- **Missing packages:** Run `pip install -r requirements.txt` again
- **Data file missing:** Ensure `data/IT_customer_churn.csv` exists
- **Git clone failed:** Check internet connection and repository URL

---

**Installation verified:** You're ready to run the project! 🎉
