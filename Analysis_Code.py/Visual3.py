
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv(r"C:\Users\HP\Desktop\kanchan\Python data analytics file\Newfile.csv")

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Customer_Age', y='Purchase_Amount', hue='Fraud_Flag', alpha=0.7, palette=['green','red'])
plt.title("Customer Age vs Purchase Amount (Fraud vs Legit)")
plt.xlabel("Customer Age")
plt.ylabel("Purchase Amount")
plt.savefig("C:\\Users\\HP\\Desktop\\kanchan\\Python_SQL_Project\\luxury-retail-fraud-detection\\images\\Customer Age vs Purchase Amount (Fraud vs Legit).png")
plt.show()


# -----------------------------
# Insight:
# - Fraudulent transactions are more common in younger to middle-aged customers.  
# - Older age groups show fewer fraud cases compared to younger ones.  
#
# Interpretation:
# Fraud detection strategies may need to focus more on transactions involving 
# younger customers, as they appear riskier. Older customers are less represented 
# in fraud cases, suggesting either lower activity levels or reduced targeting.
# -----------------------------