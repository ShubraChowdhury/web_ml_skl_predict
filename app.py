import os
import numpy as np
import pickle
from flask import (Flask, redirect, render_template, request, send_from_directory, url_for)
import sklearn
#global model
model = pickle.load(open('models/model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(features)  # features Must be in the form [[a, b]]

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output))

if __name__ == '__main__':
   app.run()
