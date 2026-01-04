from ingest import ingest_json
from transform import transform_data
from load import load_to_csv, load_to_postgres


def run_pipeline():
    raw_df = ingest_json(
        source_path="data/source/telecomX_Data.json",
        raw_path="data/raw/telecom_raw.json"
    )

    clean_df = transform_data(raw_df)

    load_to_csv(
        clean_df,
        output_path="data/final/telecom_final.csv"
    )

    load_to_postgres(
        clean_df,
        table_name="telecom_customers",
        db_url="postgresql+psycopg2://telecom_user:telecom_pass@localhost:5432/telecom_db"
    )


if __name__ == "__main__":
    run_pipeline()
