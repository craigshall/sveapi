import requests
import pandas as pd

# originally ran with a file...this appeared to time out the connection
#weather_df = pd.read_csv('weather_test.csv')

#run with a tiny dataframe as proof of concept
time = '2019-04-02 11:00:00'  # arbitrary time to start the datetime index
df = pd.DataFrame(index=pd.date_range(time, periods=3, freq='1H'),
             columns=['col1', 'col2', 'col3'], data=[[1.0, 2.0, 3.0], [1.0, 4.0, 3.0], [1.0, 6.0, 3.0]])
print(requests.post('http://single-val-test-api.herokuapp.com/extractsinglevalues', json=df.to_json())) # .json())
