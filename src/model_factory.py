from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
)

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
)


def get_model(model_name: str, config: dict):
    """
    Return the requested regression model.
    """

    models = {

        "linear_regression": LinearRegression(),

        "ridge": Ridge(),

        "lasso": Lasso(),

        "decision_tree": DecisionTreeRegressor(
            random_state=config["split"]["random_state"]
        ),

        "random_forest": RandomForestRegressor(
            n_estimators=config["random_forest"]["n_estimators"],
            max_depth=config["random_forest"]["max_depth"],
            random_state=config["random_forest"]["random_state"],
            n_jobs=-1,
        ),

        "extra_trees": ExtraTreesRegressor(
            n_estimators=300,
            random_state=config["split"]["random_state"],
            n_jobs=-1,
        ),

        "gradient_boosting": GradientBoostingRegressor(
            random_state=config["split"]["random_state"]
        ),

    }

    if model_name not in models:
        raise ValueError(f"Unknown model: {model_name}")

    return models[model_name]