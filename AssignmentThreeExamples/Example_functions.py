# A function to print "Hello World!"
def printExample ():
    print("Hello World!")


# The following code is from Team 1's week 6 presentation located in Spring_2025_VIP > Team 1 (Pyoneers) > Week6 > VIP_Top5ForDay.ipynb
def filter_top5_meters_all_data(df, date_str):
    """
    Filters the dataframe for a specific date, finds the top 5 unique 'meter_name' entries 
    with the highest mean values (without averaging), and returns all data for those meters 
    on that day, sorted by 'mean' in descending order.

    Parameters:
        df (pd.DataFrame): The dataframe with a datetime index and 'meter_name' as an index.
        date_str (str): Date in 'YYYY-MM-DD' format to filter.

    Returns:
        pd.DataFrame: Dataframe containing all data for the top 5 meter names on the selected date.
    """
    # Filter data for the chosen date
    filtered_df = df.loc[date_str]
    
    # Reset index to treat 'meter_name' as a column before sorting
    filtered_df = filtered_df.reset_index()
    
    # Find the top 5 unique meter names based on the highest single mean value (not averaged)
    top5_meters = (
        filtered_df.sort_values(by="mean", ascending=False)["meter_name"]
        .unique()[:5]  # Get the first 5 unique meter names
    )
    
    # Filter the original dataframe to keep only those top 5 meters
    top5_df = filtered_df[filtered_df["meter_name"].isin(top5_meters)]
    
    # Sort the final dataframe by 'mean' in descending order
    top5_df = top5_df.sort_values(by="mean", ascending=False)
    
    return top5_df