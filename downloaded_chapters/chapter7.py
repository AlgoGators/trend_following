<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <meta name="robots" content="noindex" />
        <link rel="stylesheet" href="../style.css">
        <title>chapter7.py · AFTS-CODE · GitFront</title>
    </head>
    <body>
        <div class="container">
            <div class="location">
                <a href="..">AFTS-CODE</a> /
                <span>chapter7.py</span>
            </div>

            <div class="blob-view">
                <div class="header">
                    <div>chapter7.py</div>
                    <div class="last">
                        <a class="btn" href="../raw/chapter7.py">Raw</a>
                    </div>
                </div>
                <div class="content ">
                    <pre style="background-color:#fff"><span style="color:#444"></span><span style="color:#b83838">&#34;&#34;&#34;</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This is the provided example python code for Chapter seven of the book:</span><span style="color:#b83838">
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

<span style="color:#2838b0">from</span> <span style="color:#289870">scipy.stats</span> <span style="color:#2838b0">import</span> linregress
<span style="color:#2838b0">import</span> <span style="color:#289870">pandas</span> <span style="color:#2838b0">as</span> <span style="color:#289870">pd</span>

<span style="color:#2838b0">from</span> <span style="color:#289870">chapter1</span> <span style="color:#2838b0">import</span> calculate_stats<span style="color:#888">,</span> MONTH<span style="color:#888">,</span> BUSINESS_DAYS_IN_YEAR
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter3</span> <span style="color:#2838b0">import</span> standardDeviation
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter4</span> <span style="color:#2838b0">import</span> <span style="color:#888">(</span>
    get_data_dict<span style="color:#888">,</span>
    calculate_variable_standard_deviation_for_risk_targeting_from_dict<span style="color:#888">,</span>
    calculate_position_series_given_variable_risk_for_dict<span style="color:#888">,</span>
    create_fx_series_given_adjusted_prices_dict<span style="color:#888">,</span>
    aggregate_returns<span style="color:#888">,</span>
<span style="color:#888">)</span>
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter5</span> <span style="color:#2838b0">import</span> ewmac<span style="color:#888">,</span> calculate_perc_returns_for_dict_with_costs
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter6</span> <span style="color:#2838b0">import</span> long_only_returns


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_position_dict_with_trend_forecast_applied</span><span style="color:#888">(</span>
    adjusted_prices_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    average_position_contracts_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    std_dev_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    fast_span<span style="color:#888">:</span> <span style="color:#388038">int</span> <span style="color:#666">=</span> <span style="color:#444">64</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    list_of_instruments <span style="color:#666">=</span> <span style="color:#388038">list</span><span style="color:#888">(</span>adjusted_prices_dict<span style="color:#666">.</span>keys<span style="color:#888">(</span><span style="color:#888">)</span><span style="color:#888">)</span>
    position_dict_with_trend_filter <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                calculate_position_with_trend_forecast_applied<span style="color:#888">(</span>
                    adjusted_prices_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    average_position_contracts_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    stdev_ann_perc<span style="color:#666">=</span>std_dev_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    fast_span<span style="color:#666">=</span>fast_span<span style="color:#888">,</span>
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> list_of_instruments
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> position_dict_with_trend_filter


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_position_with_trend_forecast_applied</span><span style="color:#888">(</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    average_position<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    stdev_ann_perc<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span>
    fast_span<span style="color:#888">:</span> <span style="color:#388038">int</span> <span style="color:#666">=</span> <span style="color:#444">64</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    forecast <span style="color:#666">=</span> calculate_forecast_for_ewmac<span style="color:#888">(</span>
        adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">,</span>
        stdev_ann_perc<span style="color:#666">=</span>stdev_ann_perc<span style="color:#888">,</span>
        fast_span<span style="color:#666">=</span>fast_span<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> forecast <span style="color:#666">*</span> average_position <span style="color:#666">/</span> <span style="color:#444">10</span>


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_forecast_for_ewmac</span><span style="color:#888">(</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span> stdev_ann_perc<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span> fast_span<span style="color:#888">:</span> <span style="color:#388038">int</span> <span style="color:#666">=</span> <span style="color:#444">64</span>
<span style="color:#888">)</span><span style="color:#888">:</span>

    scaled_ewmac <span style="color:#666">=</span> calculate_scaled_forecast_for_ewmac<span style="color:#888">(</span>
        adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">,</span>
        stdev_ann_perc<span style="color:#666">=</span>stdev_ann_perc<span style="color:#888">,</span>
        fast_span<span style="color:#666">=</span>fast_span<span style="color:#888">,</span>
    <span style="color:#888">)</span>
    capped_ewmac <span style="color:#666">=</span> scaled_ewmac<span style="color:#666">.</span>clip<span style="color:#888">(</span><span style="color:#666">-</span><span style="color:#444">20</span><span style="color:#888">,</span> <span style="color:#444">20</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> capped_ewmac


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_scaled_forecast_for_ewmac</span><span style="color:#888">(</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    stdev_ann_perc<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span>
    fast_span<span style="color:#888">:</span> <span style="color:#388038">int</span> <span style="color:#666">=</span> <span style="color:#444">64</span><span style="color:#888">,</span>
<span style="color:#888">)</span><span style="color:#888">:</span>

    scalar_dict <span style="color:#666">=</span> <span style="color:#888">{</span><span style="color:#444">64</span><span style="color:#888">:</span> <span style="color:#444">1.91</span><span style="color:#888">,</span> <span style="color:#444">32</span><span style="color:#888">:</span> <span style="color:#444">2.79</span><span style="color:#888">,</span> <span style="color:#444">16</span><span style="color:#888">:</span> <span style="color:#444">4.1</span><span style="color:#888">,</span> <span style="color:#444">8</span><span style="color:#888">:</span> <span style="color:#444">5.95</span><span style="color:#888">,</span> <span style="color:#444">4</span><span style="color:#888">:</span> <span style="color:#444">8.53</span><span style="color:#888">,</span> <span style="color:#444">2</span><span style="color:#888">:</span> <span style="color:#444">12.1</span><span style="color:#888">}</span>
    risk_adjusted_ewmac <span style="color:#666">=</span> calculate_risk_adjusted_forecast_for_ewmac<span style="color:#888">(</span>
        adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">,</span>
        stdev_ann_perc<span style="color:#666">=</span>stdev_ann_perc<span style="color:#888">,</span>
        fast_span<span style="color:#666">=</span>fast_span<span style="color:#888">,</span>
    <span style="color:#888">)</span>
    forecast_scalar <span style="color:#666">=</span> scalar_dict<span style="color:#888">[</span>fast_span<span style="color:#888">]</span>
    scaled_ewmac <span style="color:#666">=</span> risk_adjusted_ewmac <span style="color:#666">*</span> forecast_scalar

    <span style="color:#2838b0">return</span> scaled_ewmac


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_risk_adjusted_forecast_for_ewmac</span><span style="color:#888">(</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    stdev_ann_perc<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span>
    fast_span<span style="color:#888">:</span> <span style="color:#388038">int</span> <span style="color:#666">=</span> <span style="color:#444">64</span><span style="color:#888">,</span>
<span style="color:#888">)</span><span style="color:#888">:</span>

    ewmac_values <span style="color:#666">=</span> ewmac<span style="color:#888">(</span>adjusted_price<span style="color:#888">,</span> fast_span<span style="color:#666">=</span>fast_span<span style="color:#888">,</span> slow_span<span style="color:#666">=</span>fast_span <span style="color:#666">*</span> <span style="color:#444">4</span><span style="color:#888">)</span>
    daily_price_vol <span style="color:#666">=</span> stdev_ann_perc<span style="color:#666">.</span>daily_risk_price_terms<span style="color:#888">(</span><span style="color:#888">)</span>

    risk_adjusted_ewmac <span style="color:#666">=</span> ewmac_values <span style="color:#666">/</span> daily_price_vol

    <span style="color:#2838b0">return</span> risk_adjusted_ewmac


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
        annualise_stdev<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>
        use_perc_returns<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>
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

    position_contracts_dict <span style="color:#666">=</span> calculate_position_dict_with_trend_forecast_applied<span style="color:#888">(</span>
        adjusted_prices_dict<span style="color:#666">=</span>adjusted_prices_dict<span style="color:#888">,</span>
        average_position_contracts_dict<span style="color:#666">=</span>average_position_contracts_dict<span style="color:#888">,</span>
        std_dev_dict<span style="color:#666">=</span>std_dev_dict<span style="color:#888">,</span>
        fast_span<span style="color:#666">=</span><span style="color:#444">64</span><span style="color:#888">,</span>
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

    long_only <span style="color:#666">=</span> long_only_returns<span style="color:#888">(</span>
        adjusted_prices_dict<span style="color:#666">=</span>adjusted_prices_dict<span style="color:#888">,</span>
        average_position_contracts_dict<span style="color:#666">=</span>average_position_contracts_dict<span style="color:#888">,</span>
        capital<span style="color:#666">=</span>capital<span style="color:#888">,</span>
        cost_per_contract_dict<span style="color:#666">=</span>cost_per_contract_dict<span style="color:#888">,</span>
        fx_series_dict<span style="color:#666">=</span>fx_series_dict<span style="color:#888">,</span>
        multipliers<span style="color:#666">=</span>multipliers<span style="color:#888">,</span>
        std_dev_dict<span style="color:#666">=</span>std_dev_dict<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    results <span style="color:#666">=</span> linregress<span style="color:#888">(</span>long_only<span style="color:#888">,</span> perc_return_agg<span style="color:#888">)</span>
    <span style="color:#2838b0">print</span><span style="color:#888">(</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">Beta </span><span style="color:#b83838;text-decoration:underline">%f</span><span style="color:#b83838">&#34;</span> <span style="color:#666">%</span> results<span style="color:#666">.</span>slope<span style="color:#888">)</span>
    daily_alpha <span style="color:#666">=</span> results<span style="color:#666">.</span>intercept
    <span style="color:#2838b0">print</span><span style="color:#888">(</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">Annual alpha </span><span style="color:#b83838;text-decoration:underline">%.2f</span><span style="color:#b83838;text-decoration:underline">%%</span><span style="color:#b83838">&#34;</span> <span style="color:#666">%</span> <span style="color:#888">(</span><span style="color:#444">100</span> <span style="color:#666">*</span> daily_alpha <span style="color:#666">*</span> BUSINESS_DAYS_IN_YEAR<span style="color:#888">)</span><span style="color:#888">)</span>
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
