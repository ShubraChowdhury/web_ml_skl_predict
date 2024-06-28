import numpy as np
from flask import Flask, request, render_template
import pickle

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
#model = pickle.load(open('models/model.pkl', 'rb'))


#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def index():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission. 
#Redirect to /predict page with the output
#@app.route('/predict',methods=['POST'])
#def predict():

    #int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    #features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    #prediction = model.predict(features)  # features Must be in the form [[a, b]]

    #output = round(prediction[0], 2)

    #return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output))


#When the Python interpreter reads a source file, it first defines a few special variables. 
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__). 
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here. 
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run()
