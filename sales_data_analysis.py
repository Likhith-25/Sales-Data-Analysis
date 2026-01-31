import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load dataset
# -------------------------------
data = pd.read_excel(r"C:\Users\LikhithGowda\Desktop\sales_data.xlsx")

# -------------------------------
# 1. Monthly Sales Trend
# -------------------------------
monthly_sales = data.groupby("Month", sort=False)["Sales"].sum()

# plt.figure(figsize=(8, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Product-wise Sales
# -------------------------------
product_sales = data.groupby("Product")["Sales"].sum()

plt.bar(product_sales.index, product_sales.values,color="red")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# -------------------------------
# 3. Region-wise Sales
# -------------------------------
sns.barplot(x="Region", y="Sales", data=data, estimator=sum)
plt.title("Region-wise Sales Analysis")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()
