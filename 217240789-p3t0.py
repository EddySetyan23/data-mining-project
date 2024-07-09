import pandas as pd
import os


# Read the CSV file
data = pd.read_csv('C:\\Data Mining Project\\Data Mining Task 3\\217240789-t0.csv')
     
# Combine the data of 12 companies into one CSV file by adding a new dimension “Company”
# Only keep the dimensions: Date, Open, Close, Volume, Company; drop the other dimensions
data = data[['Date', 'Open', 'Close', 'Volume', 'Company']]

# Sort the data on date
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by='Date')

# Add 12 new dimensions to the data, 1 for each company
companies = data['Company'].unique()
for company in companies:
    data[company] = 0

# Merge the rows of each day
for date in data['Date'].unique():
    daily_data = data[data['Date'] == date]
    for index, row in daily_data.iterrows():
        if row['Close'] - row['Open'] > 0:
            data.at[index, row['Company']] = row['Volume']
        else:
            data.at[index, row['Company']] = 0

# Drop the Open, Close, Volume, and Company dimensions
data = data.drop(columns=['Open', 'Close', 'Volume', 'Company'])

# Group by date and sum the values
data = data.groupby('Date').sum().reset_index()

# Save the final data to a CSV file in the specified directory
output_directory = 'C:\\Data Mining Project\\Data Mining Task 3'
output_filename = '217240789.csv'
output_path = os.path.join(output_directory, output_filename)
data.to_csv(output_path, index=False)