from pathlib import Path
import yaml


# Project Root
ROOT_DIR = Path(__file__).resolve().parent.parent

# Config File
CONFIG_PATH = ROOT_DIR / "configs" / "config.yaml"


def load_config():
    """
    Load configuration from YAML file.
    """
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)

    return config


# Load once
config = load_config()