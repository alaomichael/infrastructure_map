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

# # Convert 'INFASTRUCTURE NEED' column to strings and handle NaN values
# data['INFASTRUCTURE NEED'] = data['INFASTRUCTURE NEED'].apply(lambda x: str(x) if not pd.isna(x) else '')

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
#     infrastructure_need = truncate_text(row['INFASTRUCTURE NEED'], 30)

#     # Convert infrastructure need to a list and create bullet points
#     if row['INFASTRUCTURE NEED']:
#         infrastructure_list = row['INFASTRUCTURE NEED'].split(',')
#         infrastructure_bullets = ''.join(f"<li>{item.strip()}</li>" for item in infrastructure_list)
#     else:
#         infrastructure_bullets = "<li>No infrastructure needs listed</li>"

#     # Prepare the popup content with an image
#     popup_info = (
#         f"<b>Name of School:</b> {row['NAME OF SCHOOL']}<br>"
#         f"<b>Category:</b> {row['CATEGORIES']}<br>"
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

# Function to truncate text with ellipsis
def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length-3] + '...'
    return text

# Function to properly capitalize school names
def proper_case(text):
    exceptions = ["Ud", "Deen", "Of"]
    words = text.split()
    capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
    return ' '.join(capitalized_words)

# Read data from the Excel file
data = pd.read_excel('school_dilapidation_data.xlsx')

# Print column names to verify
print("Column names in the DataFrame:", data.columns)

# Ensure the column names match those in your Excel file
latitude_col = 'LATITUDE'
longitude_col = 'LONGITUDE'

# Convert 'INFASTRUCTURE NEED' column to strings and handle NaN values
data['INFASTRUCTURE NEED'] = data['INFASTRUCTURE NEED'].apply(lambda x: str(x) if not pd.isna(x) else '')

# Apply proper_case function to the 'NAME OF SCHOOL' column
data['NAME OF SCHOOL'] = data['NAME OF SCHOOL'].apply(proper_case)

# Create a base map centered on the South-West region of Nigeria
m = folium.Map(location=[7.3775, 3.9470], zoom_start=7)

# Add infrastructure data to the map with additional details in the popup
for idx, row in data.iterrows():
    # Check if latitude and longitude are missing
    if pd.isna(row[latitude_col]) or pd.isna(row[longitude_col]):
        lat, long = get_lat_long(row['LGAs'])
        if lat and long:
            data.at[idx, latitude_col] = lat
            data.at[idx, longitude_col] = long
        else:
            continue  # Skip if geocoding fails

    # Truncate the "infrastructure Need" field if necessary
    infrastructure_need = truncate_text(row['INFASTRUCTURE NEED'], 30)

    # Convert infrastructure need to a list and create bullet points
    if row['INFASTRUCTURE NEED']:
        infrastructure_list = row['INFASTRUCTURE NEED'].split(',')
        infrastructure_bullets = ''.join(f"<li>{item.strip()}</li>" for item in infrastructure_list)
    else:
        infrastructure_bullets = "<li>No infrastructure needs listed</li>"

    # Prepare the popup content with an image
    popup_info = (
        f"<b>Name of School:</b> {row['NAME OF SCHOOL']}<br>"
        f"<b>Category:</b> {row['CATEGORIES']}<br>"
        f"<b>State:</b> {row['STATE']}<br>"
        f"<b>Local Govt Area:</b> {row['LGAs']}<br>"
        f"<b>Ward:</b> {row['WARD']}<br>"
        f"<b>Level of Dilapidation:</b> {row['LEVEL OF DILAPIDATION']}<br>"
        f"<b>Infrastructure Need:</b><ul>{infrastructure_bullets}</ul><br>"
        f"<img src='{row['IMAGE']}' width='100%' height='auto'>"
    )
    
    folium.Marker(
        location=[row[latitude_col], row[longitude_col]],
        popup=folium.Popup(popup_info, max_width=300),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save the map
m.save('static/infrastructure_map.html')
