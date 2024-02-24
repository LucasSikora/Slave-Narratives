import pandas as pd
import geopandas as gpd
import folium
import json
from shapely.geometry import shape
from shapely import wkt

merged_gdf = pd.read_csv('C:\\Users\Lucas\PycharmProjects\Slave Narratives\CSVs\merged_gdf.csv')



# Initialize a Folium Map
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)


def create_popup(row):
    narrators = row['narrator']  # Replace with the actual column name for narrators
    content = row['Interview Content']  # Replace with the actual column name for interview content
    return f"Narrators: {narrators}<br>Content: {content}"


for _, row in merged_gdf.iterrows():
    # Convert the string representation of geometry back to a geometry object
    geom = wkt.loads(row['geometry']) if isinstance(row['geometry'], str) else row['geometry']

    # Convert the geometry to a format that Folium can interpret
    geom_json = json.loads(json.dumps(shape(geom).__geo_interface__))

    popup = folium.Popup(create_popup(row), max_width=300)
    folium.GeoJson(geom_json, popup=popup).add_to(m)

    output_html_path = 'path_to_save_map.html'  # Replace with your file path
    m.save(output_html_path)