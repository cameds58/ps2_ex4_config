import pandas as pd
from pathlib import Path

def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)

if __name__ == "__main__":
    # Define the base directory dynamically (assumes the CSV is within the current script's directory)
    base_dir = Path(__file__).parent
    data_path = base_dir / "all_my_great_data" / "game.csv"

    # Load and print the DataFrame
    df = load_csv(data_path)
    print(df)
