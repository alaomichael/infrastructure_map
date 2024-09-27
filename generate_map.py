# import folium
# import pandas as pd
# from geopy.geocoders import Nominatim

# # Initialize geolocator
# geolocator = Nominatim(user_agent="geoapiExercises")

# # Function to get latitude and longitude
# def get_lat_long(location):
#     try:
#         loc = geolocator.geocode(location)
#         return loc.latitude, loc.longitude
#     except:
#         return None, None

# # Function to truncate text with ellipsis
# def truncate_text(text, max_length):
#     if len(text) > max_length:
#         return text[:max_length-3] + '...'
#     return text

# # Function to properly capitalize school names
# def proper_case(text):
#     exceptions = ["Ud", "Deen", "Of"]
#     words = text.split()
#     capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
#     return ' '.join(capitalized_words)

# # Read data from the Excel file
# data = pd.read_excel('school_dilapidation_data.xlsx')

# # Print column names to verify
# print("Column names in the DataFrame:", data.columns)

# # Ensure the column names match those in your Excel file
# latitude_col = 'LATITUDE'
# longitude_col = 'LONGITUDE'

# # Convert 'INFRASTRUCTURAL NEEDS' column to strings and handle NaN values
# data['INFRASTRUCTURAL NEEDS'] = data['INFRASTRUCTURAL NEEDS'].apply(lambda x: str(x) if not pd.isna(x) else '')

# # Apply proper_case function to the 'NAME OF SCHOOL' column
# data['NAME OF SCHOOL'] = data['NAME OF SCHOOL'].apply(proper_case)

# # Create a base map centered on the South-West region of Nigeria
# m = folium.Map(location=[7.3775, 3.9470], zoom_start=7)

# # Add infrastructure data to the map with additional details in the popup
# for idx, row in data.iterrows():
#     # Check if latitude and longitude are missing
#     if pd.isna(row[latitude_col]) or pd.isna(row[longitude_col]):
#         lat, long = get_lat_long(row['LGAs'])
#         if lat and long:
#             data.at[idx, latitude_col] = lat
#             data.at[idx, longitude_col] = long
#         else:
#             continue  # Skip if geocoding fails

#     # Truncate the "infrastructure Need" field if necessary
#     infrastructure_need = truncate_text(row['INFRASTRUCTURAL NEEDS'], 30)

#     # Convert infrastructure need to a list and create bullet points
#     if row['INFRASTRUCTURAL NEEDS']:
#         infrastructure_list = row['INFRASTRUCTURAL NEEDS'].split(',')
#         infrastructure_bullets = ''.join(f"<li>{item.strip()}</li>" for item in infrastructure_list)
#     else:
#         infrastructure_bullets = "<li>No infrastructure needs listed</li>"

#     # Prepare the popup content with an image
#     popup_info = (
#         f"<b>Name of School:</b> {row['NAME OF SCHOOL']}<br>"
#         f"<b>Category:</b> {row['CATEGORY']}<br>"
#         f"<b>State:</b> {row['STATE']}<br>"
#         f"<b>Local Govt Area:</b> {row['LGAs']}<br>"
#         f"<b>Ward:</b> {row['WARD']}<br>"
#         f"<b>Level of Dilapidation:</b> {row['LEVEL OF DILAPIDATION']}<br>"
#         f"<b>Infrastructure Need:</b><ul>{infrastructure_bullets}</ul><br>"
#         f"<img src='{row['IMAGE']}' width='100%' height='auto'>"
#     )
    
#     folium.Marker(
#         location=[row[latitude_col], row[longitude_col]],
#         popup=folium.Popup(popup_info, max_width=300),
#         icon=folium.Icon(color='blue', icon='info-sign')
#     ).add_to(m)

# # Save the map
# m.save('static/infrastructure_map.html')


# Just commented out

# import folium
# import pandas as pd
# from geopy.geocoders import Nominatim
# import json

# # Initialize geolocator
# geolocator = Nominatim(user_agent="geoapiExercises")

# # Function to get latitude and longitude
# def get_lat_long(location):
#     try:
#         loc = geolocator.geocode(location)
#         if loc:
#             return loc.latitude, loc.longitude
#         return None, None
#     except Exception as e:
#         print(f"Geocoding failed for {location}: {e}")
#         return None, None

# # Function to truncate text with ellipsis
# def truncate_text(text, max_length):
#     return (text[:max_length - 3] + '...') if len(text) > max_length else text

# # Function to properly capitalize school names
# def proper_case(text):
#     exceptions = ["Ud", "Deen", "Of"]
#     words = text.split()
#     return ' '.join([word.capitalize() if word.lower() not in exceptions else word for word in words])

# # Function to convert 'INFRASTRUCTURAL NEEDS' into a bullet list
# def create_infrastructure_bullets(infrastructure_needs):
#     if infrastructure_needs:
#         needs_list = infrastructure_needs.split(',')
#         return ''.join(f"<li>{need.strip()}</li>" for need in needs_list)
#     return "<li>No infrastructure needs listed</li>"

# # Function to generate the popup content for the map marker
# def generate_popup(row):
#     infrastructure_bullets = create_infrastructure_bullets(row['INFRASTRUCTURAL NEEDS'])
#     return (
#         f"<b>Name of School:</b> {row['NAME OF SCHOOL']}<br>"
#         f"<b>Category:</b> {row['CATEGORY']}<br>"
#         f"<b>State:</b> {row['STATE']}<br>"
#         f"<b>Local Govt Area:</b> {row['LGAs']}<br>"
#         f"<b>Ward:</b> {row['WARD']}<br>"
#         f"<b>Level of Dilapidation:</b> {row['LEVEL OF DILAPIDATION']}<br>"
#         f"<b>Infrastructure Need:</b><ul>{infrastructure_bullets}</ul><br>"
#         f"<img src='{row['IMAGE']}' width='100%' height='auto'>"
#     )

# # Read data from the Excel file
# data = pd.read_excel('school_dilapidation_data.xlsx')

# # Print column names to verify
# print("Column names in the DataFrame:", data.columns)

# # Ensure the column names match those in your Excel file
# latitude_col = 'LATITUDE'
# longitude_col = 'LONGITUDE'

# # Convert 'INFRASTRUCTURAL NEEDS' column to strings and handle NaN values
# data['INFRASTRUCTURAL NEEDS'] = data['INFRASTRUCTURAL NEEDS'].fillna('').astype(str)

# # Apply proper_case function to the 'NAME OF SCHOOL' column
# data['NAME OF SCHOOL'] = data['NAME OF SCHOOL'].apply(proper_case)

# # Create a base map centered on the South-West region of Nigeria
# m = folium.Map(location=[7.3775, 3.9470], zoom_start=7)

# # Loop through the data to add markers to the map
# for idx, row in data.iterrows():
#     # Check if latitude and longitude are missing and geocode if needed
#     if pd.isna(row[latitude_col]) or pd.isna(row[longitude_col]):
#         lat, long = get_lat_long(row['LGAs'])
#         if lat and long:
#             data.at[idx, latitude_col] = lat
#             data.at[idx, longitude_col] = long
#         else:
#             continue  # Skip if geocoding fails

#     # Truncate the "infrastructure Need" field for better display in the popup
#     infrastructure_need = truncate_text(row['INFRASTRUCTURAL NEEDS'], 30)

#     # Generate popup content
#     popup_info = generate_popup(row)

#     # Add a marker to the map
#     folium.Marker(
#         location=[row[latitude_col], row[longitude_col]],
#         popup=folium.Popup(popup_info, max_width=300),
#         icon=folium.Icon(color='blue', icon='info-sign')
#     ).add_to(m)

# # Save the map as an HTML file
# m.save('static/infrastructure_map.html')

# # Save the data to a JSON file for use in the HTML template
# data.to_json('static/school_data.json', orient='records')

# # Extract unique values for filters
# filters = {
#     'states': data['STATE'].dropna().unique().tolist(),
#     'CATEGORY': data['CATEGORY'].dropna().unique().tolist(),
#     'lgas': data['LGAs'].dropna().unique().tolist(),
#     'wards': data['WARD'].dropna().unique().tolist(),
#     'levels_of_dilapidation': data['LEVEL OF DILAPIDATION'].dropna().unique().tolist(),
#     'infrastructure_needs': data['INFRASTRUCTURAL NEEDS'].dropna().unique().tolist()
# }

# # Save the filters data to a JSON file
# with open('static/filters.json', 'w') as f:
#     json.dump(filters, f)




# import folium
# import pandas as pd
# from geopy.geocoders import Nominatim
# import json

# # Initialize geolocator
# geolocator = Nominatim(user_agent="geoapiExercises")

# # Function to get latitude and longitude
# def get_lat_long(location):
#     try:
#         loc = geolocator.geocode(location)
#         return loc.latitude, loc.longitude
#     except:
#         return None, None

# # Function to truncate text with ellipsis
# def truncate_text(text, max_length):
#     if len(text) > max_length:
#         return text[:max_length-3] + '...'
#     return text

# # Function to properly capitalize school names
# def proper_case(text):
#     exceptions = ["Ud", "Deen", "Of"]
#     words = text.split()
#     capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
#     return ' '.join(capitalized_words)

# # Read data from the Excel file
# data = pd.read_excel('school_dilapidation_data.xlsx')

# # Print column names to verify
# print("Column names in the DataFrame:", data.columns)

# # Ensure the column names match those in your Excel file
# latitude_col = 'LATITUDE'
# longitude_col = 'LONGITUDE'

# # Convert 'INFRASTRUCTURAL NEEDS' column to strings and handle NaN values
# data['INFRASTRUCTURAL NEEDS'] = data['INFRASTRUCTURAL NEEDS'].apply(lambda x: str(x) if not pd.isna(x) else '')

# # Apply proper_case function to the 'NAME OF SCHOOL' column
# data['NAME OF SCHOOL'] = data['NAME OF SCHOOL'].apply(proper_case)

# # Create a base map centered on the South-West region of Nigeria
# m = folium.Map(location=[7.3775, 3.9470], zoom_start=7)

# # Add infrastructure data to the map with additional details in the popup
# for idx, row in data.iterrows():
#     # Check if latitude and longitude are missing
#     if pd.isna(row[latitude_col]) or pd.isna(row[longitude_col]):
#         lat, long = get_lat_long(row['LGAs'])
#         if lat and long:
#             data.at[idx, latitude_col] = lat
#             data.at[idx, longitude_col] = long
#         else:
#             continue  # Skip if geocoding fails

#     # Truncate the "infrastructure Need" field if necessary
#     infrastructure_need = truncate_text(row['INFRASTRUCTURAL NEEDS'], 30)

#     # Convert infrastructure need to a list and create bullet points
#     if row['INFRASTRUCTURAL NEEDS']:
#         infrastructure_list = row['INFRASTRUCTURAL NEEDS'].split(',')
#         infrastructure_bullets = ''.join(f"<li>{item.strip()}</li>" for item in infrastructure_list)
#     else:
#         infrastructure_bullets = "<li>No infrastructure needs listed</li>"

#     # Prepare the popup content with an image
#     popup_info = (
#         f"<b>Name of School:</b> {row['NAME OF SCHOOL']}<br>"
#         f"<b>Category:</b> {row['CATEGORY']}<br>"
#         f"<b>State:</b> {row['STATE']}<br>"
#         f"<b>Local Govt Area:</b> {row['LGAs']}<br>"
#         f"<b>Ward:</b> {row['WARD']}<br>"
#         f"<b>Level of Dilapidation:</b> {row['LEVEL OF DILAPIDATION']}<br>"
#         f"<b>Infrastructure Need:</b><ul>{infrastructure_bullets}</ul><br>"
#         f"<img src='{row['IMAGE']}' width='100%' height='auto'>"
#     )
    
#     folium.Marker(
#         location=[row[latitude_col], row[longitude_col]],
#         popup=folium.Popup(popup_info, max_width=300),
#         icon=folium.Icon(color='blue', icon='info-sign')
#     ).add_to(m)

# # Save the map
# m.save('static/infrastructure_map.html')

# # Save the data to a JSON file for use in the HTML template
# data.to_json('static/school_data.json', orient='records')

# # Save unique values for filters
# filters = {
#     'states': data['STATE'].unique().tolist(),
#     'category': data['CATEGORY'].unique().tolist(),
#     'lgas': data['LGAs'].unique().tolist(),
#     'wards': data['WARD'].unique().tolist(),
#     'levels_of_dilapidation': data['LEVEL OF DILAPIDATION'].unique().tolist(),
#     'infrastructure_needs': data['INFRASTRUCTURAL NEEDS'].unique().tolist()
# }
# with open('static/filters.json', 'w') as f:
#     json.dump(filters, f)

import folium
import pandas as pd
from geopy.geocoders import Nominatim
import json
import time  # To add delay between geocoding requests
import logging

# Setup logging
logging.basicConfig(filename='geocoding_errors.log', level=logging.ERROR)

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get latitude and longitude from the school address
def get_lat_long_from_address(address):
    try:
        loc = geolocator.geocode(address)
        if loc:
            return loc.latitude, loc.longitude
        return None, None
    except Exception as e:
        logging.error(f"Geocoding failed for {address}: {e}")
        return None, None

# Function to truncate text with ellipsis
def truncate_text(text, max_length):
    return (text[:max_length - 3] + '...') if len(text) > max_length else text

# Function to properly capitalize school names
def proper_case(text):
    exceptions = ["Ud", "Deen", "Of"]
    words = text.split()
    return ' '.join([word.capitalize() if word.lower() not in exceptions else word for word in words])

# Function to convert 'INFRASTRUCTURAL NEEDS' into a bullet list
def create_infrastructure_bullets(infrastructure_needs):
    if infrastructure_needs:
        needs_list = infrastructure_needs.split(',')
        return ''.join(f"<li>{need.strip()}</li>" for need in needs_list)
    return "<li>No infrastructure needs listed</li>"

# Function to generate the popup content for the map marker
def generate_popup(row):
    infrastructure_bullets = create_infrastructure_bullets(row['INFRASTRUCTURAL NEEDS'])
    return (
        f"<b>Name of School:</b> {row['NAME OF SCHOOL']}<br>"
        f"<b>Category:</b> {row['CATEGORY']}<br>"
        f"<b>State:</b> {row['STATE']}<br>"
        f"<b>Local Govt Area:</b> {row['LGAs']}<br>"
        f"<b>Ward:</b> {row['WARD']}<br>"
        f"<b>Level of Dilapidation:</b> {row['LEVEL OF DILAPIDATION']}<br>"
        f"<b>Infrastructure Need:</b><ul>{infrastructure_bullets}</ul><br>"
        f"<img src='{row['IMAGE']}' width='100%' height='auto'>"
    )

# # Read data from the Excel file
# data = pd.read_excel('school_dilapidation_data.xlsx')

# Read data from the Excel file, and strip whitespace from column names
data = pd.read_excel('school_dilapidation_data.xlsx')
data.columns = data.columns.str.strip()  # Remove any leading/trailing whitespace from column names


# Print column names to verify
print("Column names in the DataFrame:", data.columns)

# Convert 'INFRASTRUCTURAL NEEDS' column to strings and handle NaN values
data['INFRASTRUCTURAL NEEDS'] = data['INFRASTRUCTURAL NEEDS'].fillna('').astype(str)

# Apply proper_case function to the 'NAME OF SCHOOL' column
data['NAME OF SCHOOL'] = data['NAME OF SCHOOL'].apply(proper_case)

# Create a base map centered on the South-West region of Nigeria
m = folium.Map(location=[7.3775, 3.9470], zoom_start=7, 
                tiles='OpenStreetMap')

# m = folium.Map(location=[7.3775, 3.9470], zoom_start=7, 
#                 tiles='Stamen Toner', 
#                 attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.')


# Loop through the data to add markers to the map
for idx, row in data.iterrows():
    # Geocode the "SCHOOL ADDRESS" to get latitude and longitude
    school_address = row.get('SCHOOL ADDRESS', '')
    if not school_address:
        logging.warning(f"No address found for school {row['NAME OF SCHOOL']}, skipping.")
        continue

    lat, long = get_lat_long_from_address(school_address)
    
    if lat is None or long is None:
        logging.warning(f"Geocoding failed for school {row['NAME OF SCHOOL']}, skipping.")
        continue

    # Add a delay between geocoding requests to avoid overloading the geocoding service
    time.sleep(1)

    # Generate popup content
    popup_info = generate_popup(row)

    # Add a marker to the map
    folium.Marker(
        location=[lat, long],
        popup=folium.Popup(popup_info, max_width=300),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save the map as an HTML file
m.save('static/infrastructure_map.html')

# Save the data to a JSON file for use in the HTML template
data.to_json('static/school_data.json', orient='records')

# Extract unique values for filters
filters = {
    'states': data['STATE'].dropna().unique().tolist(),
    'category': data['CATEGORY'].dropna().unique().tolist(),
    'lgas': data['LGAs'].dropna().unique().tolist(),
    'wards': data['WARD'].dropna().unique().tolist(),
    'levels_of_dilapidation': data['LEVEL OF DILAPIDATION'].dropna().unique().tolist(),
    'infrastructure_needs': data['INFRASTRUCTURAL NEEDS'].dropna().unique().tolist()
}

# Save the filters data to a JSON file
with open('static/filters.json', 'w') as f:
    json.dump(filters, f)

print("Map generation completed.")
