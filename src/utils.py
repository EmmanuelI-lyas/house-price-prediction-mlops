import json
import joblib
from pathlib import Path


def create_directory(path):
    """
    Create directory if it doesn't exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def save_pickle(obj, path):
    """
    Save Python object.
    """
    joblib.dump(obj, path)


def load_pickle(path):
    """
    Load saved object.
    """
    return joblib.load(path)


def save_json(data, path):
    """
    Save dictionary to JSON.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def load_json(path):
    """
    Load JSON file.
    """
    with open(path, "r") as file:
        return json.load(file)