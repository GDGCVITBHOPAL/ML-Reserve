import os
import sys
import pickle
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from customer_personality.logger.log import logging
from customer_personality.exception.exception_handler import AppException
from customer_personality.config.configuration import AppConfiguration
from customer_personality.pipeline.training_pipeline import TrainingPipeline

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    try:
        return render_template("index.html")
    except Exception as e:
            raise AppException(e, sys) from e



@app.route('/train',methods=['POST','GET'])
def train():
    if request.method == 'POST':
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            logging.info("Training Completed!")
            return render_template("index.html")

        except Exception as e:
            raise AppException(e, sys) from e



@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def predict():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Income =float(request.form['Income'])
            Recency =int(request.form['Recency'])
            Age =int(request.form['Age'])
            TotalSpendings =int(request.form['TotalSpendings'])
            Children =int(request.form['Children'])
            MonthEnrollement =int(request.form['MonthEnrollement'])

            data = [Income,Recency,Age,TotalSpendings,Children,MonthEnrollement]
            model = pickle.load(open(AppConfiguration().get_prediction_config().trained_model_path,'rb'))
            output = model.predict([data])[0]
            print(output)

            return render_template('results.html', prediction = str(output))

        except Exception as e:
            raise AppException(e, sys) from e

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5003,debug=True)
