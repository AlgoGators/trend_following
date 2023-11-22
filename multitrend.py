import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
from scipy.stats import norm
import sys

from chapter1 import (
    calculate_stats,
    pd_readcsv,
)
from chapter3 import standardDeviation
from chapter4 import (
    get_data_dict,
    create_fx_series_given_adjusted_prices_dict,
    calculate_variable_standard_deviation_for_risk_targeting_from_dict,
    calculate_position_series_given_variable_risk_for_dict,
)

from chapter5 import calculate_perc_returns_for_dict_with_costs
from chapter7 import calculate_forecast_for_ewmac
from chapter8 import apply_buffering_to_position_dict

# NEED TO READ DATA FIRST

# grab fisrt string from arg
filename = sys.argv[1]
data = pd_readcsv(filename)
data = data.dropna()

def calculate_position_dict_with_multiple_trend_forecast_applied(
    adjusted_prices_dict: dict,
    average_position_contracts_dict: dict,
    std_dev_dict: dict,
    fast_spans: list,
) -> dict:

    list_of_instruments = list(adjusted_prices_dict.keys())
    position_dict_with_trend_filter = dict(
        [
            (
                instrument_code,
                calculate_position_with_multiple_trend_forecast_applied(
                    adjusted_prices_dict[instrument_code],
                    average_position_contracts_dict[instrument_code],
                    stdev_ann_perc=std_dev_dict[instrument_code],
                    fast_spans=fast_spans,
                ),
            )
            for instrument_code in list_of_instruments
        ]
    )

    return position_dict_with_trend_filter


def calculate_position_with_multiple_trend_forecast_applied(
    adjusted_price: pd.Series,
    average_position: pd.Series,
    stdev_ann_perc: standardDeviation,
    fast_spans: list,
) -> pd.Series:

    forecast = calculate_combined_ewmac_forecast(
        adjusted_price=adjusted_price,
        stdev_ann_perc=stdev_ann_perc,
        fast_spans=fast_spans,
    )

    return forecast * average_position / 10


def calculate_combined_ewmac_forecast(
    adjusted_price: pd.Series,
    stdev_ann_perc: standardDeviation,
    fast_spans: list,
) -> pd.Series:

    all_forecasts_as_list = [
        calculate_forecast_for_ewmac(
            adjusted_price=adjusted_price,
            stdev_ann_perc=stdev_ann_perc,
            fast_span=fast_span,
        )
        for fast_span in fast_spans
    ]

    ### NOTE: This assumes we are equally weighted across spans
    ### eg all forecast weights the same, equally weighted
    all_forecasts_as_df = pd.concat(all_forecasts_as_list, axis=1)
    average_forecast = all_forecasts_as_df.mean(axis=1)

    ## apply an FDM
    rule_count = len(fast_spans)
    FDM_DICT = {1: 1.0, 2: 1.03, 3: 1.08, 4: 1.13, 5: 1.19, 6: 1.26}
    fdm = FDM_DICT[rule_count]

    scaled_forecast = average_forecast * fdm
    capped_forecast = scaled_forecast.clip(-20, 20)

    return capped_forecast