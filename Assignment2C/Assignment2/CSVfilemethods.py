# 11. Load a CSV file containing missing values and perform appropriate imputation methods (e.g., fill with mean, median, or mode).
import pandas as pd

csv_file_path = 'final_data.csv'  
df = pd.read_csv(csv_file_path)

print("Original DataFrame:")


imputation_method = input("Enter the imputation method")

if imputation_method == 'mean':
    df = df.fillna(df.mean())
elif imputation_method == 'median':
    df = df.fillna(df.median())
elif imputation_method == 'mode':
    df = df.fillna(df.mode().iloc[0])  
print(f"\nDataFrame after {imputation_method} imputation:")
print(df)
