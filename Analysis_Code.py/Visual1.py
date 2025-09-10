import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv(r"C:\Users\HP\Desktop\kanchan\Python data analytics file\Newfile.csv")

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Fraud_Flag', palette=['green','red'])
plt.title("Fraud vs Non-Fraud Transactions")
plt.xlabel("Fraud Flag (0 = Legit, 1 = Fraud)")
plt.ylabel("Number of Transactions")

# Add values on bars
ax = plt.gca()
for p in ax.patches:
    ax.annotate(f"{p.get_height()}", (p.get_x()+p.get_width()/2, p.get_height()+5), 
                ha='center')
plt.savefig("C:\\Users\\HP\\Desktop\\kanchan\\Python_SQL_Project\\luxury-retail-fraud-detection\\images\\fraud_vs_nonfraud.png")
plt.show()



# -----------------------------
# Insight:
# - Legitimate Transactions (Fraud_Flag = 0): 2067
# - Fraudulent Transactions (Fraud_Flag = 1): 66
#
# Interpretation:
# The dataset is highly imbalanced.
# Legitimate transactions dominate (97% approx),
# while fraud cases are very rare (~3%).
# This mirrors real-world fraud detection challenges 
# where fraud is rare but very important to catch.
# --