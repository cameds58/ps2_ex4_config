from pydantic import BaseModel

class DataPaths(BaseModel):
    data_file: str
    another_file: str