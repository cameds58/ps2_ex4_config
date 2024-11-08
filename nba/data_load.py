import pandas as pd
from pathlib import Path

def load_csv(data_path: Path) -> pd.DataFrame:
    """
    Function to load a CSV file into a pandas DataFrame.

    Args:
        data_path (Path): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(data_path)

if __name__ == "__main__":
    # Define the base directory dynamically (assuming script is inside 'nba' folder)
    base_dir = Path(__file__).resolve().parent.parent  # Go up one level from the 'nba' folder
    data_path = base_dir / "data" / "game.csv"  # Point to the 'data/game.csv'

    # Load and print the DataFrame
    df = load_csv(data_path)
    print(df)
