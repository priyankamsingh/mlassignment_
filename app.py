import pickle
from flask import Flask, request,render_template, json
import joblib
from pandas import DataFrame
import pandas as pd
#from jinja2 import escape
from markupsafe import escape
from src.data_preprocessing import preprocess_data
from src.model_prediction import model_predict

app = Flask(__name__)

@app.route('/',methods=["Get","POST"])
def home():
    return render_template("index.html")

@app.route('/predict',methods=["Get","POST"])
def predict():
    uploaded_file = request.files['file']
    df = pd.read_csv(uploaded_file)
    df = preprocess_data(df_1=df)
    with open("model/logistic_regression_model_v4_FINAL_FINAL.pkl", 'rb') as file:
            model = pickle.load(file)
    predictions_test = model_predict(df, model)
    return predictions_test.to_json(orient="split")

#def data_validation(df):
     # some logic to check dimension of the data 
  #   assert df.shape[0] == 40 
   #  return df


if __name__ == '__main__':
     app.run(debug=True, port=5002)