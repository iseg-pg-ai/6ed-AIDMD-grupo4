import pandas as pd

import data_display as dd
import dataframe_utilities as du


def main():
    # Load the dataset into Python
    df_traffic_2025 = du.loadDataset("Datasets/traffic/airport_traffic_2025.csv")
    df_co2_2025 = du.loadDataset("Datasets/emmissions/co2_emmissions_by_state_2025.csv")

    # Data cleaning
    du.cleanDataset(df_traffic_2025)
    du.cleanDataset(df_co2_2025)

    df = pd.merge(
        df_traffic_2025,
        df_co2_2025,
        left_on=["YEAR", "MONTH_NUM", "STATE_NAME"],
        right_on=["YEAR", "MONTH", "STATE_NAME"],
        how="inner",
    )

    # Data transformation
    deriveVariables(df)

    dd.descriptive_analytics(df)
    # Generate Visualization
    dd.plot_top_airports(df)
    dd.visualise_single_variable(df, "FLT_TOT_1")
    dd.visualise_single_variable(df, "DIFF_TOTAL")
    dd.plot_top_diffs(df)
    print(df)


# Data transformation
def deriveVariables(df):
    df["DAY_OF_WEEK"] = pd.to_datetime(df["FLT_DATE"]).dt.day_name()

    # Calculate the difference between Airport Controller and Network Manager, setting it to 0 if Airport Controller is 0
    df["DIFF_ARRIVALS"] = df.apply(
        lambda row: (
            row["FLT_ARR_1"] - row["FLT_ARR_IFR_2"] if row["FLT_ARR_IFR_2"] != 0 else 0
        ),
        axis=1,
    )
    df["DIFF_DEPARTURES"] = df.apply(
        lambda row: (
            row["FLT_DEP_1"] - row["FLT_DEP_IFR_2"] if row["FLT_DEP_IFR_2"] != 0 else 0
        ),
        axis=1,
    )
    df["DIFF_TOTAL"] = df.apply(
        lambda row: (
            row["FLT_TOT_1"] - row["FLT_TOT_IFR_2"] if row["FLT_TOT_IFR_2"] != 0 else 0
        ),
        axis=1,
    )

    return df


if __name__ == "__main__":
    main()
