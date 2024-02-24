# Define a function to flip names
import pandas as pd
df = pd.read_csv('C:\\Users\Lucas\PycharmProjects\pythonProject6\CSVs\Alabama_Matched.csv')


# Define a function to flip names
def flip_name(name):
    parts = name.split(' ')
    if len(parts) == 2:
        first, last = parts
        return f'{last}, {first}'
    else:
        return name  # Return the original name if it cannot be split properly


# Apply the function to the 'Name' column
df['ID'] = df['ID'].apply(flip_name)

df.to_csv('updated_names.csv', index=False)