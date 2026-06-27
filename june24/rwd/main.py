import pandas as pd

# 1a. Read the CSV
df = pd.read_csv('rwd/my_csv/RewardsData.csv')

# Convert 'Zip' to numeric to safely calculate the average
df['Zip'] = pd.to_numeric(df['Zip'], errors='coerce')
zip_avg = df['Zip'].mean()

# 1b. Fill the exact empty cell. 
# (Excel row 1372 = Python index 1370)
df.iloc[1370, df.columns.get_loc('Zip')] = zip_avg

# Optional: Convert the column back to integer to remove the '.0' from the other rows.
# (Note: This will round your average to the nearest whole number. If your professor 
# wants the exact decimal, comment out this line).
df['Zip'] = df['Zip'].round().astype('Int64')

# 2. Remove all rows with empty 'Zip' cells and save
df.dropna(subset=['Zip']).to_csv('rwd/my_csv/cleaned_data.csv', index=False)

print("Assignment completed successfully!")