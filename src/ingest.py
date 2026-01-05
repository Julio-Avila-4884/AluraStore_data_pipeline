from pathlib import Path
import pandas as pd


def ingest_sales_data(source_dir: str, output_path: str) -> pd.DataFrame:
    """
    Reads sales data from multiple store CSV files, adds store_id,
    and saves a consolidated raw dataset.
    """

    source_path = Path(source_dir)
    all_dfs = []

    for csv_file in source_path.glob("sample_tienda_*.csv"):
        store_id = csv_file.stem.split("_")[-1]  # 1, 2, 3, 4

        df = pd.read_csv(csv_file)
        df["store_id"] = int(store_id)

        all_dfs.append(df)

    if not all_dfs:
        raise ValueError("No source files found in data/source")

    raw_df = pd.concat(all_dfs, ignore_index=True)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    raw_df.to_csv(output_path, index=False)

    return raw_df
