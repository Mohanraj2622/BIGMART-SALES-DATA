pip install pandas openpyxl XlsxWriter
import pandas as pd

# Load data into a pandas DataFrame
df = pd.read_csv('bigmart_sales.csv')

# Perform data cleaning here, such as replacing missing values, encoding categorical variables, etc.
# Create a pivot table
pivot_table = df.pivot_table(values='Item_Outlet_Sales', index='Item_Identifier', columns='Outlet_Identifier', aggfunc='sum')

# Rename columns and index
pivot_table.columns = pivot_table.columns.get_level_values(1)
pivot_table.index = pivot_table.index.get_level_values(0)
# Write pivot table to Excel
writer = pd.ExcelWriter('bigmart_sales.xlsx', engine='xlsxwriter')
pivot_table.to_excel(writer, sheet_name='Sales')

# Save the file
writer.save()
