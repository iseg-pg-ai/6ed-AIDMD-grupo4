import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats


# Data representation
def descriptive_analytics(df):
    summary_stats = df.describe()
    print("Summary Statistics:")
    print(summary_stats)

    # Correlation matrix
    columns_to_include = ["MONTH_NUM", "FLT_DEP_1", "FLT_ARR_1", "FLT_TOT_1"]
    correlation_matrix = df[columns_to_include].corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    # T-tests for comparing means
    t_test_result = stats.ttest_ind(df["FLT_ARR_1"], df["FLT_ARR_IFR_2"])
    print("\nT-test Result for Arrival Flights:")
    print(t_test_result)

    # Chi-square test for categorical variables
    chi2_test_result = stats.chi2_contingency(
        pd.crosstab(df["APT_NAME"], df["DAY_OF_WEEK"])
    )
    print("\nChi-Square Test Result for Airport and Day of Week:")
    print(chi2_test_result)


# Data visualization
def visualise_single_variable(df, variable):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[variable], bins=50, kde=True)
    plt.title("Distribution of " + variable)
    plt.xlabel("Total Flights")
    plt.ylabel("Frequency")
    plt.show()
    return df


# Data visualization
def plot_top_airports(df):
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

    # Data visualization


def plot_top_diffs(df):
    top_airports = (
        df.groupby("APT_NAME")["DIFF_TOTAL"].sum().sort_values(ascending=False).head(10)
    )
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_airports.values, y=top_airports.index, palette="Blues_r")
    plt.title("Top 10 biggest diferences")
    plt.xlabel("Diferenece between Network Controller and Network Manager")
    plt.ylabel("Airport Name")
    plt.tight_layout()
    plt.show()
