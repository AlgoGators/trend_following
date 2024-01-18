import sql_functions as sql

from fx_functions import create_fx_series_given_adjusted_prices_dict

from risk_functions import calculate_variable_standard_deviation_for_risk_targeting_from_dict
from risk_functions import calculate_position_series_given_variable_risk_for_dict

from trend_functions import calculate_position_dict_with_multiple_trend_forecast_applied, apply_buffering_to_position_dict, calculate_perc_returns_for_dict_with_costs

import pandas as pd
from getMultiplierDict import getMultiplierDict
# NEED TO READ DATA FIRST

# def get_data_dict(instr_list: list):
#
#     all_data = dict(
#         [
#             (instrument_code, pd_readcsv(f"data/_{instrument_code}_Data.csv"  , date_format="%m/%d/%Y", date_index_name='Date'))
#             for instrument_code in instr_list
#         ]
#     )
#
#     adjusted_prices = dict(
#         [
#             (instrument_code, data_for_instrument.Close)
#             for instrument_code, data_for_instrument in all_data.items()
#         ]
#     )
#
#     current_prices = dict(
#         [
#             (instrument_code, data_for_instrument.Unadj_Close)
#             for instrument_code, data_for_instrument in all_data.items()
#         ]
#     )
#
#     return adjusted_prices, current_prices

def calc_idm(instrument_list: list) -> float:

    # if the lenght of the instrument list lands in a certain bracket, return a certain value
    # this is not a true idm, but a rough approx.
    # TRUE IDM = 1 / sqrt(w.rho.wT)
    n = len(instrument_list)

    if n == 1:
        return 1.0
    elif n == 2:
        return 1.20
    elif n == 3:
        return 1.48
    elif n == 4:
        return 1.56
    elif n == 5:
        return 1.70
    elif n == 6:
        return 1.90
    elif n == 7:
        return 2.10
    elif n >= 8 and n <= 14:
        return 2.20
    elif n >= 15 and n <= 24:
        return 2.30
    elif n >= 25 and n <= 30:
        return 2.40
    elif n > 30:
        return 2.50

    # if we reached here, something went wrong
    raise ValueError("Instrument Diversity Multiplier not found")
          

def trend_forecast(instr_list: list, weights: dict, capital: int, risk_target_tau: float, multipliers: dict, fast_spans: list) -> list:

    adjusted_prices_dict, current_prices_dict = sql.get_data(instr_list)

    fx_series_dict = create_fx_series_given_adjusted_prices_dict(adjusted_prices_dict)


    idm = calc_idm(instr_list)

    instrument_weights = weights

    # NEED TO FIX!!! HARDCODED COSTS
    # PIN ALL COSTS to 0.875 for all instruments in list
    for instrument in instr_list:
        cost_per_contract_dict = dict(instrument=0.875)

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

    # perc_return_dict = calculate_perc_returns_for_dict_with_costs(
    #     position_contracts_dict=buffered_position_dict,
    #     fx_series=fx_series_dict,
    #     multipliers=multipliers,
    #     capital=capital,
    #     adjusted_prices=adjusted_prices_dict,
    #     cost_per_contract_dict=cost_per_contract_dict,
    #     std_dev_dict=std_dev_dict,
    # )

    return [buffered_position_dict, position_contracts_dict]

# List of all instruments in the portfolio
def main():

    instruments = ['CL', 'ES', 'GC', 'HG', 'HO', 'NG', 'RB', 'SI']

    even_weights = 1 / len(instruments)

    
    # dict of equal weight for each instrument in the list
    weights = {}
    for code in instruments:
        weights[code] = even_weights

    multipliers = getMultiplierDict()
    risk_target_tau = 0.2

    capital = 100000

    buffered_pos, pos = trend_forecast(instruments, weights, capital, risk_target_tau, multipliers, [16, 32, 64])

    print(pos['ES'].tail())

if __name__ == '__main__':
    main()