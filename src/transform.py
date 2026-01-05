import pandas as pd


def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw sales data into a clean, analysis-ready fact table.

    Steps:
    1. Normalize column names
    2. Validate required schema
    3. Apply type conversions and basic cleaning
    """

    # --------------------------------------------------
    # 1. Normalize column names
    # --------------------------------------------------
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("á", "a")
        .str.replace("é", "e")
        .str.replace("í", "i")
        .str.replace("ó", "o")
        .str.replace("ú", "u")
    )

    # --------------------------------------------------
    # 2. Validate required columns (data contract)
    # --------------------------------------------------
    required_columns = [
        "producto",
        "categoria_del_producto",
        "precio",
        "fecha_de_compra",
        "cantidad_de_cuotas",
        "store_id"
    ]

    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # --------------------------------------------------
    # 3. Type casting & transformations
    # --------------------------------------------------

    # Precio: viene sin separador → COP
    df["precio"] = df["precio"].astype(float)

    # Cantidad de cuotas
    df["cantidad_de_cuotas"] = df["cantidad_de_cuotas"].astype(int)

    # Fecha (formato dd/mm/yyyy)
    df["fecha_de_compra"] = pd.to_datetime(
        df["fecha_de_compra"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    # --------------------------------------------------
    # 4. Optional: basic sanity filtering
    # --------------------------------------------------
    df = df[df["precio"] > 0]

    return df
