import pandas as pd
import matplotlib.pyplot as plt

#1.
df = pd.read_csv('/Users/giancarlourselli/python_decal/giancarlo_decal/homework8/stars.csv')

#2.
print("first five rows")
print(df.head())

print("\nNumber of rows and columns:")
print(df.shape)

print("\n Column names and data types")
print(df.dtypes)

#3.
print("\nAverage mass:", df['Mass (M☉)'].mean())
print("Average temperature:", df['Temperature'].mean())

print("\nStar with largest radius:")
print(df.loc[df['radius (R☉)'].idmax()])

print("\nNumber of M-type stars (Spectral_Type starts with M):")
m_stars = df[df['Spectral_Type'].str.startswith('M')]
print(len(m_stars))

#4.
print("3 closest stars by distance:")
print(df.sort_values(by = "Distance(ly)").head(3))

#5.
m_stars.to_csv ("m_type_stars.cv", index=False)

plt.figure(figsize=(8, 5))
plt.hist(df["temperature"], bins=10)
plt.title("temperature distribution of stars")
plt.xlabel("temperature (K)")
plt.ylabel("number of Stars")
plt.grid(True)
plt.show()