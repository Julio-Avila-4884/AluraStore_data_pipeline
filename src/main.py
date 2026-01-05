from ingest import ingest_sales_data
from transform import transform_sales_data
from load import load_to_csv


def run_pipeline() -> None:
    """
    Runs the Alura Store data pipeline:
    Ingest → Transform → Load
    """

    # Paths del pipeline
    source_dir = "data/source"
    raw_output_path = "data/raw/alura_store_raw.csv"
    final_output_path = "data/final/alura_store_fact_sales.csv"

    # 1. Ingest
    raw_df = ingest_sales_data(
        source_dir=source_dir,
        output_path=raw_output_path
    )

    # 2. Transform
    fact_df = transform_sales_data(raw_df)

    # 3. Load
    load_to_csv(
        df=fact_df,
        output_path=final_output_path
    )


if __name__ == "__main__":
    run_pipeline()

