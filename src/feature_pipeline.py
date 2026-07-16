from sklearn.pipeline import Pipeline

from feature_engine.imputation import (
    MeanMedianImputer,
    CategoricalImputer,
)

from feature_engine.encoding import (
    RareLabelEncoder,
    OneHotEncoder,
)

from feature_engine.outliers import Winsorizer

from feature_engine.selection import (
    DropFeatures,
    DropConstantFeatures,
    SmartCorrelatedSelection,
)

from src.features import (
    NUMERICAL_FEATURES,
    CATEGORICAL_FEATURES,
    OUTLIER_FEATURES,
)


def build_preprocessing_pipeline():
    


    pipeline = Pipeline(

        [

        

            (
                "numeric_imputer",

                MeanMedianImputer(
                    imputation_method="median",
                    variables=NUMERICAL_FEATURES,
                ),
            ),

            (
                "categorical_imputer",

                CategoricalImputer(
                    fill_value="None",
                    variables=CATEGORICAL_FEATURES,
                ),
            ),

            (
                "rare_encoder",

                RareLabelEncoder(
                    tol=0.02,
                    n_categories=5,
                    replace_with="Rare",
                    variables=CATEGORICAL_FEATURES,
                ),
            ),

            (
                "one_hot",

                OneHotEncoder(
                    variables=CATEGORICAL_FEATURES,
                    ignore_format=True,
                ),
            ),

            (
                "winsorizer",

                Winsorizer(
                    capping_method="iqr",
                    tail="both",
                    fold=1.5,
                    variables=OUTLIER_FEATURES,
                ),
            ),

            (
                "drop_constant",

                DropConstantFeatures(
                    tol=0.99,
                ),
            ),

            (
                "correlated_features",

                SmartCorrelatedSelection(
                    threshold=0.90,
                    method="pearson",
                    selection_method="variance",
                ),
            ),

        ]

    )

    return pipeline