# 📋 Data Dictionary

Complete documentation of all features in the Telecom Customer Churn dataset.

**Dataset:** `data/IT_customer_churn.csv`  
**Records:** 7,043 customers  
**Features:** 20 columns  
**Target Variable:** Churn (Binary: Yes/No)

---

## 📊 Feature Overview

| # | Feature | Data Type | Business Category | Values |
|---|---------|-----------|------------------|--------|
| 1 | customerID | String | Identifier | Unique ID |
| 2 | gender | Categorical | Demographics | Male, Female |
| 3 | SeniorCitizen | Binary | Demographics | 0, 1 |
| 4 | Partner | Categorical | Demographics | Yes, No |
| 5 | Dependents | Categorical | Demographics | Yes, No |
| 6 | tenure | Numeric | Engagement | 0-72 months |
| 7 | PhoneService | Categorical | Services | Yes, No |
| 8 | MultipleLines | Categorical | Services | Yes, No, No phone service |
| 9 | InternetService | Categorical | Services | DSL, Fiber optic, No |
| 10 | OnlineSecurity | Categorical | Add-ons | Yes, No, No internet service |
| 11 | OnlineBackup | Categorical | Add-ons | Yes, No, No internet service |
| 12 | DeviceProtection | Categorical | Add-ons | Yes, No, No internet service |
| 13 | TechSupport | Categorical | Add-ons | Yes, No, No internet service |
| 14 | StreamingTV | Categorical | Add-ons | Yes, No, No internet service |
| 15 | StreamingMovies | Categorical | Add-ons | Yes, No, No internet service |
| 16 | Contract | Categorical | Contract | Month-to-month, One year, Two year |
| 17 | PaperlessBilling | Categorical | Billing | Yes, No |
| 18 | PaymentMethod | Categorical | Billing | Electronic check, Mailed check, Bank transfer, Credit card |
| 19 | MonthlyCharges | Numeric | Financial | $0 - $120 |
| 20 | TotalCharges | Numeric | Financial | $0 - $8,000+ |
| 21 | Churn | Target | Outcome | Yes, No |

---

## 🔍 Detailed Feature Documentation

### **1. customerID**
- **Data Type:** String (Identifier)
- **Description:** Unique identifier for each customer
- **Example:** `1234-VYMYX`, `5678-QWESX`
- **Business Meaning:** Used to track individual customers across the dataset
- **Missing Values:** None
- **Unique Values:** 7,043

### **2. gender**
- **Data Type:** Categorical
- **Description:** Biological sex of the customer
- **Example:** Male, Female
- **Business Meaning:** Used for demographic segmentation and churn analysis by gender
- **Missing Values:** None
- **Value Distribution:** Roughly equal split
- **Churn Insight:** Minor variation in churn rate by gender

### **3. SeniorCitizen**
- **Data Type:** Binary (Integer)
- **Description:** Whether the customer is a senior citizen (65+ years)
- **Example:** 0 (Not senior), 1 (Senior citizen)
- **Business Meaning:** Senior citizens may have different service needs and churn patterns
- **Missing Values:** None
- **Value Distribution:** ~84% non-senior (0), ~16% senior (1)
- **Churn Insight:** Senior citizens show moderate churn difference

### **4. Partner**
- **Data Type:** Categorical
- **Description:** Whether the customer has a spouse/partner on the account
- **Example:** Yes, No
- **Business Meaning:** Indicates household structure; partnered customers may have lower churn
- **Missing Values:** None
- **Value Distribution:** ~48% have partner, ~52% don't
- **Churn Insight:** Partner status may indicate loyalty and commitment

### **5. Dependents**
- **Data Type:** Categorical
- **Description:** Whether the customer has dependent children or family members
- **Example:** Yes, No
- **Business Meaning:** Indicates family size; families may churn less
- **Missing Values:** None
- **Value Distribution:** ~30% have dependents, ~70% don't
- **Churn Insight:** Dependents may correlate with longer tenure

### **6. tenure**
- **Data Type:** Numeric (Integer)
- **Description:** Number of months the customer has been with the company
- **Range:** 0-72 months (0-6 years)
- **Example:** 1 (new), 24 (2 years), 72 (6 years)
- **Business Meaning:** Key indicator of customer loyalty; longer tenure usually means lower churn
- **Missing Values:** None
- **Churn Insight:** **CRITICAL DRIVER** - New customers (0-6 months) churn at 53.3%, vs. long-term at 9.5%
- **Average by Churn:**
  - Churned: 17.98 months
  - Retained: 37.57 months

### **7. PhoneService**
- **Data Type:** Categorical
- **Description:** Whether the customer has phone service
- **Example:** Yes, No
- **Business Meaning:** Basic service tier; base for bundling opportunities
- **Missing Values:** None
- **Value Distribution:** ~90% have phone service
- **Churn Insight:** Limited direct correlation with churn

### **8. MultipleLines**
- **Data Type:** Categorical
- **Description:** Whether the customer has multiple phone lines
- **Example:** Yes, No, No phone service
- **Business Meaning:** Indicates service usage intensity
- **Missing Values:** None
- **Possible Values:**
  - "Yes" — Multiple phone lines
  - "No" — Single line or no preference
  - "No phone service" — No phone service subscription
- **Churn Insight:** Service bundling correlates with loyalty

### **9. InternetService**
- **Data Type:** Categorical
- **Description:** Type of internet service subscribed
- **Example:** DSL, Fiber optic, No
- **Business Meaning:** Core service tier; impacts customer value and churn propensity
- **Possible Values:**
  - "DSL" — Digital Subscriber Line (traditional broadband)
  - "Fiber optic" — High-speed fiber internet (premium)
  - "No" — No internet service
- **Missing Values:** None
- **Value Distribution:**
  - DSL: ~43%
  - Fiber optic: ~34%
  - No: ~23%
- **Churn Insight:** **MAJOR DRIVER** - Fiber optic customers churn at 41.9% vs. DSL at 19%
  - Premium service may have higher expectations

### **10. OnlineSecurity**
- **Data Type:** Categorical
- **Description:** Whether customer has online security add-on service
- **Example:** Yes, No, No internet service
- **Business Meaning:** Value-added service; indicates premium tier
- **Possible Values:**
  - "Yes" — Has online security
  - "No" — No online security
  - "No internet service" — Not applicable (no internet)
- **Missing Values:** None
- **Churn Insight:** Customers with add-ons show lower churn (higher engagement)

### **11. OnlineBackup**
- **Data Type:** Categorical
- **Description:** Whether customer has online backup add-on service
- **Example:** Yes, No, No internet service
- **Business Meaning:** Value-added service; indicates data-conscious customers
- **Churn Insight:** Add-on adoption correlates with lower churn

### **12. DeviceProtection**
- **Data Type:** Categorical
- **Description:** Whether customer has device protection/insurance add-on
- **Example:** Yes, No, No internet service
- **Business Meaning:** Premium protection service
- **Churn Insight:** Add-on adoption signals higher engagement

### **13. TechSupport**
- **Data Type:** Categorical
- **Description:** Whether customer has technical support add-on service
- **Example:** Yes, No, No internet service
- **Business Meaning:** Premium support service; high-value service
- **Churn Insight:** **IMPORTANT** - Tech support adoption strongly correlates with lower churn

### **14. StreamingTV**
- **Data Type:** Categorical
- **Description:** Whether customer has streaming TV service add-on
- **Example:** Yes, No, No internet service
- **Business Meaning:** Entertainment bundling; content-driven engagement
- **Churn Insight:** Streaming services increase engagement and reduce churn

### **15. StreamingMovies**
- **Data Type:** Categorical
- **Description:** Whether customer has streaming movies service add-on
- **Example:** Yes, No, No internet service
- **Business Meaning:** Entertainment bundling; content-driven engagement
- **Churn Insight:** Similar to StreamingTV; indicates content consumption

### **16. Contract**
- **Data Type:** Categorical
- **Description:** Duration of customer's service contract
- **Example:** Month-to-month, One year, Two year
- **Business Meaning:** **CRITICAL BUSINESS VARIABLE** - Contract type directly impacts churn probability
- **Possible Values:**
  - "Month-to-month" — Flexible, can cancel anytime
  - "One year" — 1-year commitment
  - "Two year" — 2-year commitment (longest)
- **Missing Values:** None
- **Churn Insight:** **HIGHEST IMPACT DRIVER**
  - Month-to-month: 42.7% churn rate ⚠️
  - One year: 11.3% churn rate
  - Two year: 2.8% churn rate ✅
  - **Business Impact:** Promoting longer contracts is most effective retention strategy

### **17. PaperlessBilling**
- **Data Type:** Categorical
- **Description:** Whether customer uses paperless billing
- **Example:** Yes, No
- **Business Meaning:** Digital engagement metric; may indicate tech-savvy customer
- **Missing Values:** None
- **Value Distribution:** ~59% use paperless
- **Churn Insight:** Digital users show varying churn patterns

### **18. PaymentMethod**
- **Data Type:** Categorical
- **Description:** How the customer pays their bills
- **Example:** Electronic check, Mailed check, Bank transfer, Credit card
- **Business Meaning:** Payment reliability and automation indicator
- **Possible Values:**
  - "Electronic check" — Electronic payment, payment-dependent
  - "Mailed check" — Manual payment method
  - "Bank transfer (automatic)" — Automated, most reliable
  - "Credit card (automatic)" — Automated, most reliable
- **Missing Values:** None
- **Churn Insight:** **SIGNIFICANT DRIVER**
  - Electronic check: 45.3% churn (highest risk) ⚠️
  - Mailed check: 40.5% churn
  - Bank transfer (auto): 16.6% churn
  - Credit card (auto): 11.3% churn ✅
  - **Insight:** Automated payment methods correlate with lower churn

### **19. MonthlyCharges**
- **Data Type:** Numeric (Float)
- **Description:** Amount customer is billed monthly
- **Range:** $0 - $120+
- **Example:** $29.85, $65.00, $99.99
- **Unit:** USD
- **Business Meaning:** Revenue per customer; price sensitivity indicator
- **Missing Values:** None
- **Churn Insight:**
  - **Churned customers average:** $74.44/month
  - **Retained customers average:** $61.27/month
  - **Interpretation:** Higher billing customers churn more (potential price sensitivity or service dissatisfaction)

### **20. TotalCharges**
- **Data Type:** Numeric (String in raw data, converted to float)
- **Description:** Total cumulative charges paid by the customer over tenure
- **Calculation:** MonthlyCharges × tenure (approximately)
- **Range:** $0 - $8,000+
- **Example:** $29.85 (1 month), $1,450.00 (24 months), $2,850.75 (72 months)
- **Unit:** USD
- **Business Meaning:** Lifetime value (LTV) indicator; long-term customer worth
- **Missing Values:** None (note: some entries may have spaces, handled in cleaning)
- **Churn Insight:**
  - Churned customers have lower total charges (due to shorter tenure)
  - Inverse relationship with churn: higher lifetime value = lower churn

### **21. Churn** ⭐ TARGET VARIABLE
- **Data Type:** Categorical (Binary)
- **Description:** Whether the customer has churned (discontinued service)
- **Example:** Yes (churned), No (retained)
- **Business Meaning:** **Prediction target** for ML model
- **Possible Values:**
  - "Yes" — Customer churned (left the service)
  - "No" — Customer retained (still subscribed)
- **Missing Values:** None
- **Class Distribution:**
  - No (Retained): 5,174 customers (73.5%) ✅
  - Yes (Churned): 1,869 customers (26.5%) ⚠️
- **Business Impact:** 26.5% churn rate across customer base
  - Monthly revenue loss: **$139,131**
  - Annual revenue loss: **$1,669,572**

---

## 🎯 Feature Engineering in Model

The ML pipeline creates two additional engineered features:

### **ChargesPerMonth**
- **Calculation:** `TotalCharges / (tenure + 1)`
- **Purpose:** Normalize charges by customer tenure; identifies pricing per month of loyalty
- **Interpretation:** Customers paying more per month of tenure have higher churn risk

### **IsNewCustomer**
- **Calculation:** `tenure <= 6` (0 or 1)
- **Purpose:** Flag customers in critical first 6 months
- **Business Meaning:** New customers (0-6 months) are highest churn risk at 53.3%

---

## 📈 Summary Statistics

| Feature | Type | Missing | Unique | Mean | Median | Std Dev | Min | Max |
|---------|------|---------|--------|------|--------|---------|-----|-----|
| tenure | Numeric | 0 | 73 | 32.37 | 29 | 24.54 | 0 | 72 |
| MonthlyCharges | Numeric | 0 | 1,500+ | 64.76 | 65.00 | 30.09 | 18 | 120 |
| TotalCharges | Numeric | 0 | 6,500+ | 2,283.30 | 1,397.47 | 2,266.77 | 18.80 | 8,684.80 |

---

## 🔗 Related Documentation

- **Model Details:** See [MODEL_CARD.md](MODEL_CARD.md)
- **Installation Guide:** See [INSTALL.md](INSTALL.md)
- **Project Overview:** See [../README.md](../README.md)

---

**Data Dictionary Version:** 1.0  
**Last Updated:** June 2026  
**Data Quality:** ✅ Clean (no missing values, duplicates removed)
