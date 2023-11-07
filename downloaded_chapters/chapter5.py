<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <meta name="robots" content="noindex" />
        <link rel="stylesheet" href="../style.css">
        <title>chapter5.py · AFTS-CODE · GitFront</title>
    </head>
    <body>
        <div class="container">
            <div class="location">
                <a href="..">AFTS-CODE</a> /
                <span>chapter5.py</span>
            </div>

            <div class="blob-view">
                <div class="header">
                    <div>chapter5.py</div>
                    <div class="last">
                        <a class="btn" href="../raw/chapter5.py">Raw</a>
                    </div>
                </div>
                <div class="content ">
                    <pre style="background-color:#fff"><span style="color:#444"></span><span style="color:#b83838">&#34;&#34;&#34;</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This is the provided example python code for Chapter five of the book:</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838"> </span><span style="color:#b83838">&#34;</span><span style="color:#b83838">Advanced Futures Trading Strategies</span><span style="color:#b83838">&#34;</span><span style="color:#b83838">, by Robert Carver</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838"> https://www.systematicmoney.org/advanced-futures</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This code is copyright, Robert Carver 2022.</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">Shared under https://www.gnu.org/licenses/gpl-3.0.en.html</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">You may copy, modify, and share this code as long as this header is retained, and you disclose that it has been edited.</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This code comes with no warranty, is not guaranteed to be accurate, and the author is not responsible for any losses that may result from it’s use.</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">Results may not match the book exactly as different data may be used</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">Results may be different from the corresponding spreadsheet as methods may be slightly different</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">&#34;&#34;&#34;</span>

<span style="color:#888;font-style:italic">## Next two lines are optional depending on your IDE</span>
<span style="color:#2838b0">import</span> <span style="color:#289870">matplotlib</span>

matplotlib<span style="color:#666">.</span>use<span style="color:#888">(</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">TkAgg</span><span style="color:#b83838">&#34;</span><span style="color:#888">)</span>

<span style="color:#2838b0">from</span> <span style="color:#289870">copy</span> <span style="color:#2838b0">import</span> copy
<span style="color:#2838b0">import</span> <span style="color:#289870">pandas</span> <span style="color:#2838b0">as</span> <span style="color:#289870">pd</span>

<span style="color:#2838b0">from</span> <span style="color:#289870">chapter1</span> <span style="color:#2838b0">import</span> calculate_stats<span style="color:#888">,</span> BUSINESS_DAYS_IN_YEAR
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter3</span> <span style="color:#2838b0">import</span> standardDeviation
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter4</span> <span style="color:#2838b0">import</span> <span style="color:#888">(</span>
    get_data_dict<span style="color:#888">,</span>
    calculate_variable_standard_deviation_for_risk_targeting_from_dict<span style="color:#888">,</span>
    calculate_position_series_given_variable_risk_for_dict<span style="color:#888">,</span>
    create_fx_series_given_adjusted_prices_dict<span style="color:#888">,</span>
    aggregate_returns<span style="color:#888">,</span>
<span style="color:#888">)</span>


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_position_dict_with_trend_filter_applied</span><span style="color:#888">(</span>
    adjusted_prices_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    average_position_contracts_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    list_of_instruments <span style="color:#666">=</span> <span style="color:#388038">list</span><span style="color:#888">(</span>adjusted_prices_dict<span style="color:#666">.</span>keys<span style="color:#888">(</span><span style="color:#888">)</span><span style="color:#888">)</span>
    position_dict_with_trend_filter <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                calculate_position_with_trend_filter_applied<span style="color:#888">(</span>
                    adjusted_prices_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    average_position_contracts_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> list_of_instruments
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> position_dict_with_trend_filter


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_position_with_trend_filter_applied</span><span style="color:#888">(</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span> average_position<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    filtered_position <span style="color:#666">=</span> copy<span style="color:#888">(</span>average_position<span style="color:#888">)</span>
    ewmac_values <span style="color:#666">=</span> ewmac<span style="color:#888">(</span>adjusted_price<span style="color:#888">)</span>
    bearish <span style="color:#666">=</span> ewmac_values <span style="color:#666">&lt;</span> <span style="color:#444">0</span>
    filtered_position<span style="color:#888">[</span>bearish<span style="color:#888">]</span> <span style="color:#666">=</span> <span style="color:#444">0</span>

    <span style="color:#2838b0">return</span> filtered_position


<span style="color:#2838b0">def</span> <span style="color:#785840">ewmac</span><span style="color:#888">(</span>adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span> fast_span<span style="color:#666">=</span><span style="color:#444">16</span><span style="color:#888">,</span> slow_span<span style="color:#666">=</span><span style="color:#444">64</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    slow_ewma <span style="color:#666">=</span> adjusted_price<span style="color:#666">.</span>ewm<span style="color:#888">(</span>span<span style="color:#666">=</span>slow_span<span style="color:#888">,</span> min_periods<span style="color:#666">=</span><span style="color:#444">2</span><span style="color:#888">)</span><span style="color:#666">.</span>mean<span style="color:#888">(</span><span style="color:#888">)</span>
    fast_ewma <span style="color:#666">=</span> adjusted_price<span style="color:#666">.</span>ewm<span style="color:#888">(</span>span<span style="color:#666">=</span>fast_span<span style="color:#888">,</span> min_periods<span style="color:#666">=</span><span style="color:#444">2</span><span style="color:#888">)</span><span style="color:#666">.</span>mean<span style="color:#888">(</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> fast_ewma <span style="color:#666">-</span> slow_ewma


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_perc_returns_for_dict_with_costs</span><span style="color:#888">(</span>
    position_contracts_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    adjusted_prices<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    multipliers<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    fx_series<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    capital<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    cost_per_contract_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    std_dev_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    perc_returns_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                calculate_perc_returns_with_costs<span style="color:#888">(</span>
                    position_contracts_held<span style="color:#666">=</span>position_contracts_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    adjusted_price<span style="color:#666">=</span>adjusted_prices<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    multiplier<span style="color:#666">=</span>multipliers<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    fx_series<span style="color:#666">=</span>fx_series<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    capital_required<span style="color:#666">=</span>capital<span style="color:#888">,</span>
                    cost_per_contract<span style="color:#666">=</span>cost_per_contract_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    stdev_series<span style="color:#666">=</span>std_dev_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> position_contracts_dict<span style="color:#666">.</span>keys<span style="color:#888">(</span><span style="color:#888">)</span>
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> perc_returns_dict


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_perc_returns_with_costs</span><span style="color:#888">(</span>
    position_contracts_held<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    fx_series<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    stdev_series<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span>
    multiplier<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    capital_required<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    cost_per_contract<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    precost_return_price_points <span style="color:#666">=</span> <span style="color:#888">(</span>
        adjusted_price <span style="color:#666">-</span> adjusted_price<span style="color:#666">.</span>shift<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">)</span>
    <span style="color:#888">)</span> <span style="color:#666">*</span> position_contracts_held<span style="color:#666">.</span>shift<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">)</span>

    precost_return_instrument_currency <span style="color:#666">=</span> precost_return_price_points <span style="color:#666">*</span> multiplier
    historic_costs <span style="color:#666">=</span> calculate_costs_deflated_for_vol<span style="color:#888">(</span>
        stddev_series<span style="color:#666">=</span>stdev_series<span style="color:#888">,</span>
        cost_per_contract<span style="color:#666">=</span>cost_per_contract<span style="color:#888">,</span>
        position_contracts_held<span style="color:#666">=</span>position_contracts_held<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    historic_costs_aligned <span style="color:#666">=</span> historic_costs<span style="color:#666">.</span>reindex<span style="color:#888">(</span>
        precost_return_instrument_currency<span style="color:#666">.</span>index<span style="color:#888">,</span> method<span style="color:#666">=</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">ffill</span><span style="color:#b83838">&#34;</span>
    <span style="color:#888">)</span>
    return_instrument_currency <span style="color:#666">=</span> <span style="color:#888">(</span>
        precost_return_instrument_currency <span style="color:#666">-</span> historic_costs_aligned
    <span style="color:#888">)</span>

    fx_series_aligned <span style="color:#666">=</span> fx_series<span style="color:#666">.</span>reindex<span style="color:#888">(</span>
        return_instrument_currency<span style="color:#666">.</span>index<span style="color:#888">,</span> method<span style="color:#666">=</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">ffill</span><span style="color:#b83838">&#34;</span>
    <span style="color:#888">)</span>
    return_base_currency <span style="color:#666">=</span> return_instrument_currency <span style="color:#666">*</span> fx_series_aligned

    perc_return <span style="color:#666">=</span> return_base_currency <span style="color:#666">/</span> capital_required

    <span style="color:#2838b0">return</span> perc_return


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_costs_deflated_for_vol</span><span style="color:#888">(</span>
    stddev_series<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span>
    cost_per_contract<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    position_contracts_held<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    round_position_contracts_held <span style="color:#666">=</span> position_contracts_held<span style="color:#666">.</span>round<span style="color:#888">(</span><span style="color:#888">)</span>
    position_change <span style="color:#666">=</span> <span style="color:#888">(</span>
        round_position_contracts_held <span style="color:#666">-</span> round_position_contracts_held<span style="color:#666">.</span>shift<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">)</span>
    <span style="color:#888">)</span>
    abs_trades <span style="color:#666">=</span> position_change<span style="color:#666">.</span>abs<span style="color:#888">(</span><span style="color:#888">)</span>

    historic_cost_per_contract <span style="color:#666">=</span> calculate_deflated_costs<span style="color:#888">(</span>
        stddev_series<span style="color:#666">=</span>stddev_series<span style="color:#888">,</span> cost_per_contract<span style="color:#666">=</span>cost_per_contract
    <span style="color:#888">)</span>

    historic_cost_per_contract_aligned <span style="color:#666">=</span> historic_cost_per_contract<span style="color:#666">.</span>reindex<span style="color:#888">(</span>
        abs_trades<span style="color:#666">.</span>index<span style="color:#888">,</span> method<span style="color:#666">=</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">ffill</span><span style="color:#b83838">&#34;</span>
    <span style="color:#888">)</span>

    historic_costs <span style="color:#666">=</span> abs_trades <span style="color:#666">*</span> historic_cost_per_contract_aligned

    <span style="color:#2838b0">return</span> historic_costs


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_deflated_costs</span><span style="color:#888">(</span>
    stddev_series<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span> cost_per_contract<span style="color:#888">:</span> <span style="color:#388038">float</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    stdev_daily_price <span style="color:#666">=</span> stddev_series<span style="color:#666">.</span>daily_risk_price_terms<span style="color:#888">(</span><span style="color:#888">)</span>

    final_stdev <span style="color:#666">=</span> stdev_daily_price<span style="color:#888">[</span><span style="color:#666">-</span><span style="color:#444">1</span><span style="color:#888">]</span>
    cost_deflator <span style="color:#666">=</span> stdev_daily_price <span style="color:#666">/</span> final_stdev
    historic_cost_per_contract <span style="color:#666">=</span> cost_per_contract <span style="color:#666">*</span> cost_deflator

    <span style="color:#2838b0">return</span> historic_cost_per_contract


<span style="color:#2838b0">if</span> <span style="color:#b85820">__name__</span> <span style="color:#666">==</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">__main__</span><span style="color:#b83838">&#34;</span><span style="color:#888">:</span>
    <span style="color:#888;font-style:italic">## Get the files from:</span>
    <span style="color:#888;font-style:italic"># https://gitfront.io/r/user-4000052/iTvUZwEUN2Ta/AFTS-CODE/blob/sp500.csv</span>
    <span style="color:#888;font-style:italic"># and https://gitfront.io/r/user-4000052/iTvUZwEUN2Ta/AFTS-CODE/blob/US10.csv</span>
    adjusted_prices_dict<span style="color:#888">,</span> current_prices_dict <span style="color:#666">=</span> get_data_dict<span style="color:#888">(</span><span style="color:#888">)</span>

    multipliers <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>sp500<span style="color:#666">=</span><span style="color:#444">5</span><span style="color:#888">,</span> us10<span style="color:#666">=</span><span style="color:#444">1000</span><span style="color:#888">)</span>
    risk_target_tau <span style="color:#666">=</span> <span style="color:#444">0.2</span>
    fx_series_dict <span style="color:#666">=</span> create_fx_series_given_adjusted_prices_dict<span style="color:#888">(</span>adjusted_prices_dict<span style="color:#888">)</span>

    capital <span style="color:#666">=</span> <span style="color:#444">1000000</span>
    idm <span style="color:#666">=</span> <span style="color:#444">1.5</span>
    instrument_weights <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>sp500<span style="color:#666">=</span><span style="color:#444">0.5</span><span style="color:#888">,</span> us10<span style="color:#666">=</span><span style="color:#444">0.5</span><span style="color:#888">)</span>
    cost_per_contract_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>sp500<span style="color:#666">=</span><span style="color:#444">0.875</span><span style="color:#888">,</span> us10<span style="color:#666">=</span><span style="color:#444">5</span><span style="color:#888">)</span>

    std_dev_dict <span style="color:#666">=</span> calculate_variable_standard_deviation_for_risk_targeting_from_dict<span style="color:#888">(</span>
        adjusted_prices<span style="color:#666">=</span>adjusted_prices_dict<span style="color:#888">,</span>
        current_prices<span style="color:#666">=</span>current_prices_dict<span style="color:#888">,</span>
        use_perc_returns<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>
        annualise_stdev<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>
    <span style="color:#888">)</span>

    average_position_contracts_dict <span style="color:#666">=</span> <span style="color:#888">(</span>
        calculate_position_series_given_variable_risk_for_dict<span style="color:#888">(</span>
            capital<span style="color:#666">=</span>capital<span style="color:#888">,</span>
            risk_target_tau<span style="color:#666">=</span>risk_target_tau<span style="color:#888">,</span>
            idm<span style="color:#666">=</span>idm<span style="color:#888">,</span>
            weights<span style="color:#666">=</span>instrument_weights<span style="color:#888">,</span>
            std_dev_dict<span style="color:#666">=</span>std_dev_dict<span style="color:#888">,</span>
            fx_series_dict<span style="color:#666">=</span>fx_series_dict<span style="color:#888">,</span>
            multipliers<span style="color:#666">=</span>multipliers<span style="color:#888">,</span>
        <span style="color:#888">)</span>
    <span style="color:#888">)</span>

    position_contracts_dict <span style="color:#666">=</span> calculate_position_dict_with_trend_filter_applied<span style="color:#888">(</span>
        adjusted_prices_dict<span style="color:#666">=</span>adjusted_prices_dict<span style="color:#888">,</span>
        average_position_contracts_dict<span style="color:#666">=</span>average_position_contracts_dict<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#888;font-style:italic">## note doesn&#39;t include roll costs</span>
    perc_return_dict <span style="color:#666">=</span> calculate_perc_returns_for_dict_with_costs<span style="color:#888">(</span>
        position_contracts_dict<span style="color:#666">=</span>position_contracts_dict<span style="color:#888">,</span>
        fx_series<span style="color:#666">=</span>fx_series_dict<span style="color:#888">,</span>
        multipliers<span style="color:#666">=</span>multipliers<span style="color:#888">,</span>
        capital<span style="color:#666">=</span>capital<span style="color:#888">,</span>
        adjusted_prices<span style="color:#666">=</span>adjusted_prices_dict<span style="color:#888">,</span>
        cost_per_contract_dict<span style="color:#666">=</span>cost_per_contract_dict<span style="color:#888">,</span>
        std_dev_dict<span style="color:#666">=</span>std_dev_dict<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return_dict<span style="color:#888">[</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">sp500</span><span style="color:#b83838">&#34;</span><span style="color:#888">]</span><span style="color:#888">)</span><span style="color:#888">)</span>

    perc_return_agg <span style="color:#666">=</span> aggregate_returns<span style="color:#888">(</span>perc_return_dict<span style="color:#888">)</span>
    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return_agg<span style="color:#888">)</span><span style="color:#888">)</span>
</pre>
                </div>
            </div>

            <div class="space"></div>
            <div class="footer">
                Powered by <a href="https://gitfront.io">GitFront</a>
            </div>
        </div>
    </body>
</html>
