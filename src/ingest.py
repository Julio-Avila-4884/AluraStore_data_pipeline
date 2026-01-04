import json
from pathlib import Path
import pandas as pd


def ingest_json(source_path: str, raw_path: str) -> pd.DataFrame:
    """
    Reads a JSON file, stores an unmodified raw copy,
    and returns a DataFrame for downstream processing.
    """
    # Ensure raw directory exists
    Path(raw_path).parent.mkdir(parents=True, exist_ok=True)

    # Load JSON from source
    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Store raw JSON (unmodified)
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # Convert to DataFrame for pipeline processing
    df = pd.json_normalize(data)

    return df
