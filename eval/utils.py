import pandas as pd

def add_datetime_set_index(data, time_col="Date"):
    data[time_col] = pd.to_datetime(data[time_col])
    data.set_index(time_col, inplace=True)
    return data