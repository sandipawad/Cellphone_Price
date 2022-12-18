from flask import Flask,render_template,request,url_for

import pandas as pd
import numpy as np

import sklearn

import config1

from utils import MobilePrice

app =Flask(__name__)

@app.route('/')
def hello_flask():

    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])

def price_prediction():


    if request.method=='POST':

        data = request.form

        mb_price= MobilePrice(data)

        price= mb_price.get_mobile_price()

        print('::::::::',price)

        return   render_template('index.html' ,prediction=price)




if __name__ =='__main__':

    app.run(debug=True)
