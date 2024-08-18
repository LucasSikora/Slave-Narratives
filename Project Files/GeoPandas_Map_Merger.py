import pandas as pd
import geopandas as gpd

# Paths to your files
output_csv_path = 'C:\\Users\\Lucas\\PycharmProjects\\pythonProject6\\CSVs\\merged_output_gdf.csv'

json_file_path = 'C:\\Users\\Lucas\\PycharmProjects\\pythonProject6\\CSVs\\counties.json'
csv_file_path = 'C:\\Users\\Lucas\\PycharmProjects\\pythonProject6\\CSVs\\merged_output.csv'

# Load the GeoJSON file
gdf = gpd.read_file(json_file_path)

# Load your CSV file
df = pd.read_csv(csv_file_path)

# State abbreviations in alphabetical order
state_abbreviations = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

# Mapping state numbers to abbreviations
state_map = {str(i).zfill(2): abbr for i, abbr in enumerate(state_abbreviations, start=1)}

# Map state numbers to abbreviations in GeoDataFrame
gdf['State_Abbreviation'] = gdf['STATE'].map(state_map)

# Merge the DataFrame with the GeoDataFrame
merged_gdf = gdf.merge(df, left_on=['State_Abbreviation', 'NAME'], right_on=['State', 'Matching_Counties'])

merged_gdf.to_csv(output_csv_path, index = False)

# Now 'merged_gdf' is a GeoDataFrame with CSV data and the county geometries
