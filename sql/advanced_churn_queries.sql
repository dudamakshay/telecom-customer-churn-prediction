-- ============================================================
-- TELECOM CHURN — ADVANCED SQL QUERY LIBRARY (UPGRADED)
-- Includes: Window Functions, Segmentation, Revenue Analysis
-- Compatible: PostgreSQL | MySQL 8+ | SQL Server
-- ============================================================


-- ══════════════════════════════════════════════════════════════
-- SECTION A: REVENUE IMPACT ANALYSIS
-- ══════════════════════════════════════════════════════════════

-- A1: Full Revenue Impact Summary
SELECT
    COUNT(*)                                                       AS total_customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)                  AS churned_count,
    SUM(CASE WHEN Churn='No'  THEN 1 ELSE 0 END)                  AS retained_count,
    ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
          / COUNT(*), 2)                                           AS churn_rate_pct,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END), 2)  AS monthly_rev_lost,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END)*12, 2) AS annual_rev_lost,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN TotalCharges ELSE 0 END), 2)   AS lifetime_rev_lost
FROM customer_churn;
-- Result: 7043 customers | 26.54% churn | $139,131 monthly lost | $1,669,572 annual


-- A2: Revenue Lost by Contract Type (Priority Ranking)
SELECT
    Contract,
    COUNT(*)                                                       AS total_customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)                  AS churned,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END), 2) AS monthly_rev_lost,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END)*12, 2) AS annual_rev_lost,
    ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
          / COUNT(*), 2)                                           AS churn_rate_pct,
    RANK() OVER (ORDER BY SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END) DESC)
                                                                   AS revenue_priority_rank
FROM customer_churn
GROUP BY Contract
ORDER BY monthly_rev_lost DESC;


-- A3: Revenue Lost by Internet Service
SELECT
    InternetService,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)                  AS churned_customers,
    ROUND(AVG(CASE WHEN Churn='Yes' THEN MonthlyCharges END), 2)  AS avg_churned_bill,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END), 2) AS monthly_rev_lost,
    ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
          / COUNT(*), 2)                                           AS churn_rate_pct
FROM customer_churn
GROUP BY InternetService
ORDER BY monthly_rev_lost DESC;
-- Fiber Optic: 1297 churned | $91.50 avg bill | $63,932/month lost


-- ══════════════════════════════════════════════════════════════
-- SECTION B: WINDOW FUNCTIONS
-- ══════════════════════════════════════════════════════════════

-- B1: Running Total of Revenue Lost (by Tenure)
SELECT
    tenure,
    COUNT(*)                                                        AS customers,
    SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END)      AS monthly_loss_this_tenure,
    SUM(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END))
        OVER (ORDER BY tenure ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
                                                                    AS running_total_loss
FROM customer_churn
GROUP BY tenure
ORDER BY tenure;


-- B2: Rank Customers by Monthly Charges Within Each Contract Type
SELECT
    customerID,
    Contract,
    MonthlyCharges,
    Churn,
    RANK() OVER (PARTITION BY Contract ORDER BY MonthlyCharges DESC) AS rank_in_contract,
    ROUND(AVG(MonthlyCharges) OVER (PARTITION BY Contract), 2)      AS avg_charge_in_contract,
    MonthlyCharges - AVG(MonthlyCharges) OVER (PARTITION BY Contract) AS diff_from_avg
FROM customer_churn
ORDER BY Contract, rank_in_contract;


-- B3: Percentile Ranking of Each Customer by Monthly Charge
SELECT
    customerID,
    MonthlyCharges,
    Churn,
    ROUND(PERCENT_RANK() OVER (ORDER BY MonthlyCharges) * 100, 1)  AS charge_percentile,
    NTILE(4) OVER (ORDER BY MonthlyCharges)                         AS charge_quartile,
    CASE NTILE(4) OVER (ORDER BY MonthlyCharges)
        WHEN 1 THEN 'Low Spender'
        WHEN 2 THEN 'Mid Spender'
        WHEN 3 THEN 'High Spender'
        WHEN 4 THEN 'Premium Spender'
    END                                                             AS spend_segment
FROM customer_churn
ORDER BY charge_percentile DESC;


-- B4: Churn Rate vs Previous Tenure Band (LAG comparison)
WITH tenure_summary AS (
    SELECT
        CASE
            WHEN tenure BETWEEN 0  AND 6  THEN '01_0-6mo'
            WHEN tenure BETWEEN 7  AND 12 THEN '02_7-12mo'
            WHEN tenure BETWEEN 13 AND 24 THEN '03_13-24mo'
            WHEN tenure BETWEEN 25 AND 48 THEN '04_25-48mo'
            ELSE '05_49-72mo'
        END                                                         AS tenure_band,
        COUNT(*)                                                    AS total,
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)               AS churned,
        ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) / COUNT(*), 1)
                                                                    AS churn_rate_pct
    FROM customer_churn
    GROUP BY tenure_band
)
SELECT
    tenure_band,
    total,
    churned,
    churn_rate_pct,
    LAG(churn_rate_pct) OVER (ORDER BY tenure_band)                 AS prev_band_churn_rate,
    churn_rate_pct - LAG(churn_rate_pct) OVER (ORDER BY tenure_band)
                                                                    AS churn_rate_change
FROM tenure_summary
ORDER BY tenure_band;
-- Shows how churn DROPS as tenure increases: 53.3% → 35.9% → 28.7% → 20.4% → 9.5%


-- B5: Top 3 Highest-Paying Churned Customers Per Contract Type
SELECT *
FROM (
    SELECT
        customerID,
        Contract,
        MonthlyCharges,
        TotalCharges,
        tenure,
        PaymentMethod,
        ROW_NUMBER() OVER (PARTITION BY Contract ORDER BY MonthlyCharges DESC) AS rn
    FROM customer_churn
    WHERE Churn = 'Yes'
) ranked
WHERE rn <= 3
ORDER BY Contract, rn;


-- ══════════════════════════════════════════════════════════════
-- SECTION C: CUSTOMER SEGMENTATION
-- ══════════════════════════════════════════════════════════════

-- C1: Full Risk Segmentation Model
SELECT
    customerID,
    Contract,
    tenure,
    MonthlyCharges,
    InternetService,
    TechSupport,
    OnlineSecurity,
    PaymentMethod,
    Churn,
    -- Risk Score (higher = more at risk)
    (
        CASE Contract WHEN 'Month-to-month' THEN 40 WHEN 'One year' THEN 15 ELSE 0 END
      + CASE WHEN tenure <= 6   THEN 30 WHEN tenure <= 12 THEN 20
             WHEN tenure <= 24  THEN 10 ELSE 0 END
      + CASE WHEN MonthlyCharges > 80 THEN 20 WHEN MonthlyCharges > 60 THEN 10 ELSE 0 END
      + CASE TechSupport    WHEN 'No' THEN 5 ELSE 0 END
      + CASE OnlineSecurity WHEN 'No' THEN 5 ELSE 0 END
      + CASE PaymentMethod  WHEN 'Electronic check' THEN 10 ELSE 0 END
    )                                                              AS risk_score,
    CASE
        WHEN (
            CASE Contract WHEN 'Month-to-month' THEN 40 WHEN 'One year' THEN 15 ELSE 0 END
          + CASE WHEN tenure <= 6 THEN 30 WHEN tenure <= 12 THEN 20
                 WHEN tenure <= 24 THEN 10 ELSE 0 END
          + CASE WHEN MonthlyCharges > 80 THEN 20 WHEN MonthlyCharges > 60 THEN 10 ELSE 0 END
          + CASE TechSupport WHEN 'No' THEN 5 ELSE 0 END
          + CASE OnlineSecurity WHEN 'No' THEN 5 ELSE 0 END
          + CASE PaymentMethod WHEN 'Electronic check' THEN 10 ELSE 0 END
        ) >= 70 THEN 'HIGH RISK — Immediate Action'
        WHEN (
            CASE Contract WHEN 'Month-to-month' THEN 40 WHEN 'One year' THEN 15 ELSE 0 END
          + CASE WHEN tenure <= 6 THEN 30 WHEN tenure <= 12 THEN 20
                 WHEN tenure <= 24 THEN 10 ELSE 0 END
          + CASE WHEN MonthlyCharges > 80 THEN 20 WHEN MonthlyCharges > 60 THEN 10 ELSE 0 END
          + CASE TechSupport WHEN 'No' THEN 5 ELSE 0 END
          + CASE OnlineSecurity WHEN 'No' THEN 5 ELSE 0 END
          + CASE PaymentMethod WHEN 'Electronic check' THEN 10 ELSE 0 END
        ) >= 40 THEN 'MEDIUM RISK — Monitor Closely'
        ELSE 'LOW RISK — Stable'
    END                                                            AS risk_label
FROM customer_churn
ORDER BY risk_score DESC;


-- C2: Segment Summary — Count & Revenue by Risk Level
WITH risk_cte AS (
    SELECT
        customerID,
        MonthlyCharges,
        Churn,
        CASE
            WHEN Contract = 'Month-to-month' AND tenure <= 12
                 AND MonthlyCharges > 65 THEN 'HIGH RISK'
            WHEN Contract = 'Month-to-month' AND tenure <= 24 THEN 'MEDIUM RISK'
            ELSE 'LOW RISK'
        END AS risk_label
    FROM customer_churn
)
SELECT
    risk_label,
    COUNT(*)                                                       AS total_customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)                  AS already_churned,
    ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
          / COUNT(*), 1)                                           AS churn_rate_pct,
    ROUND(SUM(MonthlyCharges), 2)                                  AS total_monthly_revenue,
    ROUND(AVG(MonthlyCharges), 2)                                  AS avg_monthly_charge
FROM risk_cte
GROUP BY risk_label
ORDER BY churn_rate_pct DESC;


-- C3: Payment Method Risk Analysis
SELECT
    PaymentMethod,
    COUNT(*)                                                       AS total,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)                  AS churned,
    ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
          / COUNT(*), 1)                                           AS churn_rate_pct,
    ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END), 2) AS monthly_rev_lost,
    CASE
        WHEN ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
                   / COUNT(*), 1) >= 40 THEN '🔴 Critical'
        WHEN ROUND(100.0 * SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
                   / COUNT(*), 1) >= 20 THEN '🟡 Monitor'
        ELSE '🟢 Stable'
    END AS status
FROM customer_churn
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;
-- Electronic check: 45.3% churn rate — CRITICAL


-- ══════════════════════════════════════════════════════════════
-- SECTION D: EXECUTIVE REPORT QUERIES
-- ══════════════════════════════════════════════════════════════

-- D1: Monthly Churn Dashboard (One-Query Executive Summary)
SELECT
    'Total Customers'     AS metric, CAST(COUNT(*) AS VARCHAR)                AS value FROM customer_churn
UNION ALL SELECT
    'Churned Customers',  CAST(SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS VARCHAR) FROM customer_churn
UNION ALL SELECT
    'Churn Rate %',       CAST(ROUND(100.0*SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)/COUNT(*),2) AS VARCHAR) FROM customer_churn
UNION ALL SELECT
    'Monthly Rev Lost $', CAST(ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END),0) AS VARCHAR) FROM customer_churn
UNION ALL SELECT
    'Annual Rev at Risk', CAST(ROUND(SUM(CASE WHEN Churn='Yes' THEN MonthlyCharges ELSE 0 END)*12,0) AS VARCHAR) FROM customer_churn;
