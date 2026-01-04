import pandas as pd


REQUIRED_COLUMNS = [
    "customerid",
    "tenure",
    "monthlycharges",
    "totalcharges",
    "churn"
]


def validate_schema(df: pd.DataFrame) -> None:
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw JSON-normalized DataFrame into a clean, flat dataset.
    """

    # 1. Normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # 2. Extract and rename nested fields (EXPLICIT MODELING)
    df = df.rename(columns={
        "customer.tenure": "tenure",
        "account.charges.monthly": "monthlycharges",
        "account.charges.total": "totalcharges"
    })

    # 3. Select only relevant columns
    df = df[
        [
            "customerid",
            "tenure",
            "monthlycharges",
            "totalcharges",
            "churn"
        ]
    ]

    # 4. Validate schema
    validate_schema(df)

    # 5. Remove duplicates
    df = df.drop_duplicates()

    # 6. Handle missing critical fields
    df = df[df["customerid"].notna()]
    df = df[df["tenure"].notna()]

    # 7. Type casting
    df["tenure"] = df["tenure"].astype(int)
    df["monthlycharges"] = df["monthlycharges"].astype(float)
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

    # 8. Normalize categorical fields
    df["churn"] = df["churn"].map({"Yes": True, "No": False})

    return df
