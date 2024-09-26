# from flask import Flask, render_template, request
# import pandas as pd

# app = Flask(__name__)

# @app.template_filter('truncate_email')
# def truncate_email(email):
#     if len(email) > 40:
#         return email[:37] + '...'
#     return email

# # Custom Jinja filter for proper casing
# @app.template_filter('proper_case')
# def proper_case(text):
#     exceptions = ["Ud", "Deen", "Of"]
#     words = text.split()
#     capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
#     return ' '.join(capitalized_words)

# app.jinja_env.filters['proper_case'] = proper_case

# def load_data(file_path):
#     """Load data from an Excel file and return it as a dictionary."""
#     data = pd.read_excel(file_path)
#     return data.to_dict(orient='records')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/list')
# def list_schools():
#     data = load_data('school_dilapidation_data.xlsx')

#     # Pagination logic
#     items_per_page = 5  # Set the number of items per page
#     page = request.args.get('page', 1, type=int)  # Get the current page number from query params
#     total_items = len(data)  # Get total number of items
#     total_pages = (total_items + items_per_page - 1) // items_per_page  # Calculate total pages
#     start = (page - 1) * items_per_page  # Calculate the starting index for the current page
#     end = start + items_per_page  # Calculate the ending index for the current page
#     paginated_data = data[start:end]  # Get the data for the current page

#     return render_template('list_schools.html', data=paginated_data, page=page, total_pages=total_pages)

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import pandas as pd

# app = Flask(__name__)

# @app.template_filter('truncate_email')
# def truncate_email(email):
#     if len(email) > 40:
#         return email[:37] + '...'
#     return email

# @app.template_filter('proper_case')
# def proper_case(text):
#     exceptions = ["Ud", "Deen", "Of"]
#     words = text.split()
#     capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
#     return ' '.join(capitalized_words)

# app.jinja_env.filters['proper_case'] = proper_case

# def load_data(file_path):
#     """Load data from an Excel file and return it as a DataFrame."""
#     data = pd.read_excel(file_path)
#     return data

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/list')
# def list_schools():
#     # Load data
#     data = load_data('school_dilapidation_data.xlsx')

#     # Filtering and Searching
#     search_query = request.args.get('search', '').strip().lower()
#     category_filter = request.args.get('category', 'all')
#     state_filter = request.args.get('state', 'all')

#     # Apply filters
#     if search_query:
#         data = data[data['NAME OF SCHOOL'].str.lower().str.contains(search_query)]
#     if category_filter != 'all':
#         data = data[data['CATEGORIES'] == category_filter]
#     if state_filter != 'all':
#         data = data[data['STATE'] == state_filter]

#     # Pagination logic
#     items_per_page = 5
#     page = request.args.get('page', 1, type=int)
#     total_items = len(data)
#     total_pages = (total_items + items_per_page - 1) // items_per_page
#     start = (page - 1) * items_per_page
#     end = start + items_per_page
#     paginated_data = data.iloc[start:end].to_dict(orient='records')

#     # Get unique categories and states for filters
#     unique_categories = data['CATEGORIES'].unique().tolist()
#     unique_states = data['STATE'].unique().tolist()

#     return render_template(
#         'list_schools.html',
#         data=paginated_data,
#         page=page,
#         total_pages=total_pages,
#         unique_categories=unique_categories,
#         unique_states=unique_states,
#         search_query=search_query,
#         category_filter=category_filter,
#         state_filter=state_filter
#     )

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.template_filter('truncate_email')
def truncate_email(email):
    if len(email) > 40:
        return email[:37] + '...'
    return email

@app.template_filter('proper_case')
def proper_case(text):
    exceptions = ["Ud", "Deen", "Of"]
    words = text.split()
    capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
    return ' '.join(capitalized_words)

app.jinja_env.filters['proper_case'] = proper_case

def load_data(file_path):
    """Load data from an Excel file and return it as a list of dictionaries."""
    return pd.read_excel(file_path).to_dict(orient='records')

def get_unique_values(data, column_name):
    """Extract unique values from a list of dictionaries for a given key (column)."""
    return sorted(set(item[column_name] for item in data if column_name in item and pd.notna(item[column_name])))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list_schools():
    # Load data
    data = load_data('school_dilapidation_data.xlsx')

    # Get query parameters for filtering and search
    search_query = request.args.get('search', '').strip().lower()
    category_filter = request.args.get('category', 'all')
    state_filter = request.args.get('state', 'all')
    lga_filter = request.args.get('lga', 'all')
    ward_filter = request.args.get('ward', 'all')
    dilapidation_filter = request.args.get('level_of_dilapidation', 'all')
    infrastructure_need_filter = request.args.get('infrastructure_need', 'all')

    # Apply filters
    if search_query:
        data = [item for item in data if search_query in item['NAME OF SCHOOL'].lower()]
    if category_filter != 'all':
        data = [item for item in data if item['CATEGORIES'] == category_filter]
    if state_filter != 'all':
        data = [item for item in data if item['STATE'] == state_filter]
    if lga_filter != 'all':
        data = [item for item in data if item['LGAs'] == lga_filter]
    if ward_filter != 'all':
        data = [item for item in data if item['WARD'] == ward_filter]
    if dilapidation_filter != 'all':
        data = [item for item in data if item['LEVEL OF DILAPIDATION'] == dilapidation_filter]
    if infrastructure_need_filter != 'all':
        data = [item for item in data if infrastructure_need_filter.lower() in (item['INFASTRUCTURE NEED'] or '').lower()]

    # Pagination logic
    items_per_page = 5
    page = request.args.get('page', 1, type=int)
    total_items = len(data)
    total_pages = (total_items + items_per_page - 1) // items_per_page
    start = (page - 1) * items_per_page
    end = start + items_per_page
    paginated_data = data[start:end]

    # Get unique values for filters
    unique_categories = get_unique_values(data, 'CATEGORIES')
    unique_states = get_unique_values(data, 'STATE')
    unique_lgas = get_unique_values(data, 'LGAs')
    unique_wards = get_unique_values(data, 'WARD')
    unique_levels_of_dilapidation = get_unique_values(data, 'LEVEL OF DILAPIDATION')
    unique_infrastructure_needs = get_unique_values(data, 'INFASTRUCTURE NEED')

    return render_template(
        'list_schools.html',
        data=paginated_data,
        page=page,
        total_pages=total_pages,
        unique_categories=unique_categories,
        unique_states=unique_states,
        unique_lgas=unique_lgas,
        unique_wards=unique_wards,
        unique_levels_of_dilapidation=unique_levels_of_dilapidation,
        unique_infrastructure_needs=unique_infrastructure_needs,
        search_query=search_query,
        category_filter=category_filter,
        state_filter=state_filter,
        lga_filter=lga_filter,
        ward_filter=ward_filter,
        dilapidation_filter=dilapidation_filter,
        infrastructure_need_filter=infrastructure_need_filter
    )

if __name__ == '__main__':
    app.run(debug=True)
