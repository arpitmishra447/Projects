# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    tv = float(request.form['tv'])
    radio = float(request.form['radio'])
    newspaper = float(request.form['newspaper'])

    features = [[tv, radio, newspaper]]
    
    # Make prediction
    predicted_sales = model.predict(features)

    return render_template('index.html', prediction_text=f'Predicted Sales: {predicted_sales} units')

if __name__ == "__main__":
    app.run(debug=True)