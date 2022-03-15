
import joblib
from flask import Flask,render_template,request

app = Flask('__name__')

model = joblib.load("iris_model")

@app.route("/")

def main():
    return render_template("index.html", n = "PRESS ENTER")

@app.route("/send", methods = ['POST','GET'])

def compile():
    global model
    l1 = request.form['1']
    l2 = request.form['2']
    l3 = request.form['3']
    l4 = request.form['4']
    pred = model.predict([[l1,l2,l3,l4]])
    return render_template("index.html",n =pred)

