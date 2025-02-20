import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("/Users/alexanderjsingleton_macmini/doge_analysis/10L_VetPop2023_118th_Congress_NCVAS.csv", skiprows=5)

# Drop empty/unnecessary columns
df = df.drop(columns=["Unnamed: 5"], errors="ignore")

# Forward-fill missing states
df["State"] = df["State"].ffill()

# Convert numeric columns to float
numeric_cols = ["Under 65", "65 and Over", "Grand Total"]
for col in numeric_cols:
    if df[col].dtype == "object":  # Only clean if needed
        df[col] = df[col].str.replace(",", "").astype(float)

# Aggregate data by state (sum across congressional districts)
df_statewise = df.groupby("State", as_index=False)[["Under 65", "65 and Over", "Grand Total"]].sum()

# Display the first few rows
print(df_statewise.head())

# Set theme for better visuals
sns.set_theme(style="whitegrid")

### 🔹 1. Bar Chart - Veteran Population by State (Split by Age Group)
plt.figure(figsize=(14, 6))
df_melted = df_statewise.melt(id_vars=["State"], value_vars=["Under 65", "65 and Over"], var_name="Age Group", value_name="Population")
sns.barplot(data=df_melted, x="State", y="Population", hue="Age Group")

plt.xticks(rotation=90)
plt.title("Veteran Population by State (Age Group Comparison)")
plt.xlabel("State")
plt.ylabel("Total Veterans")
plt.legend(title="Age Group")
plt.grid()
plt.show()

### 📊 2. Pie Chart - Top 10 States by Veteran Population
top_10_states = df_statewise.nlargest(10, "Grand Total")
plt.figure(figsize=(8, 8))
plt.pie(top_10_states["Grand Total"], labels=top_10_states["State"], autopct="%1.1f%%", startangle=140)
plt.title("Top 10 States with Largest Veteran Population")
plt.show()

### 📈 3. Line Chart - Comparing Under 65 vs. 65 and Over Population by State
plt.figure(figsize=(14, 6))
sns.lineplot(data=df_statewise, x="State", y="Under 65", marker="o", label="Under 65")
sns.lineplot(data=df_statewise, x="State", y="65 and Over", marker="s", label="65 and Over")

plt.xticks(rotation=90)
plt.title("Veteran Population Age Comparison by State")
plt.xlabel("State")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.show()

### 🏛️ 4. Highlighting the Top 5 and Bottom 5 States
df_sorted = df_statewise.sort_values("Grand Total", ascending=False)
top_5 = df_sorted.head(5)
bottom_5 = df_sorted.tail(5)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_5, x="State", y="Grand Total", color="green", label="Top 5 States")
sns.barplot(data=bottom_5, x="State", y="Grand Total", color="red", label="Bottom 5 States")

plt.title("Top 5 vs. Bottom 5 States by Veteran Population")
plt.xlabel("State")
plt.ylabel("Total Veterans")
plt.legend()
plt.grid()
plt.show()
