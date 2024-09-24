from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def load_data(file_path):
    """Load data from an Excel file and return it as a dictionary."""
    data = pd.read_excel(file_path)
    return data.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/map')
# def map_view():
#     return render_template('infrastructure_map.html')

@app.route('/list')
def list_schools():
    data = load_data('school_dilapidation_data.xlsx')
    return render_template('list_schools.html', data=data)

if __name__ == '__main__':
    app.run()
