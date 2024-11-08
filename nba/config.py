import logging
import yaml
from data_classes import Config
from pathlib import Path
from pydantic import ValidationError


def load_config(file_path: str = "config.yaml") -> Config:
    """
    Load and parse the configuration from a YAML file.
        # Example usage
        # config = load_config()
        # print(config.data.table)          
        # print(config.data.features_columns)  
        # print(config.model.name)
        # print(config.model.params.max_iter)
    """
    try:
        config_dict = yaml.safe_load(open(Path(__file__).parent.parent / "config.yaml", "r"))
        config = Config(**config_dict)
    except FileNotFoundError:
        logging.error("Configuration file not found.")
    except ValidationError as e:
        logging.error("Configuration validation error:", e)
    
    return config
