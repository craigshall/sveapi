from flask import Flask
from serve import run_single_val

app=Flask(__name__)

# Define our "extractsinglevalues" end point
@app.route('/extractsinglevalues')
def single_val_output(input_df):
    run_single_val(input_df)
