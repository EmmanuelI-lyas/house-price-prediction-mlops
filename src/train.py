import numpy as np
import pandas as pd

from src.config import config

from src.data_loader import (
    load_train_data,
    load_validation_data,
)

from src.validator import validate_dataframe

from src.features import FEATURES, TARGET

from src.model_factory import get_model

from src.trainer import ModelTrainer

from src.logger import logger

from src.utils import (
    create_directory,
    save_pickle,
    save_json,
)


def train():

    # Create models directory
    create_directory("models")

    logger.info("Loading Dataset...")

    # Load datasets
    train_df = load_train_data()
    valid_df = load_validation_data()

    # Validate datasets
    validate_dataframe(
        train_df,
        target=TARGET,
    )

    validate_dataframe(
        valid_df,
        target=TARGET,
    )

    # Features & target
    X_train = train_df[FEATURES]
    y_train = np.log1p(train_df[TARGET])

    X_valid = valid_df[FEATURES]
    y_valid = np.log1p(valid_df[TARGET])

    results = []

    best_pipeline = None
    best_model = None
    best_params = {}
    best_r2 = float("-inf")

    # Train every model
    for model_name in config["model"]["models"]:

        logger.info(f"Training {model_name}")

        model = get_model(
            model_name,
            config,
        )

        trainer = ModelTrainer(

            model=model,

            model_name=model_name,

        )

        output = trainer.train(

            X_train,

            y_train,

            X_valid,

            y_valid,

        )

        metrics = output["metrics"]

        params = output["best_params"]

        pipeline = output["pipeline"]

        logger.info(metrics)

        results.append(

            {

                "Model": model_name,

                **metrics,

            }

        )

        if metrics["R2"] > best_r2:

            best_r2 = metrics["R2"]

            best_model = model_name

            best_pipeline = pipeline

            best_params = params

    # Results dataframe
    results_df = pd.DataFrame(results)

    logger.info("\n%s", results_df)

    results_df.to_csv(

        "models/model_summary.csv",

        index=False,

    )

    # Save best pipeline
    save_pickle(

        best_pipeline,

        "models/house_pipeline.pkl",

    )

    # Save metrics
    save_json(

        {

            "Best_Model": best_model,

            "Best_R2": float(best_r2),

            "Best_Params": best_params,

        },

        "models/metrics.json",

    )

    logger.info(f"Best Model : {best_model}")

    logger.info(f"Best R2 : {best_r2:.4f}")

    logger.info("Training Finished Successfully.")


if __name__ == "__main__":

    train()