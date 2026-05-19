import pandas as pd


# Data Loading
def loadDataset(dataset_path):
    """_summary_

    Args:
        dataset (string): path to dataset

    Returns:
        dataframe: read dataframe
    """
    df = pd.read_csv(dataset_path)
    return df


# Data Cleaning
def cleanDataset(df):
    df.columns = df.columns.str.strip()
    # Identifies which collumns of the dataframe are strings (or sometimes objects)
    string_columns = df.select_dtypes(include=["object", "string"]).columns
    # And sets all the values to uppercase
    df[string_columns] = df[string_columns].apply(lambda x: x.str.upper())

    # Identifies which collumns of the dataframe are ints (or sometimes floats)
    int_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in int_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # and fills the N/As with 0s instead
    df[int_cols] = df[int_cols].fillna(0).astype(int)

    return df
