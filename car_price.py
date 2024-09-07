import pickle
import pandas as pd
import datetime
import numpy as np
import streamlit as st



cars_df = pd.read_csv("./car-price.csv", encoding='ISO-8859-1', on_bad_lines='skip')


st.write(
    """
# Cars_24 price prediction 
    """
)

st.dataframe(cars_df.head())


col1, col2 = st.columns(2)

fuel_type = col1.selectbox(
    "What is your fuel type?",
    ("Diesel", "Petrol", "CNG", "LPG", "Electric"),
)


engine_size = col1.slider("What's your Engine Size?", 500, 5000, step=100)


transmission_type = col2.selectbox(
    "What is your Transmission type?",
    ("Manual", "Automatic"),
)


seats = col2.selectbox(
    "How Many Seats?",
    (2, 4,6,7,8,11),
)

# inputfeatures = [[2018.0,1,4000, fuel_type, transmission_type, 19.70, engine,86.30, seats]]
encode_dict = {"fuel_type":{'Diesel':1, 'Petrol':2, 'CNG':3, 'LPG':4, 'Electric':5}, "seller_type":{'Diesel': 1, 'Individual':2, 'Trustmark Dealer':3}, "transmission_type": {'Manual': 1, 'Automatic':2} }

def model_pred(fuel_type,transmission_type, engine, seats):

    with open("car_pred_model", 'rb') as file:
        reg_model = pickle.load(file) 
        
        inputfeatures = [[2018.0,1,4000, fuel_type, transmission_type, 19.70, engine,86.30, seats]]
        return reg_model.predict(inputfeatures)

if (st.button("Predict Price")):
    fuel_type = encode_dict['fuel_type'][fuel_type]

    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine_size, seats)

    st.text(f"price of the car is {np.round(price[0],2)} lakh rupees")
