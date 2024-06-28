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



if __name__ == '__main__':
   app.run()
