from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.template_filter('truncate_email')
def truncate_email(email):
    if len(email) > 40:
        return email[:37] + '...'
    return email

# Custom Jinja filter for proper casing
@app.template_filter('proper_case')
def proper_case(text):
    exceptions = ["Ud", "Deen", "Of"]
    words = text.split()
    capitalized_words = [word.capitalize() if word.lower() not in exceptions else word for word in words]
    return ' '.join(capitalized_words)

app.jinja_env.filters['proper_case'] = proper_case

def load_data(file_path):
    """Load data from an Excel file and return it as a dictionary."""
    data = pd.read_excel(file_path)
    return data.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list_schools():
    data = load_data('school_dilapidation_data.xlsx')
    return render_template('list_schools.html', data=data)

if __name__ == '__main__':
    app.run()
