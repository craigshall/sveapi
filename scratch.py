import pandas as pd
import pickle


def single_val_cols_to_dict(df, single_value_dict=None, dict_name=None, count_na=True):

    if single_value_dict is None:
        single_value_dict = {}

    # if dict_name is set, store the dict_name in the index.name attribute of df
    # this functionality is to allow for easier reference to the dict from an attribute of the df
    if dict_name is not None:
        # if df.index.name has a value, store it in the single_value_dict under 'index.name'
        if df.index.name is not None:
            single_value_dict['index.name'] = df.index.name
        df.index.name = dict_name

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
