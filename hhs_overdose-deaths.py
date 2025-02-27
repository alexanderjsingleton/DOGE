import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set theme for better visuals
sns.set_theme(style="whitegrid")

# Load the dataset
file_path = "Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States.csv"
df = pd.read_csv(file_path)

# Display dataset info
print(df.info())

# Show the first few rows
print(df.head())

# Filter for "All drug overdose deaths"
df_overall = df[df["PANEL"] == "All drug overdose deaths"]

# Plot Overdose Death Rates Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_overall, x="YEAR", y="ESTIMATE", hue="STUB_LABEL", marker="o")

plt.title("Drug Overdose Death Rates Over Time (All Persons)")
plt.xlabel("Year")
plt.ylabel("Deaths per 100,000 Population")
plt.legend(title="Demographic Group")
plt.grid()
plt.show()
