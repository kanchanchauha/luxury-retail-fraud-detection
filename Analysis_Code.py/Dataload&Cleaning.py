
import pandas as pd
import numpy as np


# Step 1: Import Libraries & Load Data
df = pd.read_csv(r"C:\Users\HP\Desktop\kanchan\Python_SQL_Project\luxury-retail-fraud-detection\Data\luxury_cosmetics_fraud_analysis_2025.csv")

# Step 2: Inspect the Data
print("Head")
print(df.head())

#Info
print("info")
print(df.info())

print("describe")
#describe
print(df.describe())

print("isnullvalues")
#isnull
print(df.isnull().sum())
# Count missing values



# Step 3: Handle Missing Values
df['Customer_Age'].fillna(df['Customer_Age'].mean(), inplace=True)
df['Customer_Loyalty_Tier'].fillna("Other",inplace=True)
df['Payment_Method'].fillna("Other",inplace=True)
print("After filling missing values:")
print(df.isnull().sum()) 

# Step 4: Correct Data Types

df['Transaction_Date']=pd.to_datetime(df['Transaction_Date'])
df['Transaction_Time']=pd.to_datetime(df['Transaction_Time']).dt.time
df['Customer_Age']=df['Customer_Age'].astype(int)
print(df.info())

# Step 5: Remove Duplicates
df.drop_duplicates()
print(df.info())

# Example: Flag high-risk transactions by amount and loyalty tier
df['High_Risk_Transaction'] = np.where((df['Purchase_Amount']>5000) & (df['Customer_Loyalty_Tier']=='Bronze'), 1, 0)

# Saving 
df.to_csv(r"C:\Users\HP\Desktop\kanchan\Python data analytics file\Newfile.csv",index=False)
print("Saved CSV")

