"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/20/2024
PURPOSE:merging dataFrames in Pandas
"""

import pandas as pd

# Create DataFrames with matching values for merging
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

df2 = pd.DataFrame({
    'X': [13, 14, 15, 16],
    'Y': [5, 7, 6, 8],  # Notice that these values will match with column 'B' in df1
    'Z': [17, 18, 19, 20]
})

# Display the original DataFrames
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Merge DataFrames on specified columns
df3 = pd.merge(df1, df2, right_on='Y', left_on='B')

# Display the merged DataFrame
print("\nMerged DataFrame:")
print(df3)
