import pandas as pd

# Assuming you have two Excel files: 'updated_names.xlsx' and 'Alabama_test_joiner.xlsx'
# Load the Excel files
file_path_updated_names = 'C:\\Users\Lucas\PycharmProjects\pythonProject6\CSVs\\updated_names.csv'  # Replace with your file path
file_path_test_joiner = 'C:\\Users\Lucas\PycharmProjects\pythonProject6\CSVs\Alabama_test_joiner 1.csv'  # Replace with your file path

updated_names_df = pd.read_csv(file_path_updated_names)
test_joiner_df = pd.read_csv(file_path_test_joiner)

# Ensuring 'narrator' column exists in both dataframes and is consistently named
if 'narrator' not in updated_names_df.columns:
    updated_names_df = updated_names_df.rename(columns={updated_names_df.columns[0]: 'narrator'})

if 'narrator' not in test_joiner_df.columns:
    test_joiner_df = test_joiner_df.rename(columns={test_joiner_df.columns[0]: 'narrator'})

# Renaming columns in test_joiner_df to avoid name conflicts after joining
# Exclude the 'narrator' column from renaming
test_joiner_df = test_joiner_df.rename(columns={col: f"test_{col}" for col in test_joiner_df.columns if col != 'narrator'})

# Merging the dataframes on 'narrator'
merged_df = pd.merge(updated_names_df, test_joiner_df, on='narrator', how='left')

# Group by 'narrator' and aggregate the data
# We use lambda x: ', '.join(x.dropna().astype(str)) to combine non-null values into a single string
# Adjust this part as needed based on the nature of your data
aggregated_df = merged_df.groupby('narrator').agg(lambda x: ', '.join(x.dropna().astype(str))).reset_index()

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_output.csv', index=False)
