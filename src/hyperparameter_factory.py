from sklearn.linear_model import (
    Ridge,
    Lasso,
)

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
)


def get_param_grid(model):

    """
    Returns parameter grid for RandomizedSearchCV.
    If model does not require tuning,
    return None.
    """

    if isinstance(model, Ridge):

        return {

            "alpha": [
                0.01,
                0.1,
                1,
                10,
                100,
            ],

        }

    elif isinstance(model, Lasso):

        return {

            "alpha": [
                0.0001,
                0.001,
                0.01,
                0.1,
                1,
            ],

        }

    elif isinstance(model, DecisionTreeRegressor):

        return {

            "max_depth": [
                None,
                5,
                10,
                20,
                30,
            ],

            "min_samples_split": [
                2,
                5,
                10,
            ],

            "min_samples_leaf": [
                1,
                2,
                4,
            ],

        }

    elif isinstance(model, RandomForestRegressor):

        return {

            "n_estimators": [
                100,
                200,
                300,
                500,
            ],

            "max_depth": [
                None,
                10,
                20,
                30,
            ],

            "min_samples_split": [
                2,
                5,
                10,
            ],

            "min_samples_leaf": [
                1,
                2,
                4,
            ],

        }

    elif isinstance(model, ExtraTreesRegressor):

        return {

            "n_estimators": [
                100,
                200,
                300,
            ],

            "max_depth": [
                None,
                10,
                20,
            ],

            "min_samples_split": [
                2,
                5,
            ],

        }

    elif isinstance(model, GradientBoostingRegressor):

        return {

            "n_estimators": [
                100,
                200,
            
            ],

            "learning_rate": [
                0.01,
                0.05,
                0.1,
            ],

            "max_depth": [
                10,
                
                
            ],

        }

    return None