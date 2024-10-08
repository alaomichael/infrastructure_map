from flask import Flask, render_template, request
import pandas as pd
import os
import requests

app = Flask(__name__)

# Folder to store downloaded images
IMAGE_FOLDER = 'static/images'

# Ensure the folder exists
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Filter to truncate long emails
@app.template_filter('truncate_email')
def truncate_email(email):
    return email[:37] + '...' if len(email) > 40 else email

# Filter to apply proper casing with exceptions
@app.template_filter('proper_case')
def proper_case(text):
    if isinstance(text, str):
        exceptions = {"Ud", "Deen", "of", "a"}
        words = text.split()
        capitalized_words = [
            word.capitalize() if word.lower() not in exceptions else word
            for word in words
        ]
        return ' '.join(capitalized_words)
    return text  # Return as is if not a string

# Function to download the image and store it locally if not already present
def download_image(url, file_name):
    """Download the image from the given URL and save it locally if not already present."""
    file_path = os.path.join(IMAGE_FOLDER, file_name)

    # Check if the image already exists to avoid duplicate downloads
    if not os.path.exists(file_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download image: {url}")
    else:
        print(f"Image already exists: {file_name}")

    return file_path  # Return the local path to the image

# Convert Google Drive link to direct image URL and download image
def convert_drive_link(url):
    """Convert Google Drive link to direct image URL and download image locally."""
    file_name = None

    # Check for Google Drive link format
    if "file/d/" in url:
        file_id = url.split("/d/")[1].split("/")[0]
        file_name = f"{file_id}.jpg"
        direct_link = f"https://drive.google.com/uc?id={file_id}"
    elif "open?usp=forms_web&id=" in url:
        file_id = url.split('id=')[1]
        file_name = f"{file_id}.jpg"
        direct_link = f"https://drive.google.com/uc?id={file_id}"
    else:
        return url  # Return the original URL if it's not a Google Drive link

    # Download and host the image locally
    if file_name:
        local_image_path = download_image(direct_link, file_name)
        return local_image_path  # Return local image path to be used in the application

    return url  # Return original URL if no valid format matched

# Load data from Excel file
def load_data(file_path):
    """Load data from an Excel file and return it as a list of dictionaries."""
    return pd.read_excel(file_path).to_dict(orient='records')

# Get unique values for a column from the dataset
def get_unique_values(data, column_name):
    """Extract unique values from a list of dictionaries for a given key (column)."""
    seen = set()
    unique_items = []
    
    for item in data:
        value = item.get(column_name)
        
        if value and pd.notna(value):
            # Normalize by stripping spaces and converting to lowercase for comparison
            if isinstance(value, str):
                normalized_value = value.strip().lower()
            else:
                normalized_value = str(value)
            
            if normalized_value not in seen:
                seen.add(normalized_value)
                unique_items.append(value)  # Keep the original value for display
    
    return sorted(unique_items)

# Clean the data by stripping whitespaces and converting URLs
def clean_data(data):
    """Clean the data by stripping whitespace from keys and converting image links."""
    cleaned_data = []
    for item in data:
        cleaned_item = {k.strip(): v for k, v in item.items()}  # Strip spaces from keys
        if 'IMAGE' in cleaned_item and isinstance(cleaned_item['IMAGE'], str):
            cleaned_item['IMAGE'] = convert_drive_link(cleaned_item['IMAGE'])
        cleaned_data.append(cleaned_item)
    return cleaned_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list_schools():
    # Load and clean data
    data = clean_data(load_data('school_dilapidation_data.xlsx'))

    # Get query parameters for filtering and search
    filters = {
        'search_query': request.args.get('search', '').strip().lower(),
        'category_filter': request.args.get('category', 'all'),
        'state_filter': request.args.get('state', 'all'),
        'lga_filter': request.args.get('lga', 'all'),
        'ward_filter': request.args.get('ward', 'all'),
        'dilapidation_filter': request.args.get('level_of_dilapidation', 'all'),
        'infrastructure_need_filter': request.args.get('infrastructure_need', 'all'),
    }

    # Apply filters to the data
    filtered_data = apply_filters(data, filters)

    # Pagination logic
    paginated_data, page, total_pages = paginate(filtered_data)

    # Get unique values for filters
    unique_values = {key: get_unique_values(filtered_data, key) for key in [
        'CATEGORY', 'STATE', 'LGAs', 'WARD', 'LEVEL OF DILAPIDATION', 'INFRASTRUCTURAL NEEDS']}

    return render_template(
        'list_schools.html',
        data=paginated_data,
        page=page,
        total_pages=total_pages,
        unique_category=unique_values['CATEGORY'],
        unique_states=unique_values['STATE'],
        unique_lgas=unique_values['LGAs'],
        unique_wards=unique_values['WARD'],
        unique_levels_of_dilapidation=unique_values['LEVEL OF DILAPIDATION'],
        unique_infrastructure_needs=unique_values['INFRASTRUCTURAL NEEDS'],
        search_query=filters['search_query'],
        category_filter=filters['category_filter'],
        state_filter=filters['state_filter'],
        lga_filter=filters['lga_filter'],
        ward_filter=filters['ward_filter'],
        dilapidation_filter=filters['dilapidation_filter'],
        infrastructure_need_filter=filters['infrastructure_need_filter']
    )

def apply_filters(data, filters):
    """Apply filters to the data based on the query parameters."""
    if filters['search_query']:
        data = [item for item in data if filters['search_query'] in item['NAME OF SCHOOL'].lower()]

    if filters['category_filter'] != 'all':
        data = [item for item in data if item['CATEGORY'] == filters['category_filter']]

    if filters['state_filter'] != 'all':
        data = [item for item in data if item['STATE'] == filters['state_filter']]

    if filters['lga_filter'] != 'all':
        data = [item for item in data if item['LGAs'] == filters['lga_filter']]

    if filters['ward_filter'] != 'all':
        try:
            ward_filter_value = int(filters['ward_filter'])  # Convert filter value to integer
            data = [item for item in data if int(item['WARD']) == ward_filter_value]
        except ValueError:
            pass  # Handle cases where the ward is not an integer (e.g., if there is bad data)

    if filters['dilapidation_filter'] != 'all':
        data = [item for item in data if item['LEVEL OF DILAPIDATION'] == filters['dilapidation_filter']]

    if filters['infrastructure_need_filter'] != 'all':
        data = [item for item in data if filters['infrastructure_need_filter'].lower() in (item['INFRASTRUCTURAL NEEDS'] or '').lower()]

    return data

def paginate(data):
    """Paginate the data."""
    items_per_page = 5
    page = request.args.get('page', 1, type=int)
    total_items = len(data)
    total_pages = (total_items + items_per_page - 1) // items_per_page
    start = (page - 1) * items_per_page
    end = start + items_per_page
    return data[start:end], page, total_pages

if __name__ == '__main__':
    app.run(debug=True)

