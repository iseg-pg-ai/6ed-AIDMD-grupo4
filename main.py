import pandas as pd


def loadDataset():
    df = pd.read_csv("Datasets/airport_traffic_2025.csv", sep=",")
    return df


# Data representation
# Data cleaning
# Data visualization
# Data integration
# Data transformation

# Employ exploratory data analysis techniques.

# Generate graphs

# Load the dataset into Python
df = loadDataset()
print(df)
