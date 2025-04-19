import pandas as pd
import datetime

def example():
    #implementation
    pass


def dataframe_individual_day(df, day):
    """
    Parameters:
        df (pd.Dataframe): The dataframe with a datetime index.
        day (datetime.date or datetime.datetime): The day to filter the dataframe.

    Returns:
        pd.Dataframe: Dataframe with only that day's data

    """
    # Ensure the 'datetime' column is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(df['datetime']):
        df['datetime'] = pd.to_datetime(df['datetime'])

    #If 'day' is a datetime.datetime, extract the date
    if isinstance(day, pd.Timestamp) or isinstance(day, datetime.datetime):
        day = day.date()
    
    #Returns filtered dataframe with only the data from the specified day
    return df[df['datetime'].dt.date == day]

def mean_of_multiple_days(df, column):
    """
    Parameters:
        df (pd.Dataframe): The dataframe with a datetime index and column titled column.
        column (str): The column to calculate the mean

    Returns:
        closest_day_df (pd.Dataframe): Dataframe with only the data from the day with the closest mean value to the mean of the means of all the days.
    """

    #Creates a dataframe with the means of each day
    daily_means = df.groupby(df['datetime'].dt.date)[column].mean()

    #Finds the mean value of the means of all the days
    mean_of_daily_means = daily_means.mean()
    
    #Finds the day with the closest mean value to the mean of the means
    closest_day = (daily_means - mean_of_daily_means).abs().idxmin()

    return closest_day




    

