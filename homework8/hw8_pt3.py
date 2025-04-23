import seaborn as sns
import matplotlib.pyplot as plt

#1.
penguins = sns.load_dataset("penguins")

#2. 
fig, axes = plt.subplots(1, 2, figsize=(14,15))

#3.
sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=axes[0])
axes[0].set_title("Bill Length vs Bill Depth")
axes[0].set_xlabel("Length (mm)")
axes[0].set_ylabel("Depth (mm)")
axes[0].legend(title="Species")

#4.
sns.histplot(data=penguins, x="body_mass_g", bins=20, kde=True, ax=axes[1])
axes[1].set_title("Distribution of BM")
axes[1].set_xlabel("BM")
axes[1].set_ylabel("N")

plt.tight_layout()
plt.show()