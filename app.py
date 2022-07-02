import pandas as pd
from flask import Flask, render_template, jsonify, render_template_string, request, flash
import json

# Just for full .head() viewing options
pd.options.display.max_columns = None
pd.options.display.max_rows = None

# This command create a class for our app
app = Flask(__name__)
app.secret_key = "test"


# Try with a custom dataframe
test_df = pd.DataFrame([
    ['jack', 22, 'china', 'https://www.google.com'],
    ['jill', 22, 'canada', 'https://www.cnn.com'],
    ['john', 24, 'canada', 'https://www.cnn.com'],
    ['jane', 30, 'australia','https://www.bbc.com']],
    columns=['name', 'age', 'country', 'link'])

# Create a json of the dataframe
test_df = test_df.values.tolist()


evidence_dataset = pd.read_excel('evidence_dataset.xlsx')
evidence_dataset = pd.DataFrame(evidence_dataset)
evidence_dataset = evidence_dataset.filter(['Country', 'Title', 'Category', 'Date', 'Link', 'Image'])
#
evidence_dataset = evidence_dataset.fillna("")
#evidence_dataset = evidence_dataset.to_json(orient='values')
evidence_dataset = evidence_dataset.values.tolist()
evidence_dataset

# # Try again
# evidence_dataset = [['Afghanistan', '(SEIA) UNDP COVID-19 Impact: Short term disruptions and policy considerations', 'Assessments (Multi-Sector)', 'Timestamp("2020-06-01 00:00:00")', 'https://www.undp.org/content/dam/undp/library/covid19/Afghanistan - Covid19 Impact Note - Final  April 15 2020.pdf']]
# evidence_dataset = pd.DataFrame(evidence_dataset, columns=['Country', 'Title', 'Category', 'Date', 'Link'])
# evidence_dataset = evidence_dataset.values.tolist()
# 1+1


# Adding the headings=headings allows
@app.route("/hello")
def index():
    return render_template("index.html", test_df=test_df, evidence_dataset=evidence_dataset)


if __name__ == '__main__':
    app.run(debug=True, port=4000)