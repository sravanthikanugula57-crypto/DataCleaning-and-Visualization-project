import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("ecommerce.csv")

# -----------------------------
# Show First 5 Rows
# -----------------------------
print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# Dataset Information
# -----------------------------
print("\nDataset Info:")
print(df.info())

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Remove Missing Values
# -----------------------------
df.dropna(inplace=True)

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Show Column Names
# -----------------------------
print("\nColumn Names:")
print(df.columns)

# -----------------------------
# Total Yearly Sales
# -----------------------------
total_sales = (
    df['sales_month_1'].sum() +
    df['sales_month_2'].sum() +
    df['sales_month_3'].sum() +
    df['sales_month_4'].sum() +
    df['sales_month_5'].sum() +
    df['sales_month_6'].sum() +
    df['sales_month_7'].sum() +
    df['sales_month_8'].sum() +
    df['sales_month_9'].sum() +
    df['sales_month_10'].sum() +
    df['sales_month_11'].sum() +
    df['sales_month_12'].sum()
)

print("\nTotal Yearly Sales:", total_sales)

# -----------------------------
# Average Review Score
# -----------------------------
average_review = df['review_score'].mean()

print("\nAverage Review Score:", average_review)

# -----------------------------
# Sales by Category
# -----------------------------
sales_by_category = df.groupby('category')['sales_month_1'].sum()

print("\nSales by Category:")
print(sales_by_category)

# =========================================================
# VISUALIZATION 1 : BAR CHART
# =========================================================
sales_by_category.plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

# =========================================================
# VISUALIZATION 2 : HISTOGRAM
# =========================================================
plt.hist(df['price'])

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")

plt.show()

# =========================================================
# VISUALIZATION 3 : SCATTER PLOT
# =========================================================
sns.scatterplot(
    x='price',
    y='review_score',
    data=df
)

plt.title("Price vs Review Score")

plt.show()

# =========================================================
# VISUALIZATION 4 : HEATMAP
# =========================================================
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("cleaned_ecommerce.csv", index=False)

print("\nCleaned dataset saved successfully!")