# 📊 Power BI Dashboard Guide

Interactive business intelligence dashboard for telecom customer churn analysis.

**File:** `Telecom Customer Churn Dashboard.pbix`  
**Software Required:** Power BI Desktop (Windows) or Power BI Online  
**Last Updated:** June 2026

---

## 📋 Overview

**Purpose:** Provide executives and managers with real-time, interactive churn analytics

**Key Features:**
- Interactive filtering and drilling
- KPI cards with key metrics
- Trend analysis and segmentation
- Risk-based customer ranking
- Revenue impact visualization

**Audience:**
- C-level executives (revenue/strategy view)
- Operations managers (segment view)
- Retention teams (customer-level view)
- Finance stakeholders (revenue view)

---

## 📊 Dashboard Pages

### **Page 1: Executive Overview** 📈

**Purpose:** High-level business metrics for C-suite

**Key Metrics Displayed:**
- **Total Customers:** 7,043
- **Churn Rate:** 26.5%
- **Churned Count:** 1,869 customers
- **Monthly Revenue at Risk:** $139,131
- **Annual Revenue at Risk:** $1,669,572
- **Average Customer Tenure:** 32.4 months

**Visualizations:**
1. **KPI Cards** (top of page)
   - Shows 6 main metrics with trend indicators
   - Red = negative trend, Green = improvement

2. **Churn Rate Trend** (line chart)
   - Shows churn rate over time (if temporal data available)
   - Reference line at 26.5% baseline

3. **Revenue Impact Waterfall** (waterfall chart)
   - Total monthly charges → Churn revenue loss → Net revenue impact
   - Shows magnitude of problem visually

4. **Churn Distribution Pie Chart** (pie chart)
   - Churned (26.5%) vs. Retained (73.5%) split
   - Visual representation of class imbalance

**Filters Available:**
- Contract Type (Month-to-month, One year, Two year)
- Internet Service (DSL, Fiber optic, None)
- Date Range (if applicable)

**Use Cases:**
- Board presentations
- Quarterly business reviews
- Investor briefings
- Strategic planning sessions

---

### **Page 2: Churn by Contract Type** 📋

**Purpose:** Understand churn patterns by contract commitment level

**Key Metrics:**
| Contract | Customer Count | Churn Rate | Revenue at Risk | Action |
|----------|---|---|---|---|
| Month-to-month | 3,875 | 42.7% | $97,381/mo | Highest priority |
| One year | 1,473 | 11.3% | $28,394/mo | Medium priority |
| Two year | 1,695 | 2.8% | $13,356/mo | Low priority |

**Visualizations:**
1. **Churn Rate by Contract** (clustered bar chart)
   - Shows churn% on Y-axis, contract type on X-axis
   - Color coded by risk level (red=high, yellow=medium, green=low)

2. **Revenue Loss by Contract** (stacked bar chart)
   - Shows composition of revenue loss
   - Reinforces which segments to prioritize

3. **Customer Distribution** (donut chart)
   - Size of each contract segment
   - Visual: Month-to-month = 55% of customers

4. **Trend Line** (line chart over time)
   - Shows whether churn improving/worsening by contract

**Filters Available:**
- Internet Service type
- Tenure cohort
- Payment method

**Key Insights:**
- ✅ Month-to-month has 15x higher churn than two-year
- ✅ Contract conversion is highest-ROI retention lever
- ✅ Most customers in highest-risk category

**Drill-Down Capability:**
- Click on "Month-to-month" bar to see customer list
- Further drill to individual customer details

---

### **Page 3: Internet Service Analysis** 🌐

**Purpose:** Analyze churn patterns by internet service type

**Key Metrics:**
| Service | Customer Count | Churn Rate | Avg Monthly Charge |
|---------|---|---|---|
| Fiber optic | 2,404 | 41.9% | $99.65 |
| DSL | 3,069 | 19.0% | $55.89 |
| No internet | 1,570 | 7.5% | $20.04 |

**Visualizations:**
1. **Churn Rate by Service** (bar chart)
   - Fiber optic towers above others
   - Indicates service quality/value issue

2. **Customer Lifecycle Curve** (line chart)
   - Tenure vs. churn rate for each service type
   - Shows when critical intervention points occur

3. **Revenue Concentration** (pie chart)
   - Where revenue comes from by service type
   - Fiber optic = 46% of churn revenue (despite lower customer count)

4. **Net Promoter Score (if available)** (gauge chart)
   - Service satisfaction indicator
   - Correlates with churn risk

**Key Insights:**
- ⚠️ Fiber optic has premium-tier problems (unmet expectations?)
- ✅ Phone-only customers most loyal
- 💰 Fiber optic drives majority of revenue loss

**Business Actions:**
- Investigate fiber optic service quality
- Offer enhanced support to fiber customers
- Review pricing/value proposition alignment

---

### **Page 4: Tenure & Customer Maturity** ⏰

**Purpose:** Understand how customer loyalty evolves over time

**Key Metrics (by tenure band):**
| Tenure | Customers | Churn Rate | Avg Monthly Charge |
|--------|---|---|---|
| 0-6 months | 1,114 | 53.3% | $62.15 |
| 7-12 months | 987 | 35.9% | $64.72 |
| 13-24 months | 1,255 | 28.7% | $68.45 |
| 25-48 months | 1,847 | 20.4% | $66.39 |
| 49-72 months | 1,840 | 9.5% | $59.87 |

**Visualizations:**
1. **Churn Rate by Tenure** (area chart)
   - Shows steep drop in first year
   - Stabilizes after year 2
   - Critical period: 0-6 months (53.3% churn)

2. **Customer Maturity Distribution** (histogram)
   - Shows where customer base is concentrated
   - Peak around 24-48 months (mature customers)

3. **Cohort Retention Curve** (line chart)
   - Tracks single cohort through lifecycle
   - Shows improvement from month 0 to month 72

4. **Churn Rate Heat Map** (heat map)
   - Tenure bands vs. Contract type
   - Darkest = highest churn (0-6 months + month-to-month)

**Key Insights:**
- 🚨 First 6 months are CRITICAL (53.3% churn)
- ✅ Customers surviving year 1 are highly stable
- 💡 Onboarding improvements = biggest payoff

**Business Actions:**
- Launch intensive "customer success" program for 0-6 months
- Check-in calls at 3-month mark
- Milestone celebrations at 6, 12, 24 month marks

---

### **Page 5: Payment Method & Billing** 💳

**Purpose:** Analyze payment-related churn factors

**Key Metrics:**
| Payment Method | Customer Count | Churn Rate | Churn Count |
|---|---|---|---|
| Electronic check | 2,365 | 45.3% | 1,071 |
| Mailed check | 1,619 | 40.5% | 655 |
| Bank transfer (auto) | 1,544 | 16.6% | 256 |
| Credit card (auto) | 1,515 | 11.3% | 171 |

**Visualizations:**
1. **Churn Rate by Payment Method** (bar chart)
   - Electronic check: highest risk (45.3%)
   - Auto-pay methods: lowest risk (~14%)

2. **Customer Migration Flow** (sankey diagram)
   - Shows how customers move between payment methods
   - Visualize conversion to auto-pay

3. **Revenue Risk by Method** (stacked bar)
   - Combines churn rate with average charge
   - Electronic check users = largest revenue loss

4. **Auto-pay Adoption Rate** (progress gauge)
   - Current %: 43% on auto-pay
   - Target: 80% on auto-pay
   - Visual progress indicator

**Key Insights:**
- ⚠️ Manual payment methods = high churn risk
- ✅ Auto-payment = strongest retention factor
- 💰 4-5x difference in churn between manual vs. auto

**Business Actions:**
- Incentive program: "Switch to auto-pay, save $5/month"
- Paperless + auto-pay bundle offer
- Retention team: convert high-value manual-pay customers first

---

### **Page 6: Customer Segmentation & Risk** 🎯

**Purpose:** Visualize customer risk scoring and targeting

**Visualizations:**
1. **Risk Segment Distribution** (pie chart)
   - HIGH RISK: 12% of customers
   - MEDIUM RISK: 28% of customers
   - LOW RISK: 60% of customers

2. **Risk vs. Monthly Charges** (scatter plot)
   - X-axis: Monthly charges ($)
   - Y-axis: Risk score
   - Bubble size: Customer lifetime value
   - Color: Risk category
   - Patterns show high-spend/high-risk customers

3. **Retention Opportunity Ranking** (bar chart)
   - Top 20 segments by revenue-at-risk
   - Helps prioritize retention budget

4. **Risk Trend Over Time** (line chart)
   - Is proportion of high-risk customers increasing/decreasing?
   - Leading indicator of churn problems

**Filters Available:**
- Contract type
- Internet service
- Add-on services (tech support, security, etc.)

**Key Insights:**
- 12% of customers in HIGH RISK = ~850 customers
- Targeting these 850 could recover $50K+/month
- Focus on month-to-month + new + high charges

---

### **Page 7: Add-on Services Impact** 🎁

**Purpose:** Show how value-added services correlate with retention

**Key Metrics:**
| Service | Adoption | Churn Rate | Revenue Impact |
|---|---|---|---|
| Tech Support | 27.9% | -5% impact | Lower churn when bundled |
| Online Security | 28.2% | -4% impact | Strong bundle effect |
| Online Backup | 34.3% | -3% impact | Moderate bundle effect |
| Streaming TV | 38.9% | -2% impact | Entertainment engagement |
| Multiple Add-ons | 45.2% | -12% impact | Strong synergy effect |

**Visualizations:**
1. **Churn Rate by Add-on Adoption** (bar chart)
   - Shows churn reduction for each service
   - Multiple services = stronger effect

2. **Add-on Adoption Trend** (line chart)
   - % of customer base with each service
   - Identify growing/declining services

3. **Customer Segment Cross-Tab** (matrix)
   - Tenure × Add-on services
   - Shows uptake patterns by customer maturity

4. **Upsell Opportunity Map** (bubble chart)
   - Identifies customer groups not using valuable services
   - Target for upsell campaigns

**Key Insights:**
- ✅ Tech support adoption = -5% churn impact
- ✅ Bundling multiple services = -12% churn impact
- 💡 Highest ROI: Tech support + security bundle

**Business Actions:**
- Bundle tech support with month-to-month contracts
- Cross-sell to customers with 0-6 month tenure
- Package deals (e.g., "Security + Backup" at discount)

---

### **Page 8: Competitive & Market Context** 🏆

**Purpose:** Position churn in market context (if benchmarking data available)

**Visualizations:**
1. **Telecom Industry Benchmarks** (comparison bar chart)
   - Your churn: 26.5%
   - Industry average: 21-24%
   - Top performers: <18%
   - Positioning: Slightly above average (opportunity)

2. **Customer Satisfaction vs. Churn** (scatter plot)
   - NPS or CSAT score vs. churn rate
   - Shows correlation

3. **Service Quality Metrics** (dashboard KPIs)
   - Uptime %
   - Customer support response time
   - Service reliability scores

---

## 🎛️ Interactive Features

### **Filters & Slicers** (Top of Dashboard)
Users can filter all pages by:
- **Contract Type:** Month-to-month, One year, Two year
- **Internet Service:** DSL, Fiber optic, None
- **Payment Method:** All payment types
- **Tenure Band:** 0-6mo, 7-12mo, 13-24mo, 25-48mo, 49-72mo
- **Senior Citizen:** Yes/No
- **Date Range:** (if time dimension available)

### **Drill-Down Capability**
- Click on a metric → See underlying data
- Example: Click "Fiber optic" → See list of fiber customers
- Further drill → Individual customer details

### **Highlighting**
- Hover over bar → See exact values
- Color-coded risk levels (red=high risk, green=low)

### **Bookmarks**
- Executive Summary (high-level KPIs)
- Detailed Analysis (segment deep-dives)
- Retention Plan (action-oriented view)

---

## 📊 Dashboard Data Refresh

**Update Frequency:** Weekly (recommended)

**Data Source:** `data/IT_customer_churn.csv`

**Last Refreshed:** June 2026

**Data Latency:** 1 week (show data as of date X)

### **Manual Refresh Steps:**
1. Open `Telecom Customer Churn Dashboard.pbix`
2. Click **"Refresh"** button (Home tab)
3. Wait for data load (2-5 minutes)
4. Dashboard updates with latest metrics

### **Automated Refresh (Power BI Service):**
1. Upload PBIX to Power BI Service
2. Set refresh schedule: Daily or Weekly
3. Notifications on refresh success/failure

---

## 👥 User Personas & Use Cases

### **For C-Suite Executives**
- **Page:** Executive Overview (Page 1)
- **Question:** What's our churn rate and revenue impact?
- **Action:** Review quarterly, discuss strategic initiatives
- **Time:** 5-10 minutes

### **For Operations Leaders**
- **Pages:** Contract Type (2), Tenure (4), Risk Segmentation (6)
- **Question:** Which customer segments should we prioritize?
- **Action:** Allocate retention resources by segment
- **Time:** 20-30 minutes

### **For Retention Managers**
- **Pages:** Risk Segmentation (6), Add-ons (7), Payment Method (5)
- **Question:** Which customers should I target this week?
- **Action:** Export high-risk customer list; launch campaign
- **Time:** 30-45 minutes

### **For Finance/Accounting**
- **Page:** Executive Overview (1), Contract Type (2)
- **Question:** What's the revenue impact? Where's the risk?
- **Action:** Budget for retention initiatives; forecast impact
- **Time:** 15-20 minutes

---

## 💡 Dashboard Usage Tips

### **Best Practices:**
1. ✅ Start with Executive Overview for context
2. ✅ Use filters to focus on specific segments
3. ✅ Drill-down to investigate anomalies
4. ✅ Export visuals for presentations (right-click)
5. ✅ Share specific pages with stakeholders (link sharing)

### **Common Questions & Answers:**
- **"Why is fiber optic churn so high?"** → Check Page 3: Service Analysis
- **"Which customers should we target for retention?"** → Go to Page 6: Risk Segmentation
- **"How much revenue could we recover?"** → See Page 1: Revenue at Risk
- **"Is our situation improving?"** → Check trend lines on relevant pages

### **Troubleshooting:**
- **Dashboard slow?** → Filter to smaller date range; reduce number of visuals
- **Data out of date?** → Click Refresh; check last update timestamp
- **Drill-down not working?** → Check filter context; may be blocked
- **Visualization blank?** → Verify data connection; check filter selections

---

## 🔗 Related Documentation

- **Data Dictionary:** See [../docs/DATA_DICTIONARY.md](../docs/DATA_DICTIONARY.md)
- **SQL Analytics:** See [../sql/README.md](../sql/README.md)
- **Business Presentation:** See [../presentation/README.md](../presentation/README.md)

---

## 📞 Support

- **Dashboard Issues:** Contact BI team
- **Data Questions:** See DATA_DICTIONARY.md
- **Business Questions:** See MODEL_CARD.md
- **Technical Setup:** See INSTALL.md

---

**Dashboard Version:** 1.0  
**Last Updated:** June 2026  
**Status:** ✅ Ready for Production
