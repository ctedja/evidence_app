import pandas as pd
from flask import Flask, render_template, jsonify, render_template_string, request, flash
import json
# import numpy as np
# # import plotly_express as px
# import plotly.graph_objects as go
# import datetime
# from fuzzywuzzy import process
# import geopandas as gpd
# # import dash_leaflet as dl


# Just for full .head() viewing options
pd.options.display.max_columns = None
pd.options.display.max_rows = None


# This command create a class for our app
app = Flask(__name__)
app.secret_key = "test"


# Try with a custom dataframe
test_data = [['mack', 10, 'china'], ['john', 15, 'canada'], ['jane', 14, 'australia']]

# Create the pandas DataFrame
test_df = pd.DataFrame(test_data, columns=['name', 'age', 'country'])


# Create a json of the dataframe
#json_df = test_df.to_json()
# json_df = test_df.set_index('Name').to_json(orient='index')
json_df = test_df.to_dict(orient='index')
json_df

evidence_dataset = pd.read_excel('evidence_dataset.xlsx')
evidence_dataset = pd.DataFrame(evidence_dataset)
evidence_dataset = evidence_dataset.to_json(orient='index')
evidence_dataset


# Adding the headings=headings allows
@app.route("/hello")
def index():
    return render_template("index.html", json_df=json_df, evidence_dataset=evidence_dataset)

# @app.route("/test")
# def test():
#     return json_df

if __name__ == '__main__':
    app.run(debug=True, port=4000)




# evidence_dataset.describe()
# evidence_dataset.info()
# evidence_dataset.head()

