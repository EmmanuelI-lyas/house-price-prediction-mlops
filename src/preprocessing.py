from src.config import config


# Load dataset once to infer columns

TARGET = config["data"]["target"]

# Columns to drop before preprocessing
DROP_FEATURES = [
    "Id",
]

# Numerical features
NUMERICAL_FEATURES = (
    df.drop(columns=DROP_FEATURES + [TARGET])
      .select_dtypes(include=["int64", "float64"])
      .columns
      .tolist()
)
DROP_COLUMNS = [
    "PoolQC",
    "MiscFeature",
    "Alley",
    "Fence",
]

CATEGORICAL_FEATURES = [
    col
    for col in df.select_dtypes(include=["object"]).columns
    if col not in DROP_COLUMNS
]


# Final feature list
FEATURES = NUMERICAL_FEATURES + CATEGORICAL_FEATURES
OUTLIER_FEATURES = [

    "LotFrontage",
    "LotArea",
    "MasVnrArea",

    "BsmtFinSF1",
    "BsmtUnfSF",
    "TotalBsmtSF",

    "1stFlrSF",
    "2ndFlrSF",
    "GrLivArea",

    "GarageArea",

    "WoodDeckSF",
    "OpenPorchSF",

]