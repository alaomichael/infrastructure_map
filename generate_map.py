import folium
import pandas as pd
from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get latitude and longitude
def get_lat_long(location):
    try:
        loc = geolocator.geocode(location)
        return loc.latitude, loc.longitude
    except:
        return None, None

# Read data from the Excel file
data = pd.read_excel('school_dilapidation_data.xlsx')

# Ensure the column names match those in your Excel file
latitude_col = 'Latitude'  # Update this if your column name is different
longitude_col = 'Longitude'  # Update this if your column name is different

# Create a base map
# m = folium.Map(location=[9.0820, 8.6753], zoom_start=6)

# Create a base map centered on the South-West region of Nigeria
m = folium.Map(location=[7.3775, 3.9470], zoom_start=7)

# Add infrastructure data to the map with additional details in the popup
for idx, row in data.iterrows():
    # Check if latitude and longitude are missing
    if pd.isna(row[latitude_col]) or pd.isna(row[longitude_col]):
        lat, long = get_lat_long(row['Local Govt Area'])
        if lat and long:
            data.at[idx, latitude_col] = lat
            data.at[idx, longitude_col] = long
        else:
            continue  # Skip if geocoding fails

    popup_info = (
        f"Name of School: {row['Name of the school']}<br>"
        f"State: {row['State']}<br>"
        f"Local Govt Area: {row['Local Govt Area']}<br>"
        f"Ward: {row['Ward']}<br>"
        f"Level of Dilapidation: {row['Level of Dilapidation']}<br>"
        f"Email: {row['Email of respondent']}"
    )
    
    folium.Marker(
        location=[row[latitude_col], row[longitude_col]],
        popup=popup_info,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save the map
m.save('static/infrastructure_map.html')
