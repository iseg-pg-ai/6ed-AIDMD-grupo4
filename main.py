import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def loadDataset():

    df = pd.read_csv("Datasets/airport_traffic/airport_traffic_2025.csv", sep=";")
    return df


def cleanDataset(df):

    df.columns = (
        df.columns.str.strip()
    )  # Normaliza os nomes das colunas, para permitir acesso abaixo
    # print(df.columns.tolist())

    # Obter todas as colunas que começam com FLT
    flt_cols = [col for col in df.columns if col.strip().startswith("FLT")]

    for col in flt_cols:
        # Se for uma coluna de texto com espaços, temos que tirar os espaços
        df[col] = df[col].astype(str).str.strip()

        # Força todas as colunas com FLT a serem numericas, se não tiverem um
        # valor numerico, o valor é forçado a NaN, com o errors="coerce"
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convertemos as colunas de volta para valores inteiros e forçamos a inteiro
    df[flt_cols] = df[flt_cols].fillna(0).astype(int)

    return df


def transformDataset(df):
    # Transforma 'FLT_DATE' no formato datetime do python
    # NOT WORKING FIX THIS df["FLT_DATE"] = pd.to_datetime(df["FLT_DATE"])

    # Extrai o dia da semana (Util para comparar Voos semanais vs Voos ao fim de semana)
    df["DAY_OF_WEEK"] = df["FLT_DATE"].dt.day_name()

    # Calcula diferenças entre o Network Manager e o Airport Operator
    # (BEEG data processing)
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
    # Group by Airport Name and sum the total flights
    top_airports = (
        df.groupby("APT_NAME")["FLT_TOT_1"].sum().sort_values(ascending=False).head(10)
    )

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_airports.values, y=top_airports.index, palette="Blues_r")
    plt.title("Top 10 Busiest Airports (Based on Network Manager Data)")
    plt.xlabel("Total IFR Flights")
    plt.ylabel("Airport Name")
    plt.tight_layout()
    plt.show()


# Load the dataset into Python
df = loadDataset()
print(df)

# Data cleaning
cleanDataset(df)
print(df)

# Data transformation
transformDataset(df)
print(df)


# Data representation
# Data visualization
# Generate graphs
# plot_top_airports(df)

# Data integration
# Employ exploratory data analysis techniques.
