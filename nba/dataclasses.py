from pydantic import BaseModel
from typing import List, Dict

class DataConfig(BaseModel):
    table: str
    data_path: str
    features_columns: List[str]

class ModelParams(BaseModel):
    max_iter: int
    random_state: int

class ModelConfig(BaseModel):
    name: str
    type: str
    params: ModelParams

class Config(BaseModel):
    data: DataConfig
    model: ModelConfig