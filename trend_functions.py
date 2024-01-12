import pandas as pd
from risk_functions import standardDeviation

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

def calculate_forecast_for_ewmac(
    adjusted_price: pd.Series, stdev_ann_perc: standardDeviation, fast_span: int = 64
):

    scaled_ewmac = calculate_scaled_forecast_for_ewmac(
        adjusted_price=adjusted_price,
        stdev_ann_perc=stdev_ann_perc,
        fast_span=fast_span,
    )
    capped_ewmac = scaled_ewmac.clip(-20, 20)

    return capped_ewmac

def calculate_scaled_forecast_for_ewmac(
    adjusted_price: pd.Series,
    stdev_ann_perc: standardDeviation,
    fast_span: int = 64,
):

    scalar_dict = {64: 1.91, 32: 2.79, 16: 4.1, 8: 5.95, 4: 8.53, 2: 12.1}
    risk_adjusted_ewmac = calculate_risk_adjusted_forecast_for_ewmac(
        adjusted_price=adjusted_price,
        stdev_ann_perc=stdev_ann_perc,
        fast_span=fast_span,
    )
    forecast_scalar = scalar_dict[fast_span]
    scaled_ewmac = risk_adjusted_ewmac * forecast_scalar

    return scaled_ewmac

def calculate_risk_adjusted_forecast_for_ewmac(
    adjusted_price: pd.Series,
    stdev_ann_perc: standardDeviation,
    fast_span: int = 64,
):

    ewmac_values = ewmac(adjusted_price, fast_span=fast_span, slow_span=fast_span * 4)
    daily_price_vol = stdev_ann_perc.daily_risk_price_terms()

    risk_adjusted_ewmac = ewmac_values / daily_price_vol

    return risk_adjusted_ewmac

def ewmac(adjusted_price: pd.Series, fast_span=16, slow_span=64) -> pd.Series:

    slow_ewma = adjusted_price.ewm(span=slow_span, min_periods=2).mean()
    fast_ewma = adjusted_price.ewm(span=fast_span, min_periods=2).mean()

    return fast_ewma - slow_ewma
