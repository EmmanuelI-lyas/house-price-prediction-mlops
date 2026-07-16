import numpy as np
import pandas as pd

from src.utils import load_pickle
from src.config import config
from src.logger import logger
from src.features import FEATURES


class HousePricePredictor:

    def __init__(self):

        model_path = (
            f"{config['output']['model_dir']}"
            f"{config['output']['pipeline_name']}"
        )

        logger.info(f"Loading model: {model_path}")

        self.pipeline = load_pickle(model_path)

    def predict(
        self,
        data: pd.DataFrame,
    ):

        logger.info("Running prediction...")

        # Remove Id if present
        if "Id" in data.columns:
            data = data.drop(columns=["Id"])

        # Rename API field names to training dataset field names
        data = data.rename(
            columns={
                "FirstFlrSF": "1stFlrSF",
                "SecondFlrSF": "2ndFlrSF",
                "ThreeSsnPorch": "3SsnPorch",
            }
        )

        # Keep columns in the same order used during training
        data = data[FEATURES]

        predictions = self.pipeline.predict(data)

        return np.expm1(predictions)