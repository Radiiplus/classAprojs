import pandas as pd
import numpy as np

# 1. Read the CSV (Reading 'Zip' as string to preserve formats like '27707-1634' or '55401.0')
df = pd.read_csv('rwdcity/my_csv/RewardsData.csv', dtype={'Zip': str})

# 2. Remove the 'Tags' column
df = df.drop(columns=['Tags'])

# 3. Replace all formats of Winston-salem with "Winston-Salem" (case-insensitive)
df['City'] = df['City'].str.replace(r'(?i)winston[\s-]*salem', 'Winston-Salem', regex=True)

# 4. Proper case for cities & remove single-letter cities
df['City'] = df['City'].str.strip().str.title()
# Fix specific edge cases that .title() alters
df['City'] = df['City'].replace({'District Of Columbia': 'District of Columbia'})

# Remove rows where 'City' consists of exactly one alphabet letter (e.g., 'G')
df = df[~df['City'].astype(str).str.match(r'^[a-zA-Z]$')]

# Fill empty 'City' cells with the cycling list
cities_list = ['Minneapolis', 'Los Angelis', 'Merida', 'Winston-Salem', 'Thomasville', 
               'Goldsboro', 'Raleigh', 'Bethesda', 'Midlothian', 'Jacksonville']
nan_city_mask = df['City'].isna()
nan_city_count = nan_city_mask.sum()
if nan_city_count > 0:
    df.loc[nan_city_mask, 'City'] = [cities_list[i % len(cities_list)] for i in range(nan_city_count)]

# 5. Arrange in alphabetical order by 'City'
df = df.sort_values(by='City').reset_index(drop=True)

# 6. Replace state abbreviations with full names
state_dict = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
    'DC': 'District of Columbia', 'PR': 'Puerto Rico'
}
df['State'] = df['State'].apply(lambda x: state_dict.get(x, x) if pd.notna(x) else x)

# 7. Fill empty 'State' cells with alphabetical state names (cycling through the 50 states)
states_list = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 
    'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 
    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 
    'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 
    'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 
    'Wisconsin', 'Wyoming'
]
nan_state_mask = df['State'].isna()
nan_state_count = nan_state_mask.sum()
if nan_state_count > 0:
    df.loc[nan_state_mask, 'State'] = [states_list[i % len(states_list)] for i in range(nan_state_count)]

# 8. Repeat step 5 for the 'State' column (Sort alphabetically)
df = df.sort_values(by='State').reset_index(drop=True)

# 9. Truncate Zip codes longer than 5 digits to the first five digits
df['Zip'] = df['Zip'].apply(lambda x: x[:5] if pd.notna(x) and len(str(x)) > 5 else x)

# 10. Drop rows where Zip code is less than 5 digits
df = df[df['Zip'].astype(str).str.len() >= 5]

# 11. Remove rows where 'Last Seen' is empty
df = df.dropna(subset=['Last Seen'])

# 12. Replace empty cells in 'Birthdate' with the date from 'Last Seen'
df['Birthdate'] = df['Birthdate'].fillna(df['Last Seen'])

# 13. Save the cleaned data frame as a CSV file
df.to_csv('rwdcity/my_csv/RewardsData_cleaned.csv', index=False)

print("Assignment 2 completed successfully!")