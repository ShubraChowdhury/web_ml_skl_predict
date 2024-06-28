import os
import numpy as np
import pickle
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)
# model = pickle.load(open('.models/model.pkl', 'rb'))
model = pickle.load(open(send_from_directory(os.path.join(app.root_path, 'models'),'model.pkl'),'rb'))

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')



if __name__ == '__main__':
   app.run()
