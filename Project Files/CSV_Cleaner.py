import pandas as pd
import os
csv_path = "C:\\Users\\Lucas\\PycharmProjects\\pythonProject6\\CSVs\\output_table.csv"

df = pd.read_csv(csv_path)

# Function to add space after punctuation if the next character is a letter
# Function to format the ID column
def format_id(id_text):
    # Replace hyphens with spaces and capitalize the first letter of each word
    formatted_id = id_text.replace("-", " ").title()
    return formatted_id

# Apply the function to the "ID" column
df['Formatted ID'] = df['ID'].apply(format_id)

# Function to add space after punctuation if the next character is a letter
def fix_punctuation(text):
    fixed_text = ""
    for i in range(len(text)):
        if i < len(text) - 1 and text[i].isalpha() and text[i + 1] in ",.?!":
            fixed_text += text[i] + " "
        else:
            fixed_text += text[i]
    return fixed_text

# Apply the function to the "Remaining Text" column
df['Fixed Remaining Text'] = df['Remaining Text'].apply(fix_punctuation)

# Remove the "Remaining Text" and "ID" columns
df = df[['Formatted ID', 'Pfirst', 'Fixed Remaining Text']]

# Specify the path for the new CSV file
new_csv_path = 'C:\\Users\\Lucas\\PycharmProjects\\pythonProject6\\CSVs/Alabama_fixed.csv'

# Save the DataFrame with the fixed text to a new CSV file
df.to_csv(new_csv_path, index=False)

print(f'New CSV file saved to {new_csv_path}')