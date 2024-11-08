import pandas as pd
from pathlib import Path
import config

def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path) 

if __name__ == "__main__":
    # Load the configuration
    config = config.load_config()
    data_path = Path(__file__).parent.parent / config.data.data_path

    # Load and print the DataFrame
    df = load_csv(data_path)
    print(df)
