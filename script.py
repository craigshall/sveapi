from flask import Flask, request
from serve import run_single_val
import json

app=Flask(__name__)

# Define our "extractsinglevalues" end point
@app.route('/extractsinglevalues', methods=['POST'])
def single_val_output():
    json_df = request.json
    # return(json.dumps(json_df))  # test basic functionality of api to return the input ; should be commented
    return run_single_val(json_df)
