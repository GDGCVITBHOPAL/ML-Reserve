from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn


# Path of our Logistic regression model:
modelPath = '/Campus-Recruitment/Models/LRModel.pkl'
# Initializing the Flask framework:
app = Flask(__name__)
# Loading our model for later use:
model = pickle.load(open("../Campus-Recruitment/Models/LRModel.pkl", "rb"))

# Making routes for our flask framework:
# 1. Home route:
@app.route('/')
def home():
    return render_template("index.html")

# 2. Predict route:
@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # SSC score of the student:
        sscScore = float(request.form['ssc'])
        
        # HSC score of the student:
        hscScore = float(request.form['hsc'])
        
        # Degree % of the student:
        degree = float(request.form['degree'])
        
        # Work experience of the student:
        workExperience = request.form['work-ex']
        if (workExperience == 'yes'):
            workExperience = 1
        else:
            workExperience = 0
            
        # MBA percentage of the student:
        mba = float(request.form['mba-p'])
        
        # E-test percentage of the student:
        eTest = float(request.form['e-test'])
        
        # Gender of the student:
        gender = request.form['gender']
        if (gender == 'male'):
            gender = 1
        else:
            gender = 0
            
        # Degree type of the student:
        degree_type = request.form['degree_type']
        if degree_type == 'cmm&mgmt':
            degree_type = 1
        else:
            degree_type = 0
            
        specialization = request.form['specialization']
        if specialization == 'mkt&finc':
            specialization = 1
        else:
            specialization = 0
            
        # Predictions:
        prediction = model.predict([[
            sscScore,
            hscScore,
            degree,
            workExperience,
            mba,
            eTest,
            gender,
            degree_type,
            specialization
        ]])
        
        output = prediction[0]
        
        if output == 1:
            return render_template("index.html", prediction_text='You can be recruited!')
        else:
            return render_template("index.html", prediction_text='You cannot be recruited. Try again next time!')
        
if __name__ == '__main__':
    app.run(debug=True)