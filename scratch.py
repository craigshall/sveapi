import pandas as pd
import pickle


def single_val_cols_to_dict(df_json):

    single_value_dict = {}
    count_na = True  # in original function was a parameter...keeping in case of future parameterization

    df = pd.read_json(df_json)

    # go through columns, if only 1 unique value, store in single_value_dict with column_name:single_value pair
    for col in df.columns:
        if df[col].nunique(dropna=(not count_na)) == 1:  # if count_na=True do not dropna from nunique, see docstring
            first_valid_idx = df[col].first_valid_index()  # keep from having to call first_valid_index twice
            if first_valid_idx is not None:
                single_value_dict[col] = df.at[first_valid_idx, col]
            else:
                single_value_dict[col] = NaN

    return single_value_dict


# save our file (make sure our file permissions are "wb",
# which will let us _w_rite a _b_inary file)
pickle.dump(single_val_cols_to_dict, open("single_vals.pkl", "wb"))
