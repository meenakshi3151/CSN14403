# Group a dataset by a categorical column and calculate the sum, mean, and count for each group.
import pandas as pd
data={
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'A'],
        'Value': [10, 15, 20, 25, 30, 35, 40, 45]
}

df=pd.DataFrame(data)
grouped_df=df.groupby('Category').agg({'Value':['sum','count','mean']})

print(grouped_df)