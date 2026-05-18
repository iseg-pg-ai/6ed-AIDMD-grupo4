import pandas as pd

df = pd.read_csv("Datasets/airport_traffic/airport_traffic_2025.csv")

print("Inspeção inicial (Aula #2)")
print("-------------------------------")
print("shape:", df.shape)  # Dimensões do dataset
print("-------------------------------")
print("columns:", df.columns)  # Colunas disponíveis
print("-------------------------------")
print("dtypes:", df.dtypes)  # Tipos de dados
print("-------------------------------")
print("nulls:", df.isnull().sum())  # Contagem de valores nulos por coluna
print("-------------------------------")
print("describe:", df.describe())  # Estatísticas descritivas para colunas numéricas
print("-------------------------------")
print("Tipos de dados e valores nulos:", df.info())  # Tipos de dados e valores nulos
print("-------------------------------")
print("Primeiras 5 linhas:", df.head())  # Primeiras 5 linhas
print("-------------------------------")
print("Últimas 5 linhas:", df.tail())  # Últimas 5 linhas
print("-------------------------------")
print(
    "Contagem de aeroportos únicos:", df["APT_NAME"].value_counts()
)  # Contagem de aeroportos únicos
print("-------------------------------")
print(
    "Contagem de estados únicos:", df["STATE_NAME"].value_counts()
)  # Contagem de estados únicos
print("-------------------------------")
print(
    "Intervalo de datas:", df["FLT_DATE"].min(), df["FLT_DATE"].max()
)  # Intervalo de datas
print("-------------------------------")
print(
    "Tipo de dados da coluna de data:", df["FLT_DATE"].dtype
)  # Tipo de dado da coluna de data
print("-------------------------------")
print("Fim da inspeção inicial.")
