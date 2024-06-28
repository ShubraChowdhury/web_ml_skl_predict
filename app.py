import os
import numpy as np
import pickle
from flask import (Flask, redirect, render_template, request, send_from_directory, url_for)
from azureml.core.model import Model


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
#model = pickle.load(open(send_from_directory(os.path.join(app.root_path, 'models'),'model.pkl'),'rb'))
#model_path = Model.get_model_path('model.pkl')
#with open(model_path, 'rb') as f:
#    model = pickle.load(f)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')



if __name__ == '__main__':
   app.run()
