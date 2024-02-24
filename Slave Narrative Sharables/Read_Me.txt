This folder contains the files that are generated based on information in the narratives and the Howard Potts index "A Comprehensive Name Index for the American Slave"

This folder only contains the information from Alabama as that is the first state in the narratives and the one that the program was tested on. The program is robust enough to work with each state, but only Alabama was done so far as it will take approximately 40 hours of wall clock time to fully run every bit of data through the program.

----------------------------------------------------------------------------------------------------------------------------------

***Alabama_Raw.csv contains the raw data pulled from the narratives themselves separated into columns that each contain a piece of the interview



ID - The column containing the ID of the individual interviewed

Pfirst - the first paragraph in the interview. Rows are only filled if the Pfirst is a title of an interview

Interview Content - the full narrative

Blockquote - Contains the blockquote element from the html. This typically is the description of the interview given by the writer.

Photographs - contains the file location for the photograph to be used with the website if applicable

photograph_location - contains the caption for the photograph, typically in the format "ID, Location of interview"

----------------------------------------------------------------------------------------------------------------------------------

***Merged_output.csv contains the merged information of both the narrative information along with the information found in the Potts index. This can be considered to be the primary document containing information about each narrator. The first 6 columns are the same as in Alabama_Raw.csv



Matching_Cities - contains a list of cities within the narrative. This is checked against US census data to validate that it is an actual city. 

Matching_Counties - contains a list of matching counties that correspond with the matching cities. They are matched in order.

*** the following information comes from the Potts index and is checked against the narratives themselves for validation

Birth_Year contains the birth year of the narrator if available. 

Age -  Age of narrator if applicable

Master - Contains a single master of the narrator. Because of this, there are multiple rows for each narrator in order to map out each location individually

Interviewer - contains the interviewer of the narrator if available

County - contains the county that the narrator was enslaved under the corresponding master of the same row. 

State - contains the state that the County column is in.


----------------------------------------------------------------------------------------------------------------------------------
***merged_gdf.csv is a GeoPandas GeoDataFrame (this is nerd speak for it allows me to make a map). It contains all of the aforementioned columns in merged_output.csv along with merged GeoJSON data containing the geometries of each county. 

geometry - only column of relevance in this csv. This contains the geometries of each county in terms of their coordinates so that they can be mapped onto a leaflet.js map in the correct locations.

----------------------------------------------------------------------------------------------------------------------------------

Rough_Map.html contains a very rough map of the narrators in the merged_gdf.csv DataFrame. This map currently has many issues and simply serves as a proof of concept for mapping the geometries of the counties

issues:

1) narrators are currently overlaid in such a way that only one narrator in each county is clickable
2) currently contains some erroneous data due to the check including every state.
3) Text currently displays fully rather in a scrollable box. This means you have to zoom out to view the full narrative






