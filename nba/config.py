import yaml
from pydantic import ValidationError
from dataclasses import Config

def load_config(file_path: str = "config.yaml") -> Config:
    """Load and parse the configuration from a YAML file."""
    try:
        with open(file_path, "r") as f:
            config_dict = yaml.safe_load(f)
        config = Config(**config_dict)
        return config
    except FileNotFoundError:
        print("Configuration file not found.")
    except ValidationError as e:
        print("Configuration validation error:", e)

# Usage
config = load_config()
print(config.data.table)          # Example usage
print(config.data.features_columns)  
print(config.model.name)
print(config.model.params.max_iter)
