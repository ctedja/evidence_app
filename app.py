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
test_data = [['jack', 23, 'china', 'https://www.google.com'],
             ['jill', 22, 'canada', 'https://www.cnn.com'],
             ['john', 24, 'canada', 'https://www.cnn.com'],
             ['jane', 30, 'australia', 'https://www.bbc.com']]
test_df = pd.DataFrame(test_data, columns=['name', 'age', 'country', 'link'])

# Create a json of the dataframe
test_df = test_df.values.tolist()
test_df

evidence_dataset = pd.read_excel('evidence_dataset.xlsx')
evidence_dataset = pd.DataFrame(evidence_dataset)
evidence_dataset = (evidence_dataset
                    .filter(['Country', 'Title', 'Category', 'Date', 'Link', 'Image'])
                    .tolist())

# Adding the headings=headings allows
@app.route("/hello")
def index():
    return render_template("index.html", test_df=test_df, evidence_dataset=evidence_dataset)


if __name__ == '__main__':
    app.run(debug=True, port=4000)