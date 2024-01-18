import pandas as pd

def getMultiplierDict():
    # Read in the multiplier data
    df = pd.read_csv("Symbols.csv", index_col=0)
    # Convert the dataframe to a dictionary
    m_series = df["Point Value"].astype(int)

    multiplierDict = m_series.to_dict()
    # Return the dictionary
    return multiplierDict
