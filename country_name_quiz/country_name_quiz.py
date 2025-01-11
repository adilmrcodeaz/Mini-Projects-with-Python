import pandas as pd

# Option 1: If the file is in the same directory, make sure it's named exactly "country.csv"
df = pd.read_csv("country.csv")

# Option 2: Use the full path (replace with your actual path)
# df = pd.read_csv("C:/Users/YourUsername/path/to/country.csv")
# For Mac/Linux:
# df = pd.read_csv("/home/username/path/to/country.csv")

print(df.head())
