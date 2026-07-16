import pandas as pd

from src.config import config

df = pd.read_csv(config["data"]["train_path"])

train_v1 = df.iloc[:800]

train_v2 = df.iloc[:1000]

train_v3 = df.iloc[:1200]

train_v4 = df

train_v1.to_csv(
    "data/ci_cd/train_v1.csv",
    index=False,
)

train_v2.to_csv(
    "data/ci_cd/train_v2.csv",
    index=False,
)

train_v3.to_csv(
    "data/ci_cd/train_v3.csv",
    index=False,
)

train_v4.to_csv(
    "data/ci_cd/train_v4.csv",
    index=False,
)

print("Datasets Created.")