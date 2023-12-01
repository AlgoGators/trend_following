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
    create_fx_series_given_adjusted_prices_dict,
    calculate_variable_standard_deviation_for_risk_targeting_from_dict,
    calculate_position_series_given_variable_risk_for_dict,
)

from chapter5 import calculate_perc_returns_for_dict_with_costs
from chapter7 import calculate_forecast_for_ewmac
from chapter8 import apply_buffering_to_position_dict
from chapter9 import (
    calculate_position_dict_with_multiple_trend_forecast_applied,
    calculate_position_with_multiple_trend_forecast_applied,

)
# NEED TO READ DATA FIRST

# grab fisrt string from arg
if len(sys.argv) < 2:
    print("Usage: python3 multitrend.py <filename>")
else:
    filename = sys.argv[1]
    data = pd_readcsv(filename)
    data = data.dropna()

def get_data_dict(instr_list: list):

    all_data = dict(
        [
            (instrument_code, pd_readcsv("%s.csv" % instrument_code, date_format="%m/%d/%Y", date_index_name='Date'))
            for instrument_code in instr_list
        ]
    )

    adjusted_prices = dict(
        [
            (instrument_code, data_for_instrument.Close)
            for instrument_code, data_for_instrument in all_data.items()
        ]
    )

    current_prices = dict(
        [
            (instrument_code, data_for_instrument.Unadj_Close)
            for instrument_code, data_for_instrument in all_data.items()
        ]
    )

    return adjusted_prices, current_prices

def trend_forecast(capital: int, risk_target_tau: float, multipliers: dict, instr_list: list, fast_spans: list) -> tuple[dict, dict]:

    adjusted_prices_dict, current_prices_dict = get_data_dict(instr_list)

    fx_series_dict = create_fx_series_given_adjusted_prices_dict(adjusted_prices_dict)


    idm = 1.5
    instrument_weights = dict(ES=0.5, us10=0.5)
    cost_per_contract_dict = dict(ES=0.875, us10=5)

    std_dev_dict = calculate_variable_standard_deviation_for_risk_targeting_from_dict(
        adjusted_prices=adjusted_prices_dict, current_prices=current_prices_dict
    )

    average_position_contracts_dict = (
        calculate_position_series_given_variable_risk_for_dict(
            capital=capital,
            risk_target_tau=risk_target_tau,
            idm=idm,
            weights=instrument_weights,
            std_dev_dict=std_dev_dict,
            fx_series_dict=fx_series_dict,
            multipliers=multipliers,
        )
    )

    ## We use three arbitrary slow spans here for both instruments
    ## In reality we would need to check costs and turnover
    position_contracts_dict = (
        calculate_position_dict_with_multiple_trend_forecast_applied(
            adjusted_prices_dict=adjusted_prices_dict,
            average_position_contracts_dict=average_position_contracts_dict,
            std_dev_dict=std_dev_dict,
            fast_spans=fast_spans,
        )
    )

    buffered_position_dict = apply_buffering_to_position_dict(
        position_contracts_dict=position_contracts_dict,
        average_position_contracts_dict=average_position_contracts_dict,
    )

    perc_return_dict = calculate_perc_returns_for_dict_with_costs(
        position_contracts_dict=buffered_position_dict,
        fx_series=fx_series_dict,
        multipliers=multipliers,
        capital=capital,
        adjusted_prices=adjusted_prices_dict,
        cost_per_contract_dict=cost_per_contract_dict,
        std_dev_dict=std_dev_dict,
    )

    return perc_return_dict, buffered_position_dict

INSTRUMENT_LIST = ['ES']
multipliers = dict(ES=5)
risk_target_tau = 0.2
capital = 100_000


perc, fc = trend_forecast(capital, risk_target_tau, multipliers, INSTRUMENT_LIST, [16, 32, 64])

df = pd.DataFrame.from_dict(fc)

print(calculate_stats(perc['ES']))

df.to_csv("out.csv")
