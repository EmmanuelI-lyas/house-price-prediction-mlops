from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV

from src.feature_pipeline import build_preprocessing_pipeline
from src.hyperparameter_factory import get_param_grid
from src.evaluator import ModelEvaluator
from src.logger import logger
from src.config import config


class ModelTrainer:

    def __init__(
        self,
        model,
        model_name,
    ):

        self.model = model
        self.model_name = model_name

        self.pipeline = Pipeline(

            [

                (
                    "preprocessing",
                    build_preprocessing_pipeline(),
                ),

                (
                    "model",
                    self.model,
                ),

            ]

        )

    def train(

        self,

        X_train,
        y_train,

        X_valid,
        y_valid,

    ):

        evaluator = ModelEvaluator()

        evaluator.start_timer()

        best_params = {}

        cv_score = None

        # Decide whether to perform hyperparameter tuning
        if (

            config["training"]["hyperparameter_search"]

            and

            self.model_name in config["tuned_models"]

        ):

            param_grid = get_param_grid(self.model)

        else:

            param_grid = None

        # Hyperparameter Search
        if param_grid is not None:

            logger.info(

                f"Running RandomizedSearchCV for {self.model_name}"

            )

            search = RandomizedSearchCV(

                estimator=self.pipeline,

                param_distributions={

                    f"model__{k}": v

                    for k, v in param_grid.items()

                },

                n_iter=config["training"]["n_iter"],

                cv=config["training"]["cv"],

                scoring="r2",

                random_state=42,

                n_jobs=-1,

            )

            search.fit(

                X_train,

                y_train,

            )

            self.pipeline = search.best_estimator_

            best_params = search.best_params_

            cv_score = search.best_score_

        else:

            self.pipeline.fit(

                X_train,

                y_train,

            )

        metrics = evaluator.evaluate(

            self.pipeline,

            X_valid,

            y_valid,

            cv_score=cv_score,

        )

        return {

            "pipeline": self.pipeline,

            "metrics": metrics,

            "best_params": best_params,

        }