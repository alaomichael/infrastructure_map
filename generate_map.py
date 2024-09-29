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

import os
import requests
import folium
import pandas as pd
from urllib.parse import urlparse
import json
import time
import logging

# Setup logging
logging.basicConfig(filename='geocoding_errors.log', level=logging.ERROR)

# Define a constant for the image folder
IMAGE_FOLDER = 'static/images'  # Update this as necessary

# Function to convert Google Drive link to direct image URL
def convert_drive_link(url):
    """Convert Google Drive link to direct image URL and extract file name."""
    direct_link = None
    file_name = None

    # Check if it's a Google Drive link
    if "file/d/" in url:
        file_id = url.split("/d/")[1].split("/")[0]
        direct_link = f"https://drive.google.com/uc?id={file_id}"
        file_name = f"{file_id}.jpg"
    elif "open?usp=forms_web&id=" in url:
        file_id = url.split('id=')[1]
        direct_link = f"https://drive.google.com/uc?id={file_id}"
        file_name = f"{file_id}.jpg"
    else:
        return url, None  # If not a Google Drive link, return the original URL

    return direct_link, file_name

# Function to extract filename from URL
def extract_filename_from_url(url):
    """Extract the filename from a non-Google Drive URL."""
    parsed_url = urlparse(url)
    file_name = os.path.basename(parsed_url.path)

    # If the URL doesn't have a proper file name, return None
    if not file_name or '.' not in file_name:
        return None

    return file_name

# Function to download the image and store it locally if not already present
def download_image(url, school_name=None):
    """Download the image from the given URL and save it locally if not already present."""
    # Validate the URL
    if not isinstance(url, str) or not url.strip():
        logging.warning(f"Invalid URL for school: {school_name}")
        return None

    # Check if the URL is a Google Drive link and convert it if necessary
    converted_url, file_name = convert_drive_link(url)

    # If the file name is not derived from Google Drive, extract it from the URL
    if not file_name:
        file_name = extract_filename_from_url(converted_url)
        if not file_name:
            logging.error(f"Could not extract a valid file name from URL: {url}")
            return None

    file_path = os.path.join(IMAGE_FOLDER, file_name)

    # Check if the image already exists to avoid duplicate downloads
    if not os.path.exists(file_path):
        try:
            response = requests.get(converted_url)
            response.raise_for_status()  # Raise an error for bad responses

            # Ensure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Write the image to a file
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        except Exception as e:
            logging.error(f"Failed to download image from {converted_url}: {e}")
            return None  # Return None if download failed
    else:
        print(f"Image already exists: {file_name}")

    return file_path  # Return the local path to the image

# Example usage in processing data from Excel
def process_data(row):
    """Processes a single row, downloading its image."""
    image_url = row['IMAGE']
    school_name = row['NAME OF SCHOOL']
    
    # Download the image (or use cached local copy)
    local_image_path = download_image(image_url, school_name)
    
    if local_image_path:
        print(f"Image for {school_name} stored at {local_image_path}")
    else:
        print(f"Failed to download image for {school_name}")

# Function to truncate text with ellipsis
def truncate_text(text, max_length):
    return (text[:max_length - 3] + '...') if len(text) > max_length else text

# Function to properly capitalize school names
def proper_case(text):
    exceptions = {"Ud", "Deen", "Of", "a"}
    return ' '.join(word.capitalize() if word.lower() not in exceptions else word for word in text.split())

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
        f"<img src='{row['LOCAL_IMAGE']}' width='100%' height='auto'>"
    )

# Load and clean data from Excel file
def load_data(file_path):
    data = pd.read_excel(file_path)
    data.columns = data.columns.str.strip()  # Remove leading/trailing whitespace from column names
    data['INFRASTRUCTURAL NEEDS'] = data['INFRASTRUCTURAL NEEDS'].fillna('').astype(str)
    data['NAME OF SCHOOL'] = data['NAME OF SCHOOL'].apply(proper_case)
    
    # Apply download_image row-wise with the URL
    data['LOCAL_IMAGE'] = data.apply(lambda row: download_image(row['IMAGE'], row['NAME OF SCHOOL']), axis=1)
    
    return data

# Create a base map centered on the South-West region of Nigeria
def create_map(data):
    m = folium.Map(location=[7.3775, 3.9470], zoom_start=9, tiles='OpenStreetMap')

    for idx, row in data.iterrows():
        lat = row.get('LATITUDE')
        long = row.get('LONGITUDE')

        if pd.isna(lat) or pd.isna(long):
            logging.warning(f"Missing latitude or longitude for school {row['NAME OF SCHOOL']}, skipping.")
            continue

        # Generate popup content and add marker to the map
        popup_info = generate_popup(row)
        folium.Marker(
            location=[lat, long],
            popup=folium.Popup(popup_info, max_width=300),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    return m

# Extract unique values for filters
def extract_filters(data):
    return {
        'states': data['STATE'].dropna().unique().tolist(),
        'category': data['CATEGORY'].dropna().unique().tolist(),
        'lgas': data['LGAs'].dropna().unique().tolist(),
        'wards': data['WARD'].dropna().unique().tolist(),
        'levels_of_dilapidation': data['LEVEL OF DILAPIDATION'].dropna().unique().tolist(),
        'infrastructure_needs': data['INFRASTRUCTURAL NEEDS'].dropna().unique().tolist()
    }

def main():
    # Load data and create map
    data = load_data('school_dilapidation_data.xlsx')
    m = create_map(data)

    # Save the map as an HTML file
    m.save('static/infrastructure_map.html')

    # Save the data to a JSON file for use in the HTML template
    data.to_json('static/school_data.json', orient='records')

    # Extract filters and save to a JSON file
    filters = extract_filters(data)
    with open('static/filters.json', 'w') as f:
        json.dump(filters, f)

    print("Map generation completed.")

if __name__ == '__main__':
    main()



# import os
# import requests
# import folium
# import pandas as pd
# from geopy.geocoders import Nominatim
# from urllib.parse import urlparse
# import json
# import time
# import logging

# # Setup logging
# logging.basicConfig(filename='geocoding_errors.log', level=logging.ERROR)

# # Initialize geolocator
# geolocator = Nominatim(user_agent="geoapiExercises")

# # Function to get latitude and longitude from the school address
# def get_lat_long_from_address(address, geolocator):
#     try:
#         loc = geolocator.geocode(address)
#         return (loc.latitude, loc.longitude) if loc else (None, None)
#     except Exception as e:
#         logging.error(f"Geocoding failed for {address}: {e}")
#         return None, None

# # Define a constant for the image folder
# IMAGE_FOLDER = 'static/images'  # Update this as necessary

# # Function to convert Google Drive link to direct image URL
# def convert_drive_link(url):
#     """Convert Google Drive link to direct image URL and extract file name."""
#     direct_link = None
#     file_name = None

#     # Check if it's a Google Drive link
#     if "file/d/" in url:
#         file_id = url.split("/d/")[1].split("/")[0]
#         direct_link = f"https://drive.google.com/uc?id={file_id}"
#         file_name = f"{file_id}.jpg"
#     elif "open?usp=forms_web&id=" in url:
#         file_id = url.split('id=')[1]
#         direct_link = f"https://drive.google.com/uc?id={file_id}"
#         file_name = f"{file_id}.jpg"
#     else:
#         return url, None  # If not a Google Drive link, return the original URL

#     return direct_link, file_name

# # Function to extract filename from URL
# def extract_filename_from_url(url):
#     """Extract the filename from a non-Google Drive URL."""
#     parsed_url = urlparse(url)
#     file_name = os.path.basename(parsed_url.path)

#     # If the URL doesn't have a proper file name, return None
#     if not file_name or '.' not in file_name:
#         return None

#     return file_name

# # Function to download the image and store it locally if not already present
# def download_image(url, school_name=None):
#     """Download the image from the given URL and save it locally if not already present."""
#     # Validate the URL
#     if not isinstance(url, str) or not url.strip():
#         logging.warning(f"Invalid URL for school: {school_name}")
#         return None

#     # Check if the URL is a Google Drive link and convert it if necessary
#     converted_url, file_name = convert_drive_link(url)

#     # If the file name is not derived from Google Drive, extract it from the URL
#     if not file_name:
#         file_name = extract_filename_from_url(converted_url)
#         if not file_name:
#             logging.error(f"Could not extract a valid file name from URL: {url}")
#             return None

#     file_path = os.path.join(IMAGE_FOLDER, file_name)

#     # Check if the image already exists to avoid duplicate downloads
#     if not os.path.exists(file_path):
#         try:
#             response = requests.get(converted_url)
#             response.raise_for_status()  # Raise an error for bad responses

#             # Ensure the directory exists
#             os.makedirs(os.path.dirname(file_path), exist_ok=True)

#             # Write the image to a file
#             with open(file_path, 'wb') as file:
#                 file.write(response.content)
#             print(f"Downloaded: {file_name}")
#         except Exception as e:
#             logging.error(f"Failed to download image from {converted_url}: {e}")
#             return None  # Return None if download failed
#     else:
#         print(f"Image already exists: {file_name}")

#     return file_path  # Return the local path to the image

# # Example usage in processing data from Excel
# def process_data(row):
#     """Processes a single row, downloading its image."""
#     image_url = row['IMAGE']
#     school_name = row['NAME OF SCHOOL']
    
#     # Download the image (or use cached local copy)
#     local_image_path = download_image(image_url, school_name)
    
#     if local_image_path:
#         print(f"Image for {school_name} stored at {local_image_path}")
#     else:
#         print(f"Failed to download image for {school_name}")

# # Function to truncate text with ellipsis
# def truncate_text(text, max_length):
#     return (text[:max_length - 3] + '...') if len(text) > max_length else text

# # Function to properly capitalize school names
# def proper_case(text):
#     exceptions = {"Ud", "Deen", "Of", "a"}
#     return ' '.join(word.capitalize() if word.lower() not in exceptions else word for word in text.split())

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
#         f"<img src='{row['LOCAL_IMAGE']}' width='100%' height='auto'>"
#     )

# # Load and clean data from Excel file
# def load_data(file_path):
#     data = pd.read_excel(file_path)
#     data.columns = data.columns.str.strip()  # Remove leading/trailing whitespace from column names
#     data['INFRASTRUCTURAL NEEDS'] = data['INFRASTRUCTURAL NEEDS'].fillna('').astype(str)
#     data['NAME OF SCHOOL'] = data['NAME OF SCHOOL'].apply(proper_case)
    
#     # Apply download_image row-wise with the URL
#     data['LOCAL_IMAGE'] = data.apply(lambda row: download_image(row['IMAGE'], row['NAME OF SCHOOL']), axis=1)
    
#     return data

# # Create a base map centered on the South-West region of Nigeria
# def create_map(data):
#     m = folium.Map(location=[7.3775, 3.9470], zoom_start=9, tiles='OpenStreetMap')

#     for idx, row in data.iterrows():
#         school_address = row.get('SCHOOL ADDRESS', '')
#         if not school_address:
#             logging.warning(f"No address found for school {row['NAME OF SCHOOL']}, skipping.")
#             continue

#         lat, long = get_lat_long_from_address(school_address, geolocator)  # Pass the geolocator here
#         if lat is None or long is None:
#             logging.warning(f"Geocoding failed for school {row['NAME OF SCHOOL']}, skipping.")
#             continue

#         time.sleep(1)  # Delay between geocoding requests

#         # Generate popup content and add marker to the map
#         popup_info = generate_popup(row)
#         folium.Marker(
#             location=[lat, long],
#             popup=folium.Popup(popup_info, max_width=300),
#             icon=folium.Icon(color='blue', icon='info-sign')
#         ).add_to(m)

#     return m

# # Extract unique values for filters
# def extract_filters(data):
#     return {
#         'states': data['STATE'].dropna().unique().tolist(),
#         'category': data['CATEGORY'].dropna().unique().tolist(),
#         'lgas': data['LGAs'].dropna().unique().tolist(),
#         'wards': data['WARD'].dropna().unique().tolist(),
#         'levels_of_dilapidation': data['LEVEL OF DILAPIDATION'].dropna().unique().tolist(),
#         'infrastructure_needs': data['INFRASTRUCTURAL NEEDS'].dropna().unique().tolist()
#     }

# def main():
#     # Load data and create map
#     data = load_data('school_dilapidation_data.xlsx')
#     m = create_map(data)

#     # Save the map as an HTML file
#     m.save('static/infrastructure_map.html')

#     # Save the data to a JSON file for use in the HTML template
#     data.to_json('static/school_data.json', orient='records')

#     # Extract filters and save to a JSON file
#     filters = extract_filters(data)
#     with open('static/filters.json', 'w') as f:
#         json.dump(filters, f)

#     print("Map generation completed.")

# if __name__ == '__main__':
#     main()
