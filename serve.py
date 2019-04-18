import pickle


def run_single_val(input_df):
    # read in a processor from our pickled file. Don't forget to
    # include "rb", which lets us _r_ead a _b_inary file.
    pickle_single_vals = pickle.load(open("single_vals.pkl", "rb"))

    return pickle_single_vals(input_df)

