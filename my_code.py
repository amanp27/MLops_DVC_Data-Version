import pandas as pd
import os

data = {'Name': ['Aman', 'Harsh', 'Chinmay'],
      'Age': [25, 20, 28],
      'City': ['Hyderabad', 'Nagpur', 'Delhi']}

df = pd.DataFrame(data)

new_row = {'Name': 'Kavya', 'Age': 23, 'City': "Pune"}
df.loc[(len(df.index))] = new_row

new_row2 = {'Name': 'Akanksha', 'Age': 22, 'City': 'Nashik'}
df.loc[len(df.index)] = new_row2

# For Directory as ->'data'.
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# To save the file inside directory as ->'sample_data_csv'.
file_path = os.path.join(data_dir, 'sample_data_csv')
df.to_csv(file_path, index = False)

print(f"CSV file saved to {file_path}")