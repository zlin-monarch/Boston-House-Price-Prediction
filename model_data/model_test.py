from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import pandas as pd
from utils.logger import create_logger



def scale(payload):
    """Scales Payload"""
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict


def predict_housing_price(input_data):
    """
    Predicts housing price based on input data.
    :param input_data: A dictionary containing the model features.
    :return: A prediction of the housing price.
    """
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")    
    print('Model:', clf)
    input_pd = pd.DataFrame(input_data)
    scaled_input = scale(input_pd)
    prediction = list(clf.predict(scaled_input))
    return prediction


if __name__ == '__main__':
    logger = create_logger()

    input_data = {
        "CHAS": {"0": 0},
        "RM": {"0": 6.575},
        "TAX": {"0": 296.0},
        "PTRATIO": {"0": 15.3},
        "B": {"0": 396.9},
        "LSTAT": {"0": 4.98}
    }
    logger.info(f"Scaling Payload: \n{input_data}")
    logger.info('Loading model')
    prediction = predict_housing_price(input_data)
    logger.info(f'Prediction: {prediction}')
    # logger.debug("this will get printed")
    # logger.info("this will get printed")
    # logger.warning("this will get printed")
    # logger.error("this will get printed")
    # logger.critical("this will get printed")

