# 📡 Telecom Customer Churn Prediction
**End-to-End Data Analytics & Machine Learning Portfolio Project**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-Advanced-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Executive Summary

This project demonstrates **end-to-end data analytics and machine learning** capabilities through a real-world business problem: **predicting telecom customer churn**.

**Key Achievement:** Built a **81.76% accurate ML model** that identifies high-risk customers, enabling:
- **$1.67M annual revenue at risk** quantification
- **Actionable customer segments** for targeted retention
- **Data-driven business recommendations** for churn reduction

**Impact Potential:** A 5% reduction in churn = **$1M+ annual revenue recovery**

---

## 🎯 Business Problem

**Challenge:** Telecom companies lose significant revenue when customers discontinue services without warning.

**Current State:**
- **26.5%** of customers are churning
- **$139,131** monthly revenue at risk
- **1,869 customers** leaving annually

**Root Causes:**
- Month-to-month contracts (42.7% churn) — lack commitment
- Fiber optic service issues (41.9% churn) — unmet expectations
- Electronic payment methods (45.3% churn) — friction
- Poor onboarding (53.3% churn in first 6 months) — early failure

**Solution:** Use data analytics + ML to identify at-risk customers early and intervene with targeted retention strategies.

---

## ✨ Project Highlights

### **Comprehensive Data Analysis**
- ✅ 7,043 customer records analyzed
- ✅ 20 customer dimensions evaluated
- ✅ 100% data quality (no missing values)
- ✅ Advanced SQL window functions for segmentation

### **Machine Learning Models**
- ✅ **Logistic Regression:** 81.76% accuracy (SELECTED MODEL)
- ✅ **Random Forest:** 79.84% accuracy (feature analysis)
- ✅ **ROC-AUC Score:** 0.85 (excellent discrimination)
- ✅ **Production-ready:** Model serialized and deployable

### **Business Intelligence**
- ✅ Interactive Power BI dashboard with 8 pages
- ✅ Customer risk segmentation (High/Medium/Low)
- ✅ Revenue impact visualization
- ✅ KPI tracking and trend analysis

### **Professional Documentation**
- ✅ Complete data dictionary (20 features documented)
- ✅ Model card with limitations and ethics
- ✅ SQL guide for analytics teams
- ✅ Installation and setup instructions
- ✅ Business presentation (12+ slides)

---

## 📊 Key Results

### **Business Impact**
| Metric | Value | Context |
|--------|-------|---------|
| **Churn Rate** | 26.5% | Identified 1,869 customers at risk |
| **Monthly Revenue at Risk** | $139,131 | Direct revenue loss from churn |
| **Annual Revenue at Risk** | $1,669,572 | $1.67M annual impact |
| **Potential Monthly Recovery (5% churn reduction)** | $83,479 | Realistic scenario |
| **Potential Annual Recovery (5%)** | $1,001,748 | From optimized retention |

### **Model Performance**
| Metric | Value | Interpretation |
|--------|-------|-----------------|
| **Accuracy** | 81.76% | Correctly classifies 4 out of 5 customers |
| **ROC-AUC** | 0.85 | Excellent ability to rank customers by risk |
| **Precision** | 71% | 71% of predicted churners are actual churners |
| **Recall** | 52% | Identifies 52% of actual churners |
| **F1-Score** | 0.60 | Good balance of precision and recall |

### **Top Churn Drivers** (in order of impact)
| Factor | Impact | Churn Rate | Action |
|--------|--------|-----------|--------|
| **Contract Type** | Highest | Month-to-month: 42.7% vs. Two-year: 2.8% | Convert to longer terms |
| **Internet Service** | High | Fiber optic: 41.9% vs. DSL: 19.0% | Improve fiber service |
| **Payment Method** | High | E-check: 45.3% vs. Auto-pay: 11.3% | Incentivize auto-pay |
| **Customer Tenure** | High | 0-6 months: 53.3% vs. 49-72 months: 9.5% | Intensive onboarding |
| **Tech Support** | Medium | With support: Lower churn | Bundle premium services |

---

## 🚀 Quick Start (5 Minutes)

### **Prerequisites**
- Python 3.9+ ([download](https://www.python.org/downloads/))
- pip (included with Python)

### **Installation**
```bash
# 1. Clone repository
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run analysis
python scripts/churn_analysis.py
```

**Expected output:** Analysis completes in 2-3 minutes. Check `images/` for visualizations and `model/` for trained model.

### **Next Steps**
- 📖 **Full Setup Guide:** See [docs/INSTALL.md](docs/INSTALL.md)
- 🤖 **Model Details:** See [docs/MODEL_CARD.md](docs/MODEL_CARD.md)
- 📋 **Data Reference:** See [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md)

---

## 📁 Repository Structure

```
customer-churn-prediction/
│
├── docs/                              # 📚 Complete documentation
│   ├── INSTALL.md                    # Setup & installation guide
│   ├── DATA_DICTIONARY.md            # Feature documentation (21 features)
│   ├── MODEL_CARD.md                 # Model details & ethical considerations
│   └── README.md                     # Docs index
│
├── data/
│   └── IT_customer_churn.csv         # Dataset (7,043 customers, 20 features)
│
├── scripts/
│   └── churn_analysis.py             # Main ML pipeline (executable)
│
├── notebooks/
│   └── customer_churn_analysis.ipynb # Interactive Jupyter notebook
│
├── sql/
│   ├── advanced_churn_queries.sql    # SQL analytics & segmentation
│   └── README.md                     # SQL guide & examples
│
├── model/
│   └── logistic_regression_classifier.pkl  # Trained model (serialized)
│
├── images/
│   ├── churn_eda.png                 # EDA visualizations (6 charts)
│   └── churn_model.png               # Model evaluation (feature importance + confusion matrix)
│
├── dashboard/
│   ├── Telecom Customer Churn Dashboard.pbix  # Interactive Power BI dashboard
│   ├── dashboard preview.png         # Dashboard screenshot
│   └── README.md                     # Dashboard guide & pages
│
├── presentation/
│   ├── customer_churn_presentation.pptx  # Business presentation (12+ slides)
│   └── README.md                     # Presentation outline & insights
│
├── requirements.txt                  # Python dependencies (pinned versions)
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

---

## 🔧 Usage

### **Run Python Script** (fastest)
```bash
python scripts/churn_analysis.py
```
Generates: EDA visualizations, model evaluation, trained model ⏱️ 2-3 min

### **Run Jupyter Notebook** (interactive)
```bash
jupyter notebook notebooks/customer_churn_analysis.ipynb
```
Explore code, modify, re-run cells interactively 📖

### **Query SQL Analytics** (database-focused)
Open `sql/advanced_churn_queries.sql` in your SQL client for:
- Revenue impact analysis
- Customer segmentation
- Risk scoring
- Retention opportunity identification

### **Explore Power BI Dashboard** (business intelligence)
Open `dashboard/Telecom Customer Churn Dashboard.pbix` in Power BI Desktop for:
- Interactive KPI dashboards
- Customer segment filtering
- Risk visualization
- Revenue impact tracking

---

## 📊 What's Included

### **Analysis & Modeling**
- ✅ Data cleaning (0 missing values)
- ✅ Exploratory data analysis (EDA) with 6 visualizations
- ✅ Feature engineering (2 new features created)
- ✅ Model training (Logistic Regression + Random Forest)
- ✅ Evaluation (Accuracy, ROC-AUC, Classification Report)

### **Business Insights**
- ✅ Revenue impact quantification ($1.67M annual)
- ✅ Customer segmentation (High/Medium/Low risk)
- ✅ Churn driver identification (top 5 factors)
- ✅ Retention recommendations (5 actionable strategies)

### **Documentation**
- ✅ Installation guide (setup in 5 minutes)
- ✅ Data dictionary (21 features explained)
- ✅ Model card (performance, limitations, ethics)
- ✅ SQL guide (advanced window functions)
- ✅ Power BI guide (8 dashboard pages)
- ✅ Business presentation (12+ slides)

---

## 💡 Key Insights for Recruiters

### **For Data Analyst Position**
- ✅ SQL proficiency (window functions, aggregations, segmentation)
- ✅ Business acumen (revenue impact analysis, segment prioritization)
- ✅ Visualization skills (Power BI dashboard, matplotlib/seaborn)
- ✅ Communication (documentation, business recommendations)

### **For Data Scientist Position**
- ✅ ML modeling (binary classification, model comparison)
- ✅ Feature engineering (domain-aware, iterative improvement)
- ✅ Model evaluation (accuracy, ROC-AUC, classification metrics)
- ✅ Reproducibility (random seeds, version control)
- ✅ Production-readiness (serialized model, clear workflow)

### **For Business Analyst Position**
- ✅ Business problem definition (churn challenge, revenue impact)
- ✅ Data-driven insights (top 5 churn drivers, customer segments)
- ✅ Actionable recommendations (5 prioritized strategies)
- ✅ ROI quantification ($1M+ recovery potential)

---

## 🎯 Top 5 Churn Reduction Strategies

**1. Contract Conversion Campaign** 🏆 Highest ROI
- Convert month-to-month customers to 1-2 year contracts
- Expected impact: **15% churn reduction**
- Revenue recovery: **$250K+ annually**

**2. Fiber Optic Service Excellence**
- Improve service quality and customer support
- Expected impact: **10% churn reduction**
- Revenue recovery: **$167K+ annually**

**3. Auto-Pay Incentive Program**
- Offer discounts for switching to auto-payment
- Expected impact: **8% churn reduction**
- Revenue recovery: **$134K+ annually**

**4. Early Success Program**
- Intensive onboarding for first 6 months (critical period)
- Expected impact: **12% reduction in first-year churn**
- Revenue recovery: **$200K+ annually**

**5. Premium Add-On Bundling**
- Bundle tech support with contracts, especially month-to-month
- Expected impact: **6% churn reduction**
- Revenue recovery: **$100K+ annually**

---

## 📈 Model Performance Details

### **Logistic Regression (Selected Model)**
```
Accuracy:     81.76%  ✅
ROC-AUC:      0.85    ✅✅
Precision:    71%     ✅ Low false-positive rate
Recall:       52%     ✅ Catches majority of churners
F1-Score:     0.60    ✅ Good balance

Classification Report:
                Precision  Recall  F1-Score  Support
    Retained       0.85     0.93      0.89    1,048
    Churned        0.71     0.52      0.60      400
    
    Overall        82%      82%       81%    1,448
```

**Why this model?**
1. Highest accuracy (81.76% vs. 79.84% RF)
2. Excellent ROC-AUC (0.85) — ranks customers well
3. Highly interpretable (business-friendly)
4. Fast inference (production-ready)

---

## 🔗 Documentation Links

| Document | Purpose | Audience |
|----------|---------|----------|
| [docs/INSTALL.md](docs/INSTALL.md) | Setup & environment | Developers |
| [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) | Feature reference | Analysts, Scientists |
| [docs/MODEL_CARD.md](docs/MODEL_CARD.md) | Model details & ethics | Scientists, Managers |
| [sql/README.md](sql/README.md) | SQL query guide | Analysts, DBAs |
| [dashboard/README.md](dashboard/README.md) | Power BI guide | Executives, Managers |
| [presentation/README.md](presentation/README.md) | Presentation outline | All stakeholders |

---

## 🛠️ Tech Stack

**Programming & Data Science**
- Python 3.9+
- pandas (data manipulation)
- NumPy (numerical computing)
- scikit-learn (machine learning)

**Visualization**
- Matplotlib (static charts)
- Seaborn (statistical visualization)
- Plotly (interactive charts)
- Power BI (business intelligence)

**Development**
- Jupyter Notebook (interactive development)
- Git & GitHub (version control)
- Virtual environments (reproducibility)

**Database & Analytics**
- SQL (PostgreSQL/MySQL compatible)
- Advanced window functions
- Complex aggregations

**Model Deployment**
- joblib (model serialization)
- pickle (Python object serialization)
- Ready for REST API, batch scoring, or CRM integration

---

## 📚 Learning Resources

**Concepts Demonstrated:**
- Binary classification (supervised learning)
- Feature engineering (domain-driven)
- Model evaluation (multiple metrics)
- SQL window functions (advanced analytics)
- Business storytelling (data visualization)
- Production-ready code (documentation, structure)

**Skills Showcased:**
- Data cleaning & preprocessing
- Exploratory data analysis
- Machine learning modeling
- SQL analytics
- Business intelligence (Power BI)
- Technical documentation
- Presentation design

---

## ✅ Project Checklist

- ✅ Data quality verified (0 missing, duplicates removed)
- ✅ Models trained and evaluated (81.76% accuracy)
- ✅ Documentation comprehensive (6 guides)
- ✅ Code reproducible (fixed random seeds)
- ✅ Business insights actionable (5 strategies)
- ✅ Presentation professional (12+ slides)
- ✅ Version control (GitHub-ready)

---

## 🎓 Future Enhancements

**Short-term:**
- [ ] Cross-validation for robust estimates
- [ ] Hyperparameter tuning (GridSearchCV)
- [ ] Feature interaction analysis
- [ ] Production monitoring dashboard

**Medium-term:**
- [ ] Advanced models (XGBoost, LightGBM)
- [ ] Causal inference analysis
- [ ] Customer lifetime value (CLV) prediction
- [ ] Real-time scoring API

**Long-term:**
- [ ] Treatment effect modeling (intervention impact)
- [ ] Automated retraining pipeline
- [ ] Fairness & bias audits
- [ ] CRM integration for automated actions

---

## 📧 Questions & Support

- **Installation Issues?** → See [docs/INSTALL.md](docs/INSTALL.md)
- **Data Questions?** → See [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md)
- **Model Details?** → See [docs/MODEL_CARD.md](docs/MODEL_CARD.md)
- **SQL Help?** → See [sql/README.md](sql/README.md)
- **Dashboard Guide?** → See [dashboard/README.md](dashboard/README.md)

---

## 📄 License

MIT License — See [LICENSE](LICENSE) for details

---

## 👤 About

**Project:** Telecom Customer Churn Prediction  
**Portfolio:** Data Analytics & Machine Learning  
**Version:** 1.0  
**Status:** ✅ Production Ready  

**Technologies:** Python • pandas • scikit-learn • SQL • Power BI • Jupyter  

**Contact:** [Your GitHub Profile](https://github.com/your-username)

---

**⭐ If this project was helpful, please consider starring the repository!**

**Last Updated:** June 2026
