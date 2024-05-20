# BigMart Sales Data Processing

This project includes a Python script that processes BigMart sales data, creates a pivot table, and exports the results to an Excel file.

## Features

- Loads sales data from a CSV file into a pandas DataFrame.
- Cleans the data (placeholder for various data cleaning steps).
- Creates a pivot table summarizing sales by item and outlet.
- Writes the pivot table to an Excel file using the XlsxWriter engine.

## Requirements

- Python 3.x
- pandas
- openpyxl
- XlsxWriter

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Mohanraj2622/bigmart-sales-data-processing.git
    cd bigmart-sales-data-processing
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install pandas openpyxl XlsxWriter
    ```

## Usage

1. **Prepare the dataset**: Ensure you have a CSV file named `bigmart_sales.csv` with appropriate sales data.

2. **Run the Python script**:
    ```bash
    python process_sales_data.py
    ```

## Files

- `process_sales_data.py`: The main Python script for processing the sales data.
- `bigmart_sales.csv`: The CSV file containing BigMart sales data.
- `bigmart_sales.xlsx`: The Excel file where the pivot table is saved.

## Python Script Details (`process_sales_data.py`)

```python
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
```

### Data Cleaning

Placeholder section in the script for data cleaning steps. Here are some common steps you might consider:

- Replacing missing values:
    ```python
    df.fillna(method='ffill', inplace=True)
    ```

- Encoding categorical variables:
    ```python
    df = pd.get_dummies(df, columns=['CategoryColumn'])
    ```

### Pivot Table

The pivot table summarizes sales data:
- `values='Item_Outlet_Sales'`: The values to aggregate.
- `index='Item_Identifier'`: The rows of the pivot table.
- `columns='Outlet_Identifier'`: The columns of the pivot table.
- `aggfunc='sum'`: Aggregation function to sum the sales.

### Writing to Excel

- Uses `pd.ExcelWriter` with the `xlsxwriter` engine to write the pivot table to an Excel file.
- Saves the Excel file as `bigmart_sales.xlsx` with a sheet named 'Sales'.

## Notes

- Ensure the CSV file (`bigmart_sales.csv`) is correctly formatted and located in the same directory as the Python script.
- Customize the data cleaning steps as per your data requirements.

## Acknowledgments

- Inspired by data processing and analysis techniques in Python using pandas and XlsxWriter.
