import pandas as pd

def calculate_net_load(load_df, pv_df):
    """
    Merges building load and PV data, then calculates net load.

    Args:
        load_df (pd.DataFrame): Load data with 'Timestamp' and 'kW'
        pv_df (pd.DataFrame): PV data with 'Timestamp' and 'kW'

    Returns:
        pd.DataFrame: Combined dataframe with Net Load (kW)
    """
    combined_df = pd.merge(load_df, pv_df, on="Timestamp", how="inner")
    combined_df.rename(columns={
        "kW_x": "Building Load (kW)",
        "kW_y": "PV Generation (kW)"
    }, inplace=True)
    combined_df["Net Load (kW)"] = combined_df["Building Load (kW)"] - combined_df["PV Generation (kW)"]
    return combined_df

def calculate_daily_max(df, timestamp_col="Timestamp", value_col="Net Load (kW)"):
    """
    Groups data by date and calculates the max value for each day.

    Args:
        df (pd.DataFrame): Input dataframe with timestamp and a numeric column
        timestamp_col (str): Name of the timestamp column
        value_col (str): Name of the column to find daily max

    Returns:
        pd.DataFrame: DataFrame with Date and Daily Max column
    """
    df["Date"] = df[timestamp_col].dt.date
    daily_max = df.groupby("Date")[value_col].max().reset_index()
    daily_max.rename(columns={value_col: f"Daily Max {value_col}"}, inplace=True)
    return daily_max
