import pandas as pd
from flask import Flask, render_template, jsonify, render_template_string, request, flash
import json
import datetime
from datetime import datetime

# Just for full .head() viewing options
pd.options.display.max_columns = None
pd.options.display.max_rows = None

# This command create a class for our app
app = Flask(__name__)
app.secret_key = "test"


# Try with a custom dataframe
test_df = pd.DataFrame([
    ['Australia', 'Report #1', 'Category #1', '2021-01-01', 'https://www.google.com', 'https://reliefweb.int/sites/default/files/styles/thumbnail/public/previews/c5/2d/c52de4ba-42d8-4383-8310-eb1a6966e803.png'],
    ['Canada', 'Report #2', 'Category #1', '2021-01-01', 'https://www.google.com', 'https://reliefweb.int/sites/default/files/styles/thumbnail/public/previews/c5/2d/c52de4ba-42d8-4383-8310-eb1a6966e803.png'],
    ['China', 'Report #3', 'Category #2', '2021-01-01', 'https://www.google.com', 'https://reliefweb.int/sites/default/files/styles/thumbnail/public/previews/c5/2d/c52de4ba-42d8-4383-8310-eb1a6966e803.png']],
    columns=['Country', 'Title', 'Category', 'Date', 'Link', 'Image'])
test_df['Date'] = pd.to_datetime(test_df['Date'])

# Create a json of the dataframe
test_df = test_df.fillna("")
test_df = test_df.values.tolist()


evidence_dataset = pd.read_excel('evidence_dataset.xlsx')
evidence_dataset = pd.DataFrame(evidence_dataset)
evidence_dataset = evidence_dataset.filter(['Country', 'Title', 'Category', 'Date', 'Link', 'Image'])
evidence_dataset['Date'] = evidence_dataset['Date'].dt.date
evidence_dataset = evidence_dataset.fillna("")
#evidence_dataset = evidence_dataset.to_json(orient='values')
evidence_dataset = evidence_dataset.values.tolist()


# # Try again
# evidence_dataset = [['Afghanistan', '(SEIA) UNDP COVID-19 Impact: Short term disruptions and policy considerations', 'Assessments (Multi-Sector)', 'Timestamp("2020-06-01 00:00:00")', 'https://www.undp.org/content/dam/undp/library/covid19/Afghanistan - Covid19 Impact Note - Final  April 15 2020.pdf']]
# evidence_dataset = pd.DataFrame(evidence_dataset, columns=['Country', 'Title', 'Category', 'Date', 'Link'])
# evidence_dataset = evidence_dataset.values.tolist()
# 1+1


@app.route("/hello")
def index():
    return render_template("index.html", test_df=test_df, evidence_dataset=evidence_dataset)


if __name__ == '__main__':
    app.run(debug=True, port=4000)