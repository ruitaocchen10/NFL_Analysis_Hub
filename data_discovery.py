import nfl_data_py as nfl
import pandas as pd

injury_data = nfl.import_injuries([2023])

# Size and shape
print(f"Dataset size: {injury_data.shape}")  # (rows, columns)
print(f"Number of injuries: {len(injury_data)}")

# Column names and types
print(f"Columns: {injury_data.columns.tolist()}")
print(f"Data types:\n{injury_data.dtypes}")

# See actual data samples
print(injury_data.head())        # First 5 rows
print(injury_data.head(10))      # First 10 rows

# Quick statistical overview
print(injury_data.describe())    # For numerical columns
print(injury_data.info())        # Overall summary

# Count missing values
print(injury_data.isnull().sum())

# Percentage missing for each column
missing_pct = (injury_data.isnull().sum() / len(injury_data)) * 100
print(missing_pct)

# For any column with limited unique values
print(injury_data['practice_status'].value_counts())

# Check unique values in each column
for col in injury_data.columns:
    print(f"{col}: {injury_data[col].nunique()} unique values")