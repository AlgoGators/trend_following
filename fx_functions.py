import pandas as pd

def create_fx_series_given_adjusted_prices_dict(adjusted_prices_df: pd.DataFrame) -> dict:
    fx_series_dict = dict(
        [
            (
                instrument_code,
                create_fx_series_given_adjusted_prices(
                    instrument_code, adjusted_prices
                ),
            )
            for instrument_code, adjusted_prices in adjusted_prices_df.items()
        ]
    )
    return fx_series_dict

# 
def create_fx_series_given_adjusted_prices(
    instrument_code: str, adjusted_prices: pd.Series
) -> pd.Series:
    # Everything is listed in USD, so we need to create a series of 1s
    # NEED TO REDO FOR FORIEGN CURRENCIES
    return pd.Series(1, index=adjusted_prices.index)  ## FX rate, 1 for USD / USD

fx_dict = dict(eurostx="eur")

def get_fx_prices(currency: str) -> pd.Series:
    # ! Deprecated pd_readcsv
    prices_as_df = pd_readcsv("%s_fx.csv" % currency)
    return prices_as_df.squeeze()

