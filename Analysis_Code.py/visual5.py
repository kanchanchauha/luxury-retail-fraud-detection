import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv(r"C:\Users\HP\Desktop\kanchan\Python data analytics file\Newfile.csv")


plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Purchase_Amount', hue='Fraud_Flag', kde=True, palette=['green','red'], bins=30)
plt.title("Purchase Amount Distribution by Fraud Flag")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.savefig("C:\\Users\\HP\\Desktop\\kanchan\\Python_SQL_Project\\luxury-retail-fraud-detection\\images\\Purchase Amount Distribution by Fraud Flag.png")
plt.show()


# -----------------------------
# Insight:
# - Legitimate transactions (green) are spread across all purchase ranges.  
# - Fraudulent transactions (red) cluster more around **mid-to-high purchase amounts**.  
# - Very few fraud cases exist at very low purchase amounts.  
#
# Interpretation:
# Fraudsters may prefer targeting **medium to large purchases** 
# to maximize impact, while small-value fraud attempts are rare.  
# This insight can help businesses **flag high-value transactions for extra verification**.  
# -----------------------------