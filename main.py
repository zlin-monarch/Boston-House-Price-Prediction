import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler  # Assuming you use StandardScaler for scaling
import sklearn.externals.joblib as joblib

# Assuming your function is defined in a separate file (predict_housing_price.py)
from model_data.model_test import *
from utils.logger import create_logger


@st.cache_resource()
def load_model():
    global logger, model
    print('Loading model')
    logger = create_logger()  # Assuming your create_logger function
    model = joblib.load("./model_data/boston_housing_prediction.joblib")
    return model, logger
st.title("Boston Housing Price Prediction")


if "model" not in st.session_state.keys():
    model, logger = load_model()
    st.session_state["model"] = model
    st.session_state["logger"] = logger

model = st.session_state["model"]
logger = st.session_state["logger"]

# Initialize session state for lstat and ptratio if not already set
if 'lstat' not in st.session_state:
    st.session_state.lstat = 2.00
if 'ptratio' not in st.session_state:
    st.session_state.ptratio = 17.0

chas = st.radio('Charles River dummy variable (0: not adjacent, 1: adjacent)', [0, 1])
rm = st.slider('Average number of rooms per dwelling (Range)', min_value=4.0, max_value=8.5, step=0.1)
tax = st.slider('Full-value property tax rate (Range)', min_value=190, max_value=700, step=10)
b = st.slider('1000(Bk - 0.63 sqft) where Bk is the proportion of blacks by town', min_value=375, max_value= 395, step=10)


lstat = st.number_input('Lower status of the population (range from 2% to 30%)', min_value=2.00, max_value = 30.00, value = st.session_state.lstat, step = 1.00, format = '%0.01f')
ptratrio=  st.number_input('Pupil-teacher ratio by town (range from 17% to 21%)', min_value=17.00, max_value=21.00, value = st.session_state.ptratio, step = 0.1, format = '%0.01f')


# # Get user input for each feature
user_input = {
    "CHAS": chas,
    "RM": rm,
    "TAX": tax,
    "PTRATIO": ptratrio,
    "B": b,
    "LSTAT": lstat
}



# Convert user input to a dictionary with nested dictionaries (same format as your existing code)
data = {key: {"0": value} for key, value in user_input.items()}

# Run prediction when the button is clicked
from sklearn.preprocessing import StandardScaler

if st.button("Predict"):
    logger.info(f"Input: \n{data}")
    input_pd = pd.DataFrame(data)
    scaled_input = input_pd
    # scaler = StandardScaler().fit(input_pd.astype(float))
    # scaled_input = scaler.transform(input_pd.astype(float))
    logger.info(f"Scaled Input: \n{scaled_input}")
    prediction = list(model.predict(scaled_input))
    logger.info(f'Prediction: {prediction}')

    # Display prediction result
    st.success(f"Predicted Price: ${prediction[0]:.2f}")
