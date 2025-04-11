import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
print("Current working directory:", os.getcwd())
# Load the dataset (make sure pokemon.csv is in the same directory)
df = pd.read_csv("/Users/giancarlourselli/python_decal/giancarlo_decal/quiz/pokemon.csv")

# Create a 1x2 subplot layout
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Scatter plot of Attack vs Defense
axes[0].scatter(df['Attack'], df['Defense'], color='orange')
axes[0].set_title('Attack vs Defense for Pokemon')
axes[0].set_xlabel('Attack')
axes[0].set_ylabel('Defense')

# Plot 2: Countplot of Generation
sns.countplot(x='Generation', data=df, ax=axes[1])
axes[1].set_title('Generations of Pokemon')
axes[1].set_xlabel('Generation')
axes[1].set_ylabel('Count')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
