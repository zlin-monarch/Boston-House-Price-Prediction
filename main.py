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

st.image("./static/Images/Background.jpg")
st.title("Boston Housing Price Prediction")


if "model" not in st.session_state.keys():
    model, logger = load_model()
    st.session_state["model"] = model
    st.session_state["logger"] = logger

# print(st.session_state.keys())
model = st.session_state["model"]
logger = st.session_state["logger"]

# Initialize session state for lstat and ptratio if not already set
# if 'lstat' not in st.session_state:
#     st.session_state.lstat = 2.00
# if 'ptratio' not in st.session_state:
#     st.session_state.ptratio = 17.0

if 'first_visit' not in st.session_state:
    st.session_state.first_visit=True
else:
    st.session_state.first_visit=False

if st.session_state.first_visit:
    st.balloons()
    st.session_state.first_visit=False

chas = st.radio('Charles River dummy variable (0: not adjacent, 1: adjacent)', [0, 1])
rm = st.slider('Average number of rooms per dwelling (Range)', min_value=4.0, max_value=8.5, step=0.1)
tax = st.slider('Full-value property tax rate (Range)', min_value=190, max_value=700, step=10)
b = st.slider('1000(Bk - 0.63 sqft) where Bk is the proportion of blacks by town', min_value=375, max_value= 395, step=10)


lstat = st.number_input('Lower status of the population (range from 2% to 30%)', min_value=2.00, max_value = 30.00, step = 1.00, format = '%0.01f')
ptratrio=  st.number_input('Pupil-teacher ratio by town (range from 17% to 21%)', min_value=17.00, max_value=21.00, step = 0.1, format = '%0.01f')


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
col1, col2 = st.columns(2)
with col1:
    if st.button("Predict", type = 'primary'):
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


import streamlit.components.v1 as components
with col2:
    if st.button('Feel Lucky', type='secondary'):
        st.write("If you like this app, please consider to buy me a coffee") 
        components.html(
            """
            <form action="https://www.paypal.com/donate" method="post" target="_top">
                <input type="hidden" name="hosted_button_id" value="8JJTGY95URQCQ" />
                <input type="image" src="https://pics.paypal.com/00/s/MDY0MzZhODAtNGI0MC00ZmU5LWI3ODYtZTY5YTcxOTNlMjRm/file.PNG" height="35" border="0" name="submit" title="Donate with PayPal" alt="Donate with PayPal button" />
                <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
            </form>
            """,
            height=45
        )
        st.write("so I can keep it alive. Thank you!")