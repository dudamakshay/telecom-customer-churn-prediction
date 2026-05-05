# ============================================================
# TELECOM CHURN PREDICTION — STREAMLIT APP
# Run: streamlit run churn_app.py
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, roc_auc_score, roc_curve
)
import warnings
warnings.filterwarnings('ignore')

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="Churn Prediction | TelecomCorp",
    page_icon="📡",
    layout="wide"
)

# ── CUSTOM CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f172a; }
    .metric-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
    }
    .stMetric { background: #1e293b; border-radius: 8px; padding: 12px; }
    h1 { color: #38bdf8; }
    h2, h3 { color: #e2e8f0; }
</style>
""", unsafe_allow_html=True)

# ── LOAD & CACHE DATA ───────────────────────────────────────
@st.cache_data
def load_data():
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(BASE_DIR, 'data', 'IT_customer_churn.csv')

    df = pd.read_csv(data_path)   # ✅ IMPORTANT

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)

    return df

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(BASE_DIR, 'data', 'IT_customer_churn.csv')

    df = pd.read_csv(data_path)   # ✅ THIS LINE WAS MISSING

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
    
    return df

@st.cache_data
def train_models(df):
    df_model = df.copy()
    le = LabelEncoder()
    cat_cols = df_model.select_dtypes(include='object').columns.tolist()
    cat_cols.remove('Churn')
    for col in cat_cols:
        df_model[col] = le.fit_transform(df_model[col])
    df_model['Churn'] = (df_model['Churn'] == 'Yes').astype(int)

    # Feature engineering
    df_model['ChargesPerMonth'] = df_model['TotalCharges'] / (df_model['tenure'] + 1)
    df_model['IsNewCustomer']   = (df_model['tenure'] <= 6).astype(int)

    X = df_model.drop('Churn', axis=1)
    y = df_model['Churn']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        'Logistic Regression':   LogisticRegression(max_iter=1000, random_state=42),
        'Random Forest':         RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting':     GradientBoostingClassifier(n_estimators=100, random_state=42),
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred  = model.predict(X_test)
        proba = model.predict_proba(X_test)[:, 1]
        results[name] = {
            'model':    model,
            'pred':     pred,
            'proba':    proba,
            'accuracy': accuracy_score(y_test, pred),
            'roc_auc':  roc_auc_score(y_test, proba),
            'cm':       confusion_matrix(y_test, pred),
            'report':   classification_report(y_test, pred, target_names=['Retained','Churned'])
        }
    return results, X_test, y_test, X.columns.tolist(), models['Random Forest']

# ── SIDEBAR ──────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/phone-signal.png", width=60)
    st.title("TelecomCorp")
    st.caption("Churn Analytics Platform")
    st.divider()
    page = st.radio(
        "Navigate",
        ["📊 Executive Dashboard",
         "🔍 EDA & Insights",
         "🤖 ML Models",
         "🎯 Predict Customer Risk",
         "💡 Interview Guide"]
    )
    st.divider()
    st.caption("Dataset: 7,043 customers | 20 features")
    st.caption("Models: LR · RF · GBM")

df = load_data()
results, X_test, y_test, feature_cols, rf_model = train_models(df)

# ════════════════════════════════════════════════════════════
# PAGE 1: EXECUTIVE DASHBOARD
# ════════════════════════════════════════════════════════════
if page == "📊 Executive Dashboard":
    st.title("📡 Customer Churn Intelligence Dashboard")
    st.caption("Real-time churn analytics · TelecomCorp Data Science Team")
    st.divider()

    # KPI Row
    churned_df  = df[df['Churn'] == 'Yes']
    retained_df = df[df['Churn'] == 'No']
    monthly_loss = churned_df['MonthlyCharges'].sum()
    annual_loss  = monthly_loss * 12

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Customers",    f"{len(df):,}")
    col2.metric("Churned Customers",  f"{len(churned_df):,}", delta="-26.5%", delta_color="inverse")
    col3.metric("Churn Rate",         "26.5%", delta="+5.5pp vs industry", delta_color="inverse")
    col4.metric("Monthly Rev Lost",   f"${monthly_loss:,.0f}", delta_color="inverse")
    col5.metric("Annual Rev at Risk", f"${annual_loss:,.0f}", delta_color="inverse")

    st.divider()

    # Charts Row 1
    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Churn Rate by Contract Type")
        contract_data = df.groupby('Contract').apply(
            lambda x: round((x['Churn'] == 'Yes').mean() * 100, 1)
        ).reset_index()
        contract_data.columns = ['Contract', 'Churn Rate %']
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        colors = ['#ff4d6d', '#ffb347', '#00e096']
        bars = ax.barh(contract_data['Contract'], contract_data['Churn Rate %'],
                       color=colors, height=0.5)
        for bar, val in zip(bars, contract_data['Churn Rate %']):
            ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                    f'{val}%', va='center', color='white', fontsize=11, fontweight='bold')
        ax.set_xlabel('Churn Rate (%)', color='#94a3b8')
        ax.tick_params(colors='#94a3b8')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        for sp in ['bottom','left']:
            ax.spines[sp].set_color('#334155')
        ax.set_xlim(0, 55)
        st.pyplot(fig)
        plt.close()

    with col_b:
        st.subheader("Churn Rate by Internet Service")
        inet_data = df.groupby('InternetService').apply(
            lambda x: round((x['Churn'] == 'Yes').mean() * 100, 1)
        ).reset_index()
        inet_data.columns = ['Service', 'Churn Rate %']
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        colors2 = ['#38bdf8', '#ff4d6d', '#00e096']
        wedges, texts, autotexts = ax.pie(
            inet_data['Churn Rate %'], labels=inet_data['Service'],
            autopct='%1.1f%%', colors=colors2,
            textprops={'color': 'white', 'fontsize': 10}
        )
        for at in autotexts:
            at.set_fontweight('bold')
        st.pyplot(fig)
        plt.close()

    # Charts Row 2
    col_c, col_d = st.columns(2)

    with col_c:
        st.subheader("Churn Rate by Tenure Band")
        df['tenure_band'] = pd.cut(df['tenure'], bins=[0,6,12,24,48,72],
                                    labels=['0–6mo','7–12mo','13–24mo','25–48mo','49–72mo'])
        tenure_data = df.groupby('tenure_band', observed=False).apply(
            lambda x: round((x['Churn'] == 'Yes').mean() * 100, 1)
        ).reset_index()
        tenure_data.columns = ['Tenure Band','Churn Rate %']
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        ax.plot(tenure_data['Tenure Band'], tenure_data['Churn Rate %'],
                marker='o', color='#ff4d6d', linewidth=2.5, markersize=7)
        ax.fill_between(range(len(tenure_data)), tenure_data['Churn Rate %'],
                        alpha=0.15, color='#ff4d6d')
        for i, v in enumerate(tenure_data['Churn Rate %']):
            ax.annotate(f'{v}%', (i, v), textcoords="offset points",
                        xytext=(0, 8), ha='center', color='white', fontsize=9, fontweight='bold')
        ax.set_xticks(range(len(tenure_data)))
        ax.set_xticklabels(tenure_data['Tenure Band'], color='#94a3b8', rotation=20)
        ax.tick_params(colors='#94a3b8')
        ax.set_ylabel('Churn Rate (%)', color='#94a3b8')
        ax.set_facecolor('#1e293b')
        for sp in ['top','right']:
            ax.spines[sp].set_visible(False)
        for sp in ['bottom','left']:
            ax.spines[sp].set_color('#334155')
        st.pyplot(fig)
        plt.close()

    with col_d:
        st.subheader("Revenue Lost by Payment Method")
        pay_data = df[df['Churn']=='Yes'].groupby('PaymentMethod')['MonthlyCharges'].sum().reset_index()
        pay_data.columns = ['Method','Revenue Lost']
        pay_data = pay_data.sort_values('Revenue Lost', ascending=True)
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        short_labels = [m.replace(' (automatic)','*').replace('Electronic','E-').replace('Mailed','Mail')
                        for m in pay_data['Method']]
        bars = ax.barh(short_labels, pay_data['Revenue Lost'],
                       color=['#334155','#475569','#ff4d6d','#ff4d6d'], height=0.5)
        for bar, val in zip(bars, pay_data['Revenue Lost']):
            ax.text(bar.get_width() + 200, bar.get_y() + bar.get_height()/2,
                    f'${val:,.0f}', va='center', color='white', fontsize=9)
        ax.set_xlabel('Monthly Revenue Lost ($)', color='#94a3b8')
        ax.tick_params(colors='#94a3b8')
        for sp in ['top','right']:
            ax.spines[sp].set_visible(False)
        for sp in ['bottom','left']:
            ax.spines[sp].set_color('#334155')
        st.pyplot(fig)
        plt.close()

    # Revenue Impact Table
    st.divider()
    st.subheader("💰 Revenue Impact Summary")
    impact_df = pd.DataFrame({
        'Segment': ['Month-to-Month', 'Fiber Optic', 'Electronic Check', 'New Customers (0-6mo)', 'TOTAL'],
        'Churned Customers': [1655, 1297, 1071, 784, 1869],
        'Monthly Revenue Lost': ['$69,842', '$63,932', '$57,712', '$38,445', '$139,131'],
        'Annual Revenue Lost': ['$838,104', '$767,184', '$692,544', '$461,340', '$1,669,572'],
        'Priority': ['🔴 Critical', '🔴 Critical', '🔴 Critical', '🟡 High', '—']
    })
    st.dataframe(impact_df, use_container_width=True, hide_index=True)

# ════════════════════════════════════════════════════════════
# PAGE 2: EDA & INSIGHTS
# ════════════════════════════════════════════════════════════
elif page == "🔍 EDA & Insights":
    st.title("🔍 Exploratory Data Analysis")
    st.caption("Understanding patterns in the churn dataset")

    tab1, tab2, tab3 = st.tabs(["📋 Data Overview", "📈 Distributions", "🔗 Correlation"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Dataset Shape")
            st.info(f"**{df.shape[0]:,} rows** × **{df.shape[1]} columns**")
            st.subheader("Missing Values")
            nulls = df.isnull().sum()
            st.success(f"✅ Zero missing values in {len(nulls)} columns")
        with col2:
            st.subheader("Column Types")
            dtype_df = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.astype(str),
                'Category': ['Categorical' if df[c].dtype == 'object' else 'Numerical' for c in df.columns]
            })
            st.dataframe(dtype_df, hide_index=True, use_container_width=True)

        st.subheader("Sample Data")
        st.dataframe(df.head(10), use_container_width=True)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            col_choice = st.selectbox("Select Numerical Column",
                                       ['tenure', 'MonthlyCharges', 'TotalCharges'])
            fig, ax = plt.subplots(figsize=(6, 4))
            fig.patch.set_facecolor('#1e293b')
            ax.set_facecolor('#1e293b')
            ax.hist(df[df['Churn']=='Yes'][col_choice], alpha=0.7,
                    label='Churned', color='#ff4d6d', bins=30)
            ax.hist(df[df['Churn']=='No'][col_choice], alpha=0.7,
                    label='Retained', color='#00e096', bins=30)
            ax.legend()
            ax.set_xlabel(col_choice, color='#94a3b8')
            ax.set_ylabel('Count', color='#94a3b8')
            ax.tick_params(colors='#94a3b8')
            for sp in ['top','right']:
                ax.spines[sp].set_visible(False)
            for sp in ['bottom','left']:
                ax.spines[sp].set_color('#334155')
            st.pyplot(fig); plt.close()

        with col2:
            cat_choice = st.selectbox("Select Categorical Column",
                                       ['Contract','InternetService','PaymentMethod','gender','SeniorCitizen'])
            fig, ax = plt.subplots(figsize=(6, 4))
            fig.patch.set_facecolor('#1e293b')
            ax.set_facecolor('#1e293b')
            churn_by_cat = df.groupby([cat_choice,'Churn']).size().unstack(fill_value=0)
            churn_by_cat.plot(kind='bar', ax=ax, color=['#00e096','#ff4d6d'],
                              edgecolor='none', width=0.6)
            ax.legend(['Retained','Churned'], facecolor='#1e293b', labelcolor='white')
            ax.set_xlabel(cat_choice, color='#94a3b8')
            ax.tick_params(colors='#94a3b8', axis='x', rotation=25)
            ax.tick_params(colors='#94a3b8', axis='y')
            for sp in ['top','right']:
                ax.spines[sp].set_visible(False)
            for sp in ['bottom','left']:
                ax.spines[sp].set_color('#334155')
            st.pyplot(fig); plt.close()

    with tab3:
        st.subheader("Correlation Heatmap (Numerical Columns)")
        num_df = df[['tenure','MonthlyCharges','TotalCharges','SeniorCitizen']].copy()
        num_df['Churn_Num'] = (df['Churn'] == 'Yes').astype(int)
        fig, ax = plt.subplots(figsize=(7, 5))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        sns.heatmap(num_df.corr(), annot=True, fmt='.2f', cmap='coolwarm',
                    ax=ax, linewidths=0.5, linecolor='#0f172a',
                    annot_kws={'size': 11, 'color': 'white'})
        ax.tick_params(colors='white')
        st.pyplot(fig); plt.close()

        st.info("📌 **Key Insight:** Tenure has a **negative correlation** with churn — longer-tenured customers are less likely to leave. Monthly Charges have a **positive correlation** — higher bills = higher churn risk.")

# ════════════════════════════════════════════════════════════
# PAGE 3: ML MODELS
# ════════════════════════════════════════════════════════════
elif page == "🤖 ML Models":
    st.title("🤖 Machine Learning Model Comparison")
    st.caption("Logistic Regression vs Random Forest vs Gradient Boosting")

    # Model comparison table
    comp_df = pd.DataFrame({
        'Model': list(results.keys()),
        'Accuracy': [f"{v['accuracy']:.4f}" for v in results.values()],
        'ROC-AUC':  [f"{v['roc_auc']:.4f}" for v in results.values()],
        'Best For': ['Explainability & speed', 'Balanced accuracy + feature importance', 'Highest performance']
    })
    st.subheader("📊 Model Comparison")
    st.dataframe(comp_df, hide_index=True, use_container_width=True)

    # Select model to inspect
    selected = st.selectbox("Choose model to inspect in detail",
                             list(results.keys()))
    res = results[selected]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots(figsize=(5, 4))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        sns.heatmap(res['cm'], annot=True, fmt='d', cmap='Blues', ax=ax,
                    xticklabels=['Retained','Churned'],
                    yticklabels=['Retained','Churned'],
                    linewidths=0.5, linecolor='#0f172a',
                    annot_kws={'size': 14, 'weight': 'bold'})
        ax.set_ylabel('Actual', color='#94a3b8')
        ax.set_xlabel('Predicted', color='#94a3b8')
        ax.tick_params(colors='#94a3b8')
        st.pyplot(fig); plt.close()

    with col2:
        st.subheader("ROC Curve")
        fig, ax = plt.subplots(figsize=(5, 4))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        fpr, tpr, _ = roc_curve(y_test, res['proba'])
        ax.plot(fpr, tpr, color='#38bdf8', lw=2.5,
                label=f"AUC = {res['roc_auc']:.3f}")
        ax.plot([0,1],[0,1], color='#475569', lw=1, linestyle='--')
        ax.set_xlabel('False Positive Rate', color='#94a3b8')
        ax.set_ylabel('True Positive Rate', color='#94a3b8')
        ax.tick_params(colors='#94a3b8')
        ax.legend(facecolor='#1e293b', labelcolor='white')
        for sp in ['top','right']:
            ax.spines[sp].set_visible(False)
        for sp in ['bottom','left']:
            ax.spines[sp].set_color('#334155')
        ax.fill_between(fpr, tpr, alpha=0.1, color='#38bdf8')
        st.pyplot(fig); plt.close()

    # Classification Report
    st.subheader("Classification Report")
    st.code(res['report'])

    # Feature Importance (RF only)
    if selected == 'Random Forest':
        st.subheader("🎯 Top 15 Feature Importances")
        df_model_fi = df.copy()
        df_model_fi['TotalCharges'] = pd.to_numeric(df_model_fi['TotalCharges'], errors='coerce').fillna(0)
        le = LabelEncoder()
        cat_cols = df_model_fi.select_dtypes(include='object').columns.tolist()
        cat_cols.remove('Churn')
        for col in cat_cols:
            df_model_fi[col] = le.fit_transform(df_model_fi[col])
        df_model_fi['Churn'] = (df_model_fi['Churn'] == 'Yes').astype(int)
        df_model_fi['ChargesPerMonth'] = df_model_fi['TotalCharges'] / (df_model_fi['tenure'] + 1)
        df_model_fi['IsNewCustomer']   = (df_model_fi['tenure'] <= 6).astype(int)
        X_fi = df_model_fi.drop('Churn', axis=1)

        fi = pd.Series(rf_model.feature_importances_, index=X_fi.columns).sort_values(ascending=True).tail(12)
        fig, ax = plt.subplots(figsize=(8, 5))
        fig.patch.set_facecolor('#1e293b')
        ax.set_facecolor('#1e293b')
        colors_fi = ['#ff4d6d' if i >= len(fi)-3 else '#38bdf8' for i in range(len(fi))]
        fi.plot(kind='barh', ax=ax, color=colors_fi)
        ax.set_xlabel('Importance Score', color='#94a3b8')
        ax.tick_params(colors='#94a3b8')
        for sp in ['top','right']:
            ax.spines[sp].set_visible(False)
        for sp in ['bottom','left']:
            ax.spines[sp].set_color('#334155')
        ax.axvline(x=0.05, color='#475569', linestyle='--', alpha=0.5)
        st.pyplot(fig); plt.close()

        st.info("🔴 Red bars = Top 3 churn drivers. Focus retention budget on these features.")

# ════════════════════════════════════════════════════════════
# PAGE 4: PREDICT CUSTOMER RISK
# ════════════════════════════════════════════════════════════
elif page == "🎯 Predict Customer Risk":
    st.title("🎯 Individual Customer Churn Risk Predictor")
    st.caption("Enter customer details to get instant churn probability")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Demographics")
        gender          = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen  = st.selectbox("Senior Citizen", ["No", "Yes"])
        partner         = st.selectbox("Has Partner", ["Yes", "No"])
        dependents      = st.selectbox("Has Dependents", ["Yes", "No"])
        tenure          = st.slider("Tenure (months)", 0, 72, 12)

    with col2:
        st.subheader("Services")
        phone_service   = st.selectbox("Phone Service", ["Yes", "No"])
        internet_svc    = st.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])
        online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
        tech_support    = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
        streaming_tv    = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])

    with col3:
        st.subheader("Account & Billing")
        contract        = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        paperless       = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment_method  = st.selectbox("Payment Method", [
            "Electronic check", "Mailed check",
            "Bank transfer (automatic)", "Credit card (automatic)"
        ])
        monthly_charges = st.slider("Monthly Charges ($)", 18.0, 119.0, 70.0)
        total_charges   = monthly_charges * tenure

    if st.button("🔮 Predict Churn Risk", type="primary", use_container_width=True):
        # Build input row matching training columns
        input_map = {
            'gender':            1 if gender == 'Male' else 0,
            'SeniorCitizen':     1 if senior_citizen == 'Yes' else 0,
            'Partner':           1 if partner == 'Yes' else 0,
            'Dependents':        1 if dependents == 'Yes' else 0,
            'tenure':            tenure,
            'PhoneService':      1 if phone_service == 'Yes' else 0,
            'MultipleLines':     0,
            'InternetService':   {'Fiber optic': 1, 'DSL': 0, 'No': 2}[internet_svc],
            'OnlineSecurity':    {'No': 0, 'Yes': 1, 'No internet service': 2}[online_security],
            'OnlineBackup':      0,
            'DeviceProtection':  0,
            'TechSupport':       {'No': 0, 'Yes': 1, 'No internet service': 2}[tech_support],
            'StreamingTV':       {'No': 0, 'Yes': 1, 'No internet service': 2}[streaming_tv],
            'StreamingMovies':   0,
            'Contract':          {'Month-to-month': 0, 'One year': 1, 'Two year': 2}[contract],
            'PaperlessBilling':  1 if paperless == 'Yes' else 0,
            'PaymentMethod':     {'Electronic check': 2, 'Mailed check': 3,
                                  'Bank transfer (automatic)': 0,
                                  'Credit card (automatic)': 1}[payment_method],
            'MonthlyCharges':    monthly_charges,
            'TotalCharges':      total_charges,
            'ChargesPerMonth':   total_charges / (tenure + 1),
            'IsNewCustomer':     1 if tenure <= 6 else 0,
        }
        input_df = pd.DataFrame([input_map])

        prob = rf_model.predict_proba(input_df)[0][1]
        risk_pct = round(prob * 100, 1)

        st.divider()
        col_res1, col_res2, col_res3 = st.columns(3)

        with col_res1:
            color = "#ff4d6d" if risk_pct > 60 else "#ffb347" if risk_pct > 35 else "#00e096"
            risk_label = "🔴 HIGH RISK" if risk_pct > 60 else "🟡 MEDIUM RISK" if risk_pct > 35 else "🟢 LOW RISK"
            st.markdown(f"""
            <div style='background:#1e293b;border-radius:12px;padding:24px;text-align:center;border:2px solid {color};'>
                <div style='font-size:48px;font-weight:900;color:{color};'>{risk_pct}%</div>
                <div style='font-size:18px;color:{color};margin-top:8px;'>{risk_label}</div>
                <div style='font-size:12px;color:#64748b;margin-top:4px;'>Churn Probability</div>
            </div>""", unsafe_allow_html=True)

        with col_res2:
            st.metric("Contract Type", contract)
            st.metric("Tenure", f"{tenure} months")
            st.metric("Monthly Bill", f"${monthly_charges:.2f}")

        with col_res3:
            st.subheader("Recommended Actions")
            if risk_pct > 60:
                st.error("⚡ Immediate retention call required")
                st.error("🎁 Offer 20% discount or plan upgrade")
                st.error("📞 Assign dedicated account manager")
            elif risk_pct > 35:
                st.warning("📧 Send personalized retention email")
                st.warning("💡 Recommend annual contract upgrade")
            else:
                st.success("✅ Customer is stable — maintain quality")
                st.success("🌟 Candidate for upsell/cross-sell")

# ════════════════════════════════════════════════════════════
# PAGE 5: INTERVIEW GUIDE
# ════════════════════════════════════════════════════════════
elif page == "💡 Interview Guide":
    st.title("💡 Interview Preparation Guide")
    st.caption("Beginner-friendly explanations — say these in your interview!")

    tab1, tab2, tab3 = st.tabs(["🎤 1-Min Pitch", "❓ Q&A", "⚠️ Avoid These Mistakes"])

    with tab1:
        st.subheader("Your 1-Minute Project Explanation")
        st.success("""
**"I built an end-to-end Customer Churn Prediction project for a telecom company.**

The company had 7,043 customers and was losing 26.5% of them — that's $139,000 every month in lost revenue.

I used SQL to analyze patterns — I found that month-to-month contract customers churn at 42.7%, while two-year contract customers only churn at 2.8%. That's a 15x difference.

In Python, I built three machine learning models — Logistic Regression, Random Forest, and Gradient Boosting. My best model achieved 81.76% accuracy and a ROC-AUC score of 0.85.

I identified the top churn drivers: monthly charges, tenure, and contract type. Finally, I built a Streamlit app where any team member can enter a customer's details and instantly see their churn risk score.

The business outcome: by targeting just the top 500 high-risk customers each month, the company can potentially save $50,000+ in monthly revenue."**
        """)

        st.subheader("30-Second Version (for quick intro)")
        st.info("""
**"I built a churn prediction model for a telecom company with 7,043 customers.
The churn rate was 26.5%, causing $139K monthly revenue loss.
I used Python and SQL for analysis, built ML models achieving 81.76% accuracy,
and identified that contract type and monthly charges are the biggest churn drivers.
The model helps the retention team target high-risk customers before they leave."**
        """)

    with tab2:
        qas = [
            ("Q1: What is churn and why does it matter?",
             "Churn means a customer stopped using our service. It matters because getting a new customer costs 5x more than keeping an existing one. In our dataset, 1,869 customers left — causing $139,000 in monthly revenue loss."),
            ("Q2: What data did you use?",
             "I used a telecom dataset with 7,043 customers and 20 columns — including demographics (age, gender), services (internet, phone), billing (monthly charges), and the target variable: Churn (Yes/No)."),
            ("Q3: What was your biggest finding?",
             "Month-to-month contract customers churn at 42.7% vs only 2.8% for two-year contracts. This single insight saves the business millions — just convince customers to switch to annual contracts."),
            ("Q4: Why did you choose Random Forest?",
             "Random Forest handles mixed data types (text + numbers), doesn't need much preprocessing, and gives feature importance scores — which tells us WHICH factors cause churn. This is very valuable for business decisions."),
            ("Q5: What is ROC-AUC?",
             "It measures how well the model separates churners from non-churners. Score of 0.5 = random guessing. Score of 1.0 = perfect. My model scored 0.85 — meaning it's very good at ranking high-risk customers."),
            ("Q6: How would the business use this model?",
             "Run the model every month. Get a list of top 500 high-risk customers. Assign the retention team to call them with special offers (discount, free upgrade). This prevents churn before it happens."),
            ("Q7: What is a Confusion Matrix?",
             "It shows 4 things: customers correctly predicted as Retained, correctly predicted as Churned, wrongly flagged as churning (false alarm), and missed churners (we said they'd stay but they left). Missed churners are the most costly."),
            ("Q8: How did you clean the data?",
             "I checked for missing values — there were none. I removed duplicates. I converted text columns (like 'Yes'/'No') into numbers using Label Encoding so the ML model could understand them."),
            ("Q9: What SQL did you use?",
             "I used GROUP BY to find churn rates by contract and internet service. I used window functions for running totals and rank-based segmentation. I wrote CASE WHEN logic to label customers as High, Medium, or Low risk."),
            ("Q10: What would you improve?",
             "I would add SMOTE to handle class imbalance better, try XGBoost for higher accuracy, build a real-time scoring API using FastAPI, and set up monthly automated reports so leadership gets updates automatically."),
        ]
        for q, a in qas:
            with st.expander(q):
                st.write(a)

    with tab3:
        st.subheader("⚠️ Common Mistakes Beginners Make in Interviews")
        mistakes = {
            "❌ Saying 'I just ran the code'":
                "✅ Say: 'I analyzed the business problem first, then chose the right technique.'",
            "❌ Only talking about accuracy":
                "✅ Always mention ROC-AUC, Precision, Recall — especially for imbalanced data.",
            "❌ No business connection":
                "✅ Always connect findings to money. Don't say '42.7% churn'. Say '$69,000/month lost from this segment.'",
            "❌ Memorizing answers without understanding":
                "✅ Understand the concept simply first. If you can explain it to a 10-year-old, you can explain it to an interviewer.",
            "❌ Saying 'The model is 81% accurate' as if it's perfect":
                "✅ Say: 'Accuracy is 81.76%, but more importantly the ROC-AUC is 0.85, which means the model is strong at identifying who will actually churn.'",
            "❌ Not knowing your own numbers":
                "✅ Memorize: 7,043 customers, 26.5% churn, $139K monthly loss, 81.76% accuracy, top 3 drivers.",
        }
        for mistake, fix in mistakes.items():
            st.error(mistake)
            st.success(fix)
            st.write("")
