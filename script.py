from flask import Flask
from serve import apply_single_val  

app=Flask(__name__)

# Define our "single_vals" end point
@app.route('/single_vals')
def single_val_output(input_df):
    # read in a processor from our pickled file. Don't forget to 
    # include "rb", which lets us _r_ead a _b_inary file.
    pickle_single_vals = pickle.load(open("single_vals.pkl", "rb"))

    # apply it to some sample text to make sure it works
    apply_single_val(pickle_single_vals, input_df) 
