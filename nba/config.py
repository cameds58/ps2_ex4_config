import yaml
from pydantic import BaseModel
from config_classes import DataPaths

class Config(BaseModel):
    data_paths: DataPaths

def load_config():
    with open("config.yaml", "r") as f:
        config_dict = yaml.safe_load(f)
    return Config(**config_dict)
