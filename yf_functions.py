import yfinance as yf
import pandas as pd

DATE_FORMAT = '%Y-%m-%d'
# Pulling futures data from Yahoo Finance
def get_instrument_data_dict(ticker, start_date, end_date) -> dict:
    """
    Pulls futures data from list of instrument and creates a dictionary
    """
    data_dict = {}
    for instrument in ticker:
        data_dict[instrument] = get_instrument_data(instrument, start_date, end_date)
    return data_dict
    
def get_instrument_data(ticker, start_date, end_date)-> pd.DataFrame:
    """
    Pulls futures data from Yahoo Finance
    """
    ticker = yf.Ticker(ticker)
    data = ticker.history(start=start_date, end=end_date)
    df_data = pd.DataFrame(data)
    return df_data

def get_instrument_code(filename: str):
    """
    Opens Symbols.csv and turns it into a list with all the instrument codes
    """
    instrument_code = []
    df = pd.read_csv(filename)
    for code in df['Code']:
        instrument_code.append(f"{code}=F")
    return instrument_code

if __name__ == "__main__":
    instrument_list = get_instrument_code('Symbols.csv')
    print(instrument_list)
    data_dict = get_instrument_data_dict(instrument_list, '2024-01-01', '2024-01-02')
    # print first 5 rows of the first five instruments
    for key in data_dict.keys():
        print(data_dict[key].head())
