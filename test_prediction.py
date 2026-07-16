import pandas as pd

from src.predict import HousePricePredictor

predictor = HousePricePredictor()

df = pd.read_csv("data/raw/test.csv")

prediction = predictor.predict(df.iloc[[0]])

print("Prediction:")
print(prediction)