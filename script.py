from flask import Flask
from serve import run_single_val

app=Flask(__name__)

# Define our "extractsinglevalues" end point
@app.route('/extractsinglevalues', methods=['POST'])
def single_val_output(json_df):
    run_single_val(json_df)
