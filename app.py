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
    """Load data from an Excel file and return it as a DataFrame."""
    data = pd.read_excel(file_path)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list_schools():
    # Load data
    data = load_data('school_dilapidation_data.xlsx')

    # Filtering and Searching
    search_query = request.args.get('search', '').strip().lower()
    category_filter = request.args.get('category', 'all')
    state_filter = request.args.get('state', 'all')

    # Apply filters
    if search_query:
        data = data[data['NAME OF SCHOOL'].str.lower().str.contains(search_query)]
    if category_filter != 'all':
        data = data[data['CATEGORIES'] == category_filter]
    if state_filter != 'all':
        data = data[data['STATE'] == state_filter]

    # Pagination logic
    items_per_page = 5
    page = request.args.get('page', 1, type=int)
    total_items = len(data)
    total_pages = (total_items + items_per_page - 1) // items_per_page
    start = (page - 1) * items_per_page
    end = start + items_per_page
    paginated_data = data.iloc[start:end].to_dict(orient='records')

    # Get unique categories and states for filters
    unique_categories = data['CATEGORIES'].unique().tolist()
    unique_states = data['STATE'].unique().tolist()

    return render_template(
        'list_schools.html',
        data=paginated_data,
        page=page,
        total_pages=total_pages,
        unique_categories=unique_categories,
        unique_states=unique_states,
        search_query=search_query,
        category_filter=category_filter,
        state_filter=state_filter
    )

if __name__ == '__main__':
    app.run(debug=True)
