import pandas as pd

from sklearn.model_selection import train_test_split

from src.config import config
from src.utils import create_directory


def split_data():

    df = pd.read_csv("data/raw/train.csv")

    train_df, valid_df = train_test_split(

        df,

        test_size=config["split"]["test_size"],

        random_state=config["split"]["random_state"],

    )

    create_directory("data/processed")

    train_df.to_csv(
        "data/processed/train_split.csv",
        index=False,
    )

    valid_df.to_csv(
        "data/processed/valid_split.csv",
        index=False,
    )

    print(train_df.shape)
    print(valid_df.shape)


if __name__ == "__main__":

    split_data()