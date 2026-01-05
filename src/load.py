from pathlib import Path
import pandas as pd



def load_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Saves the transformed DataFrame to a final CSV file.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
