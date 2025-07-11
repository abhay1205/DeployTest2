import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('PricePredictorModel.pkl','rb'))
st.title("House Price Predictor")

cPark = float(st.text_input("No.of Cars Parking: ","1"))
landSize = float(st.text_input("Enter Land Size: ","1000"))
buildingArea = float(st.text_input("Enter Building Area: ","1000"))
yearBuilt = float(st.text_input("Enter Year built: ", "2008"))

featureInput = np.array([[cPark, landSize, buildingArea, yearBuilt]])

price = model.predict(featureInput)

st.write(f'Hello, *World!* :sunglasses: . Customer Group : {price} ')