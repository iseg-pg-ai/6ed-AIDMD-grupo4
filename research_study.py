def loadDataset():
    df = pd.read_csv("Datasets/airport_traffic/airport_traffic_2025.csv", sep=";")
    return df

def cleanDataset(df):
    df.columns = df.columns.str.strip()
    flt_cols = [col for col in df.columns if col.strip().startswith("FLT")]

    for col in flt_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df[flt_cols] = df[flt_cols].fillna(0).astype(int)

    return df

def transformDataset(df):
    df["DAY_OF_WEEK"] = df["FLT_DATE"].dt.day_name()
    df["DIFF_ARRIVALS"] = df["FLT_ARR_1"] - df["FLT_ARR_IFR_2"]
    df["DIFF_DEPARTURES"] = df["FLT_DEP_1"] - df["FLT_DEP_IFR_2"]
    df["DIFF_TOTAL"] = df["FLT_TOT_1"] - df["FLT_TOT_IFR_2"]

    return df

def visualise_single_variable(df, variable):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[variable], bins=50, kde=True)
    plt.title("Distribution of Total Flights (IFR)")
    plt.xlabel("Total Flights")
    plt.ylabel("Frequency")
    plt.show()
    return df

def plot_top_airports(df):
    top_airports = df.groupby("APT_NAME")["FLT_TOT_1"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_airports.values, y=top_airports.index, palette="Blues_r")
    plt.title("Top 10 Busiest Airports (Based on Network Manager Data)")
    plt.xlabel("Total IFR Flights")
    plt.ylabel("Airport Name")
    plt.tight_layout()
    plt.show()
