import pandas as pd

from src.config import config
from src.logger import logger


def load_train_data():
    """
    Load training dataset.
    """

    path = config["data"]["train_path"]

    logger.info(f"Loading training data: {path}")

    df = pd.read_csv(path)

    logger.info(f"Training Shape: {df.shape}")

    return df


def load_validation_data():
    """
    Load validation dataset.
    """

    path = config["data"]["validation_path"]

    logger.info(f"Loading validation data: {path}")

    df = pd.read_csv(path)

    logger.info(f"Validation Shape: {df.shape}")

    return df


def load_test_data():
    """
    Load Kaggle test dataset.
    """

    path = config["data"]["test_path"]

    logger.info(f"Loading test data: {path}")

    df = pd.read_csv(path)

    logger.info(f"Test Shape: {df.shape}")

    return df