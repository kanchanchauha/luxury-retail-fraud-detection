
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df = pd.read_csv(r"C:\Users\HP\Desktop\kanchan\Python data analytics file\Newfile.csv")
# Fraud by Payment Method (Pie Chart)
fraud_payment = df[df['Fraud_Flag']==1]['Payment_Method'].value_counts()

plt.figure(figsize=(6,6))
fraud_payment.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3')
plt.title("Fraud by Payment Method")
plt.ylabel("")
plt.savefig("C:\\Users\\HP\\Desktop\\kanchan\\Python_SQL_Project\\luxury-retail-fraud-detection\\images\\Fraud by Payment Method.png")
plt.show()


# -----------------------------
# Insight:
# - The highest fraud cases occur with **Debit Card transactions**.  
# - Unexpectedly, **Gift Card** ranks second in fraud cases.  
# - **Mobile Payments** come third, showing significant vulnerability.  
#
# Interpretation:
# - Debit Cards may be more vulnerable due to wider usage and weaker real-time checks.  
# - Gift Cards being the second highest is unusual and may suggest exploitation 
#   through anonymous or unmonitored purchases.  
# - Mobile Payments, while convenient, also show notable fraud risk, 
#   which highlights the need for stronger authentication.  
# -----------------------------

