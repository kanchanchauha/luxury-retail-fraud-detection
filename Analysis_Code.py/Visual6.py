
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv(r"C:\Users\HP\Desktop\kanchan\Python data analytics file\Newfile.csv")


plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Customer_Loyalty_Tier', hue='Fraud_Flag', palette=['green','red'])
plt.title("Fraud by Customer Loyalty Tier")
plt.xlabel("Customer Loyalty Tier")
plt.ylabel("Count")
plt.legend(title="Fraud Flag", labels=["Legit","Fraud"])
plt.savefig("C:\\Users\\HP\\Desktop\\kanchan\\Python_SQL_Project\\luxury-retail-fraud-detection\\images\\Fraud by Customer Loyalty Tier.png")
plt.show()


# -----------------------------
# Insight:
# - **Bronze tier** shows the highest fraud count compared to other tiers.  
# - **Silver and Gold** also report noticeable fraud cases, but less than Bronze.  
# - Higher loyalty tiers (Platinum, Diamond, etc.) show very few fraud cases.  
#
# Interpretation:
# - Lower-tier customers (Bronze, Silver, Gold) are at **higher fraud risk**.  
# - Businesses may need **stronger fraud monitoring for lower-tier customers**,  
#   while higher-tier customers may already be better protected by stricter checks.  
# -----------------------------