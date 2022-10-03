from flask import Flask, escape, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

model = pickle.load(open("Stroke_model.pkl", 'rb'))

app = Flask(__name__)
@app.route('/analysis')
def analysis():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        gender = request.form['gender']
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        disease = int(request.form['heart_disease'])
        glucose = float(request.form['avg_glucose_level'])
        smoking = request.form['smoking_status']

        # gender
        if (gender == "Male"):
            gender_male=1
            gender_other=0
        elif(gender == "Other"):
            gender_male = 0
            gender_other = 1
        else:
            gender_male=0
            gender_other=0
        

        # smoking sttaus
        if(smoking=='formerly smoked'):
            smoking_status_formerly_smoked = 1
            smoking_status_never_smoked = 0
            smoking_status_smokes = 0
        elif(smoking == 'smokes'):
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_smokes = 1
        elif(smoking=="never smoked"):
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 1
            smoking_status_smokes = 0
        else:
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_smokes = 0

        feature = scaler.fit_transform([[age, hypertension, disease, glucose, gender_male, gender_other, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]])

        prediction = model.predict(feature)[0]
        # print(prediction) 
        # 
        if prediction==0:
            prediction = "NO" 
        else:
            prediction = "YES" 

        return render_template("index.html", prediction_text="Chance of Stroke Prediction is --> {}".format(prediction))   
         

    else:
        return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)