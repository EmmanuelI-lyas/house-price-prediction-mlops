import pandas as pd

from tests.test_api import sample_payload
from src.predict import HousePricePredictor


def test_prediction_pipeline():

    predictor = HousePricePredictor()

    df = pd.DataFrame([sample_payload])

    prediction = predictor.predict(df)

    assert prediction[0] > 0