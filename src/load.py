from pathlib import Path
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


def load_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Saves the transformed DataFrame to a final CSV file.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def load_to_postgres(
    df: pd.DataFrame,
    table_name: str,
    db_url: str
) -> None:
    """
    Loads the DataFrame into a PostgreSQL table.

    Fails fast if PostgreSQL is not available.
    """
    try:
        engine = create_engine(db_url)

        # Test connection explicitly
        with engine.connect() as conn:
            pass

    except OperationalError as e:
        raise RuntimeError(
            "PostgreSQL no está disponible. "
            "Verifica que Docker esté levantado y las credenciales sean correctas."
        ) from e

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
