# sveapi
<h2>simple api creation project following along with kaggle's careercon 2019</h2>

<h3>3 day tutorial on api creation with kaggle notebooks here:</h3>
https://www.kaggle.com/rtatman/careercon-intro-to-apis<br>
https://www.kaggle.com/rtatman/careercon-making-an-app-from-your-modeling-code/<br>
https://www.kaggle.com/rtatman/careercon-deploying-apis-on-heroku-appengine

<h3>original files can be found in this repo:</h3>
https://github.com/rctatman/minimal_flask_example_heroku

<h4>Results</h4>
<p>A functioning API hosted at http://single-val-test-api.herokuapp.com/extractsinglevalues will return any columns that only contain a single value from a JSON serialized pandas DataFrame.  api_test.py creates a small DataFrame and runs it against the API, then loads a larger file (weather_test.csv) to run against the API.  This version runs with an explicit function instead of trying to load a pickled function because the pickled function led to AttributeError when hosted on Heroku.  I believe this error is related to this issue on StackOverflow: https://stackoverflow.com/questions/40287657/load-pickled-object-in-different-file-attribute-error.</p>
<h5>Next steps:</h5>
<p>Implement another API using the tutorial found here: https://www.datacamp.com/community/tutorials/machine-learning-models-api-python.  Before implementing my next API I will develop a function or model worth interfacing with, as opposed to just a simple implementation of one of my <a href="https://github.com/craigshall/chiptools">chiptools</a> functions as I did here.</p>
