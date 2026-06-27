### **Setup & Reading the Data**
```python
import pandas as pd
import numpy as np

df = pd.read_csv('rwdcity/my_csv/RewardsData.csv', dtype={'Zip': str})
```
* **What it does:** Imports the necessary libraries and reads the CSV file into a DataFrame named `df`. 
* **Why it's important:** We use `dtype={'Zip': str}` to force Pandas to read the Zip column as text. If we don't do this, Pandas might read Zip codes as numbers, which would destroy formats like `27707-1634` (turning it into a float) or truncate leading zeros.

---

### **Step 1: Remove the 'Tags' column**
```python
df = df.drop(columns=['Tags'])
```
* **What it does:** Deletes the 'Tags' column entirely from the DataFrame.
* **Why it's important:** Fulfills the first instruction to clean up unnecessary data.

---

### **Step 2: Standardize "Winston-Salem"**
```python
df['City'] = df['City'].str.replace(r'(?i)winston[\s-]*salem', 'Winston-Salem', regex=True)
```
* **What it does:** Searches the 'City' column for any variation of Winston-Salem (e.g., "Winston salem", "winston-salem", "Winston  Salem") and replaces it with the exact string `"Winston-Salem"`.
* **Why it's important:** The regex `(?i)` makes it case-insensitive, and `[\s-]*` catches any spaces or hyphens between the words. This ensures all variations are unified.

---

### **Step 3: Proper Case & Remove Single-Letter Cities**
```python
df['City'] = df['City'].str.strip().str.title()
df['City'] = df['City'].replace({'District Of Columbia': 'District of Columbia'})

df = df[~df['City'].astype(str).str.match(r'^[a-zA-Z]$')]
```
* **What it does:** 
  1. `.strip()` removes accidental leading/trailing spaces. `.title()` capitalizes the first letter of every word (e.g., "sandy springs" becomes "Sandy Springs").
  2. Because `.title()` incorrectly capitalizes small words like "of", the `.replace()` line fixes "District Of Columbia" back to "District of Columbia".
  3. The final line uses a regex `^[a-zA-Z]$` to find cities that are exactly one letter long (like the city "G" in your raw data) and drops those specific rows.

---

### **Step 4: Fill Empty 'City' Cells**
```python
cities_list = ['Minneapolis', 'Los Angelis', 'Merida', 'Winston-Salem', 'Thomasville', 
               'Goldsboro', 'Raleigh', 'Bethesda', 'Midlothian', 'Jacksonville']
nan_city_mask = df['City'].isna()
nan_city_count = nan_city_mask.sum()
if nan_city_count > 0:
    df.loc[nan_city_mask, 'City'] = [cities_list[i % len(cities_list)] for i in range(nan_city_count)]
```
* **What it does:** 
  1. Creates the list of cities provided in your prompt.
  2. `isna()` finds all empty (NaN) cells in the 'City' column.
  3. The list comprehension uses the modulo operator (`i % len(cities_list)`) to cycle through the `cities_list`. If there are 15 empty cells, it will assign the 10 cities, and then loop back to the start for the remaining 5.

---

### **Step 5: Sort Alphabetically by 'City'**
```python
df = df.sort_values(by='City').reset_index(drop=True)
```
* **What it does:** Sorts the entire DataFrame alphabetically based on the 'City' column. `reset_index(drop=True)` cleans up the row numbers so they go from 0 to N sequentially.

---

### **Step 6: Replace State Abbreviations with Full Names**
```python
state_dict = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    # ... [all 50 states + DC/PR] ...
    'NC': 'North Carolina', 'NY': 'New York', 'TX': 'Texas', 'VA': 'Virginia', 'WA': 'Washington'
}
df['State'] = df['State'].apply(lambda x: state_dict.get(x, x) if pd.notna(x) else x)
```
* **What it does:** Creates a dictionary mapping every 2-letter abbreviation to its full name. The `apply()` function checks every cell: if it's an abbreviation, it swaps it for the full name. If it's already a full name (or empty), it leaves it alone.

---

### **Step 7: Fill Empty 'State' Cells**
```python
states_list = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 
    # ... [all 50 states in alphabetical order] ...
    'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]
nan_state_mask = df['State'].isna()
nan_state_count = nan_state_mask.sum()
if nan_state_count > 0:
    df.loc[nan_state_mask, 'State'] = [states_list[i % len(states_list)] for i in range(nan_state_count)]
```
* **What it does:** Exactly like Step 4, but for States. It finds empty 'State' cells and fills them by cycling through the 50 states in alphabetical order (1st empty gets Alabama, 2nd gets Alaska... 51st gets Alabama again).

---

### **Step 8: Sort Alphabetically by 'State'**
```python
df = df.sort_values(by='State').reset_index(drop=True)
```
* **What it does:** Re-sorts the DataFrame, this time alphabetically by the 'State' column, and resets the index again.

---

### **Step 9: Truncate Zip Codes Longer than 5 Digits**
```python
df['Zip'] = df['Zip'].apply(lambda x: x[:5] if pd.notna(x) and len(str(x)) > 5 else x)
```
* **What it does:** Looks at every Zip code. If it is not empty and is longer than 5 characters (like `27707-1634` or `55401.0`), it slices the string to keep only the first 5 characters (`x[:5]`).

---

### **Step 10: Drop Rows with Zip Codes Less than 5 Digits**
```python
df = df[df['Zip'].astype(str).str.len() >= 5]
```
* **What it does:** Converts the Zip column to strings, counts the length, and uses boolean indexing to keep *only* the rows where the length is 5 or greater. This drops invalid zips like `969`.

---

### **Step 11: Remove Empty 'Last Seen' Rows**
```python
df = df.dropna(subset=['Last Seen'])
```
* **What it does:** Drops any row where the 'Last Seen' column is empty (NaN).

---

### **Step 12: Fill Empty 'Birthdate' with 'Last Seen'**
```python
df['Birthdate'] = df['Birthdate'].fillna(df['Last Seen'])
```
* **What it does:** Finds all empty cells in the 'Birthdate' column and replaces them with the value from the exact same row's 'Last Seen' column.

---

### **Step 13: Save the Cleaned CSV**
```python
df.to_csv('rwdcity/my_csv/RewardsData_cleaned.csv', index=False)

print("Assignment 2 completed successfully!")
```
* **What it does:** Exports the final, cleaned DataFrame to a new CSV file named `RewardsData_cleaned.csv` in your `my_csv` folder. `index=False` ensures Pandas doesn't write the row numbers as an extra, unnamed column. Finally, it prints a success message to your console.