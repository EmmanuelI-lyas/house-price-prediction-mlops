import time

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


class ModelEvaluator:

    def __init__(self):
        self.start_time = None

    def start_timer(self):
        self.start_time = time.time()

    def training_time(self):
        return round(time.time() - self.start_time, 2)

    def evaluate(
        self,
        model,
        X_valid,
        y_valid,
        cv_score=None,
    ):

        predictions = model.predict(X_valid)

        metrics = {

            "MAE": float(
                mean_absolute_error(
                    y_valid,
                    predictions,
                )
            ),

            "RMSE": float(
                mean_squared_error(
                    y_valid,
                    predictions,
                ) ** 0.5
            ),

            "R2": float(
                r2_score(
                    y_valid,
                    predictions,
                )
            ),

            "CV_R2": float(cv_score) if cv_score is not None else float("nan"),

            "Training_Time": self.training_time(),

        }

        return metrics