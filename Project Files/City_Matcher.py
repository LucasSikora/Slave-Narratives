import pandas as pd
import re

# Read the CSV files into pandas dataframes
interview_df = pd.read_csv('C:\\Users\Lucas\PycharmProjects\pythonProject6\Alabama_Raw.csv')
cities_df = pd.read_csv('C:\\Users\Lucas\PycharmProjects\pythonProject6\\uscities.csv')

# Create new columns in the interview dataframe to store matching cities and counties
interview_df['Matching_Cities'] = ''
interview_df['Matching_Counties'] = ''

# Dictionary of state abbreviations including Puerto Rico and Washington, D.C.
state_abbreviations = {
    'Alabama': 'Ala|Al',
    'Arizona': 'Ariz|Az',
    'Arkansas': 'Ark|Ar',
    'California': 'Calif|Ca',
    'Florida': 'Fla|Fl',
    'Georgia': 'Ga|Ga.',
    'Hawaii': 'Hawaii|Hi',
    'Idaho': 'Idaho|Id',
    'Illinois': 'Ill|Il',
    'Iowa': 'Iowa|Ia',
    'Kansas': 'Kans|Ks',
    'Kentucky': 'Ky|Ky.',
    'Louisiana': 'La|La.',
    'Maryland': 'Md',
    'Mississippi': 'Miss.|Ms',
    'Missouri': 'Mo',
    'Nevada': 'Nev.|Nv',
    'New Jersey': 'N.J.|Nj',
    'New York': 'N.Y.|Ny',
    'North Carolina': 'N.C.|Nc',
    'North Dakota': 'N.D.|Nd',
    'Ohio': 'Ohio|Oh',
    'Oklahoma': 'Okla.|Ok',
    'Oregon': 'Ore.|Or',
    'Pennsylvania': 'Pa|Pa.',
    'Rhode Island': 'R.I.|Ri',
    'South Carolina': 'S.C.|Sc',
    'South Dakota': 'S.D.|Sd',
    'Tennessee': 'Tenn.|Tn',
    'Texas': 'Tex.|Tx',
    'Vermont': 'Vermont|Vt',
    'Virginia': 'Va|Va.',
    'West Virginia': 'W.Va.|Wv',
    'Puerto Rico': 'P.R.|PR',
    'District of Columbia': 'D.C.|DC'
}

# Iterate through all rows of the interview dataframe
for i, interview_row in interview_df.iterrows():
    matching_cities_list = []
    matching_counties_list = []

    # Extract cities from 'Interview Content', 'Blockquote Text', and 'Photograph_Location' columns
    combined_text = f"{interview_row['Interview Content']} {interview_row['Blockquote Text']} {interview_row['Photograph_Location']}"
    all_cities = set(
        re.findall(r'\b(?:' + '|'.join(cities_df['city'].map(re.escape)) + r')\b', combined_text, flags=re.IGNORECASE))

    for city in all_cities:
        city_rows = cities_df[cities_df['city'].str.lower() == city.lower()]

        for _, city_row in city_rows.iterrows():
            # Check if the state is in the abbreviations dictionary
            if city_row['state_name'] in state_abbreviations:
                # Create a state pattern with both full name and abbreviation
                state_abbreviation_pattern = '|'.join(state_abbreviations[city_row['state_name']].split('|'))
                city_state_pattern = rf'{re.escape(city_row["city"])},?\s*({state_abbreviation_pattern})'

                if re.search(city_state_pattern, combined_text, flags=re.IGNORECASE):
                    matching_cities_list.append(f"{city_row['city']}, {city_row['state_name']}")
                    matching_counties_list.append(city_row['county_name'])

    # Join the matching cities and counties into strings
    matching_cities_str = ', '.join(matching_cities_list)
    matching_counties_str = ', '.join(matching_counties_list)

    # Assign the matching cities and counties to the dataframe columns
    interview_df.at[i, 'Matching_Cities'] = matching_cities_str
    interview_df.at[i, 'Matching_Counties'] = matching_counties_str
# Save the updated dataframe to a new CSV file
interview_df.to_csv('Alabama_Matched.csv', index=False)
