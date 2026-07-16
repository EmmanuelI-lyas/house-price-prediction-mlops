import pandas as pd

from fastapi import FastAPI
from mangum import Mangum

from src.predict import HousePricePredictor
from src.schema import HouseFeatures


app = FastAPI(

    title="House Price Prediction API",

    version="1.0.0",

    description="Predict house sale prices using a trained Scikit-Learn pipeline.",

)


predictor = HousePricePredictor()


@app.get("/")
def home():

    return {

        "message": "House Price Prediction API",

        "status": "running",

    }


@app.get("/health")
def health():

    return {

        "status": "healthy",

    }


@app.post("/predict")
def predict(features: HouseFeatures):

    data = pd.DataFrame([features.model_dump()])

    prediction = predictor.predict(data)

    return {

        "Predicted_Price": round(float(prediction[0]), 2)

    }


handler = Mangum(app)