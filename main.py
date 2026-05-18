import research_study as rs


def main():
    # Load the dataset into Python
    df = rs.loadDataset()

    # Data cleaning
    rs.cleanDataset(df)

    # Data transformation
    rs.transformDataset(df)

    rs.descriptive_analytics(df)

    # Generate Visualization
    rs.plot_top_airports(df)

    rs.visualise_single_variable(df, "FLT_TOT_1")
    rs.visualise_single_variable(df, "DIFF_TOTAL")

    rs.plot_top_diffs(df)

    print(df)


if __name__ == "__main__":
    main()
