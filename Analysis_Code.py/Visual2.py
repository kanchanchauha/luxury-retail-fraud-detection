
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv(r"C:\Users\HP\Desktop\kanchan\Python data analytics file\Newfile.csv")

# Fraud by Loyalty Tier (Bar Plot)

plt.figure(figsize=(8,5))
fraud_by_tier = df.groupby('Customer_Loyalty_Tier')['Fraud_Flag'].sum()

plt.figure(figsize=(7,5))
fraud_by_tier.plot.bar(color='Orange')
plt.xlabel('Loyalty Tier')
plt.ylabel('Number of Fraud Cases')
plt.title('Fraud Count by Loyalty Tier')
plt.savefig("C:\\Users\\HP\\Desktop\\kanchan\\Python_SQL_Project\\luxury-retail-fraud-detection\\images\\Fraud Count by Loyalty Tier.png")
plt.show()

# -----------------------------
# Insight:
# - Bronze customers show the highest number of fraud cases.
# - Top 3 tiers with fraud counts: Bronze > Silver > Gold.
#
# Interpretation:
# Fraud risk appears concentrated in lower to mid-tier loyalty groups. 
# This may suggest:
#   1. Fraudsters are more likely to target customers with weaker loyalty status. 
#   2. Higher loyalty tiers (Platinum, Diamond, etc.) have fewer fraud cases,
#      possibly due to stricter monitoring or stronger verification processes.
# -----------------------------