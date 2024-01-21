# Merge two DataFrames based on a common column, handling potential duplicates and missing values appropriately.
import pandas as pd
d1={
    'column':[1,2,3,4],
    'data1':['A','B','C','D']
}

d2={
 'column':[5,2,7,8],
    'data2':['E','B','G','H']
}

df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
merged_df=pd.merge(df1,df2,on='column',how='outer')
print(merged_df)
