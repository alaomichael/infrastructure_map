# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('infrastructure_map.html')

@app.route('/list')
def list_school():
    # Read data from the Excel file
    data = pd.read_excel('path_to_your_excel_file.xlsx')
    return render_template('list_schools.html', data=data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run()
