-- ==========================================================
-- 🚀 Fraud Analysis Project (MySQL)
-- ==========================================================

-- ===============================
-- 📌 Step 1: Database Setup
-- ===============================
CREATE DATABASE IF NOT EXISTS fraud_analysis;
USE fraud_analysis;

-- Import File
-- Preview dataset
SELECT * FROM newfile LIMIT 10;

-- ===============================
-- 🛠 Step 2: Data Cleaning
-- ===============================
-- Convert Transaction_Time to proper TIME format
UPDATE newfile
SET Transaction_Time = STR_TO_DATE(Transaction_Time, '%H:%i:%s');

-- Change column type to TIME
ALTER TABLE newfile
MODIFY COLUMN Transaction_Time TIME;

-- ===============================
-- 📊 Step 3: Basic Data Exploration
-- ===============================

-- 1. Total transactions
SELECT COUNT(*) AS total_transactions
FROM newfile;

-- 2. Missing Customer Age values
SELECT COUNT(*) AS missing_customer_age
FROM newfile
WHERE Customer_Age IS NULL;

-- 3. Unique Customers and Stores
SELECT COUNT(DISTINCT Customer_ID) AS unique_customers,
       COUNT(DISTINCT Store_ID) AS unique_stores
FROM newfile;

-- ===============================
-- 🚨 Step 4: Fraud Detection Insights
-- ===============================

-- 4. Fraud vs Non-Fraud
SELECT Fraud_Flag, COUNT(*) AS transaction_count
FROM newfile
GROUP BY Fraud_Flag;

-- 5. Fraud by Payment Method
SELECT Payment_Method, 
       SUM(Fraud_Flag) AS fraud_transactions,
       COUNT(*) AS total_transactions,
       ROUND(SUM(Fraud_Flag) * 100.0 / COUNT(*), 2) AS fraud_rate_percent
FROM newfile
GROUP BY Payment_Method
ORDER BY fraud_rate_percent DESC;

-- 6. Fraud by Location
SELECT Location,
       SUM(Fraud_Flag) AS fraud_transactions,
       COUNT(*) AS total_transactions
FROM newfile
GROUP BY Location
ORDER BY fraud_transactions DESC;

-- ===============================
-- 👥 Step 5: Customer Behavior
-- ===============================

-- 7. Average spend by Loyalty Tier
SELECT Customer_Loyalty_Tier,
       ROUND(AVG(Purchase_Amount), 2) AS avg_spend
FROM newfile
GROUP BY Customer_Loyalty_Tier;

-- 8. Age group fraud patterns
SELECT CASE 
          WHEN Customer_Age < 25 THEN 'Under 25'
          WHEN Customer_Age BETWEEN 25 AND 40 THEN '25-40'
          WHEN Customer_Age BETWEEN 41 AND 60 THEN '41-60'
          ELSE '60+'
       END AS Age_Group,
       SUM(Fraud_Flag) AS fraud_cases,
       COUNT(*) AS total_transactions
FROM newfile
GROUP BY Age_Group
ORDER BY fraud_cases DESC;

-- ===============================
-- 📈 Step 6: Trend Analysis
-- ===============================

-- 9. High-Risk Transactions Trend (by Month)
SELECT MONTHNAME(Transaction_Date) AS month,
       SUM(High_Risk_Transaction) AS high_risk_count
FROM newfile
GROUP BY MONTH(Transaction_Date), MONTHNAME(Transaction_Date)
ORDER BY MONTH(Transaction_Date);

-- 10. Fraud & High-Risk Overlap
SELECT SUM(CASE WHEN Fraud_Flag = 1 THEN 1 ELSE 0 END) AS frauds,
       SUM(CASE WHEN High_Risk_Transaction = 1 THEN 1 ELSE 0 END) AS high_risk,
       SUM(CASE WHEN Fraud_Flag = 1 AND High_Risk_Transaction = 1 THEN 1 ELSE 0 END) AS fraud_high_risk_overlap
FROM newfile;

-- ===============================
-- 🏬 Step 7: Store Performance
-- ===============================

-- 11. Average Footfall by Store
SELECT Store_ID, AVG(Footfall_Count) AS avg_footfall
FROM newfile
GROUP BY Store_ID
ORDER BY avg_footfall DESC;

-- 12. Store Performance with Fraud %
SELECT Store_ID,
       COUNT(*) AS total_transactions,
       SUM(Fraud_Flag) AS fraud_transactions,
       ROUND(SUM(Fraud_Flag) * 100.0 / COUNT(*), 2) AS fraud_percent
FROM newfile
GROUP BY Store_ID
ORDER BY fraud_percent DESC;
