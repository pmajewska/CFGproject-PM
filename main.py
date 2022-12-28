import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales2.csv')
df_sales = df[['year', 'month', 'expenditure1', 'expenditure2', 'expenditure3', 'sales_product1', 'sales_product2', 'sales_product3']].copy()
df_sales

for index, row in df_sales.iterrows():
    df_sales['sales'] = (df_sales['sales_product1'] + df_sales['sales_product2'] + df_sales['sales_product3'])
  
for index, row in df_sales.iterrows():
    df_sales['expenditure'] =  (df_sales['expenditure1'] + df_sales['expenditure2'] + df_sales['expenditure3'])
  
for index, row in df_sales.iterrows():
    if row['sales'] > row['expenditure']:
        df_sales.loc[index,'P&L'] = 'profit'
        print (row['month'], df_sales.loc[index,'P&L'])
  
for index, row in df_sales.iterrows():
    if row['sales'] < row['expenditure']:
        df_sales.loc[index,'P&L'] = 'loss'
        print (row['month'], df_sales.loc[index,'P&L'])
  
print(df_sales[df_sales['sales'] == df_sales['sales'].max()])
print(df_sales[df_sales['sales'] == df_sales['sales'].min()])
print('Total sales:', df_sales['sales'].sum())
print('Mean sales value:', df_sales['sales'].mean())

for index, row in df_sales.iterrows():
    df_sales['percentage'] =  (df_sales['sales'] / df_sales['sales'].sum()) * 100
    print(row['month'], df_sales.loc[index,'percentage'])
  
# Figure sales as a bar
df_sales.groupby('month')['sales'].sum().plot(kind='bar')
plt.show()

# Figure percentage as a bar
df_sales.groupby('month')['percentage'].sum().plot(kind='bar')
plt.show()

# # Figure as a pie:
# df_sales.groupby('month')['sales'].sum().plot(kind='pie')
# plt.show()

# Figure percentage as a pie
df_sales.groupby('month')['percentage'].sum().plot(kind='pie')
plt.show()


# This is a code for 'profit' and 'loss' without grouping:
  
# for index, row in df_sales.iterrows():
#     if row['sales'] > row['expenditure']:
#         df_sales.loc[index,'P&L'] = 'profit'
#         print (row['month'], df_sales.loc[index,'P&L'])
#     else:
#         df_sales.loc[index, 'P&L'] = 'loss'
#         print(row['month'], df_sales.loc[index, 'P&L'])
