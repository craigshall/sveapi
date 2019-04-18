import requests
import pandas as pd


weather_df = pd.read_csv('weather_test.csv')
print(requests.post('http://single_val_test_api.herokuapp.com/extractpackages', json=weather_df).json())
