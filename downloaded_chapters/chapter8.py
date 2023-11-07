<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <meta name="robots" content="noindex" />
        <link rel="stylesheet" href="../style.css">
        <title>chapter8.py · AFTS-CODE · GitFront</title>
    </head>
    <body>
        <div class="container">
            <div class="location">
                <a href="..">AFTS-CODE</a> /
                <span>chapter8.py</span>
            </div>

            <div class="blob-view">
                <div class="header">
                    <div>chapter8.py</div>
                    <div class="last">
                        <a class="btn" href="../raw/chapter8.py">Raw</a>
                    </div>
                </div>
                <div class="content ">
                    <pre style="background-color:#fff"><span style="color:#444"></span><span style="color:#b83838">&#34;&#34;&#34;</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This is the provided example python code for Chapter eight of the book:</span><span style="color:#b83838">
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
<span style="color:#2838b0">import</span> <span style="color:#289870">pandas</span> <span style="color:#2838b0">as</span> <span style="color:#289870">pd</span>
<span style="color:#2838b0">import</span> <span style="color:#289870">numpy</span> <span style="color:#2838b0">as</span> <span style="color:#289870">np</span>

<span style="color:#2838b0">from</span> <span style="color:#289870">chapter1</span> <span style="color:#2838b0">import</span> calculate_stats
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter4</span> <span style="color:#2838b0">import</span> <span style="color:#888">(</span>
    get_data_dict<span style="color:#888">,</span>
    create_fx_series_given_adjusted_prices_dict<span style="color:#888">,</span>
    calculate_variable_standard_deviation_for_risk_targeting_from_dict<span style="color:#888">,</span>
    calculate_position_series_given_variable_risk_for_dict<span style="color:#888">,</span>
<span style="color:#888">)</span>

<span style="color:#2838b0">from</span> <span style="color:#289870">chapter5</span> <span style="color:#2838b0">import</span> calculate_perc_returns_for_dict_with_costs
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter7</span> <span style="color:#2838b0">import</span> calculate_position_dict_with_trend_forecast_applied


<span style="color:#2838b0">def</span> <span style="color:#785840">apply_buffering_to_position_dict</span><span style="color:#888">(</span>
    position_contracts_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span> average_position_contracts_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    instrument_list <span style="color:#666">=</span> <span style="color:#388038">list</span><span style="color:#888">(</span>position_contracts_dict<span style="color:#666">.</span>keys<span style="color:#888">(</span><span style="color:#888">)</span><span style="color:#888">)</span>
    buffered_position_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                apply_buffering_to_positions<span style="color:#888">(</span>
                    position_contracts<span style="color:#666">=</span>position_contracts_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    average_position_contracts<span style="color:#666">=</span>average_position_contracts_dict<span style="color:#888">[</span>
                        instrument_code
                    <span style="color:#888">]</span><span style="color:#888">,</span>
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> instrument_list
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> buffered_position_dict


<span style="color:#2838b0">def</span> <span style="color:#785840">apply_buffering_to_positions</span><span style="color:#888">(</span>
    position_contracts<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    average_position_contracts<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    buffer_size<span style="color:#888">:</span> <span style="color:#388038">float</span> <span style="color:#666">=</span> <span style="color:#444">0.10</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    <span style="color:#388038">buffer</span> <span style="color:#666">=</span> average_position_contracts<span style="color:#666">.</span>abs<span style="color:#888">(</span><span style="color:#888">)</span> <span style="color:#666">*</span> buffer_size
    upper_buffer <span style="color:#666">=</span> position_contracts <span style="color:#666">+</span> <span style="color:#388038">buffer</span>
    lower_buffer <span style="color:#666">=</span> position_contracts <span style="color:#666">-</span> <span style="color:#388038">buffer</span>

    buffered_position <span style="color:#666">=</span> apply_buffer<span style="color:#888">(</span>
        optimal_position<span style="color:#666">=</span>position_contracts<span style="color:#888">,</span>
        upper_buffer<span style="color:#666">=</span>upper_buffer<span style="color:#888">,</span>
        lower_buffer<span style="color:#666">=</span>lower_buffer<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> buffered_position


<span style="color:#2838b0">def</span> <span style="color:#785840">apply_buffer</span><span style="color:#888">(</span>
    optimal_position<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span> upper_buffer<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span> lower_buffer<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    upper_buffer <span style="color:#666">=</span> upper_buffer<span style="color:#666">.</span>ffill<span style="color:#888">(</span><span style="color:#888">)</span><span style="color:#666">.</span>round<span style="color:#888">(</span><span style="color:#888">)</span>
    lower_buffer <span style="color:#666">=</span> lower_buffer<span style="color:#666">.</span>ffill<span style="color:#888">(</span><span style="color:#888">)</span><span style="color:#666">.</span>round<span style="color:#888">(</span><span style="color:#888">)</span>
    use_optimal_position <span style="color:#666">=</span> optimal_position<span style="color:#666">.</span>ffill<span style="color:#888">(</span><span style="color:#888">)</span>

    current_position <span style="color:#666">=</span> use_optimal_position<span style="color:#888">[</span><span style="color:#444">0</span><span style="color:#888">]</span>
    <span style="color:#2838b0">if</span> np<span style="color:#666">.</span>isnan<span style="color:#888">(</span>current_position<span style="color:#888">)</span><span style="color:#888">:</span>
        current_position <span style="color:#666">=</span> <span style="color:#444">0.0</span>

    buffered_position_list <span style="color:#666">=</span> <span style="color:#888">[</span>current_position<span style="color:#888">]</span>

    <span style="color:#2838b0">for</span> idx <span style="color:#a848a8">in</span> <span style="color:#388038">range</span><span style="color:#888">(</span><span style="color:#388038">len</span><span style="color:#888">(</span>optimal_position<span style="color:#666">.</span>index<span style="color:#888">)</span><span style="color:#888">)</span><span style="color:#888">[</span><span style="color:#444">1</span><span style="color:#888">:</span><span style="color:#888">]</span><span style="color:#888">:</span>
        current_position <span style="color:#666">=</span> apply_buffer_single_period<span style="color:#888">(</span>
            last_position<span style="color:#666">=</span>current_position<span style="color:#888">,</span>
            top_pos<span style="color:#666">=</span>upper_buffer<span style="color:#888">[</span>idx<span style="color:#888">]</span><span style="color:#888">,</span>
            bot_pos<span style="color:#666">=</span>lower_buffer<span style="color:#888">[</span>idx<span style="color:#888">]</span><span style="color:#888">,</span>
        <span style="color:#888">)</span>

        buffered_position_list<span style="color:#666">.</span>append<span style="color:#888">(</span>current_position<span style="color:#888">)</span>

    buffered_position <span style="color:#666">=</span> pd<span style="color:#666">.</span>Series<span style="color:#888">(</span>buffered_position_list<span style="color:#888">,</span> index<span style="color:#666">=</span>optimal_position<span style="color:#666">.</span>index<span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> buffered_position


<span style="color:#2838b0">def</span> <span style="color:#785840">apply_buffer_single_period</span><span style="color:#888">(</span>last_position<span style="color:#888">:</span> <span style="color:#388038">int</span><span style="color:#888">,</span> top_pos<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span> bot_pos<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">)</span><span style="color:#888">:</span>

    <span style="color:#2838b0">if</span> last_position <span style="color:#666">&gt;</span> top_pos<span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> top_pos
    <span style="color:#2838b0">elif</span> last_position <span style="color:#666">&lt;</span> bot_pos<span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> bot_pos
    <span style="color:#2838b0">else</span><span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> last_position


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
        adjusted_prices<span style="color:#666">=</span>adjusted_prices_dict<span style="color:#888">,</span> current_prices<span style="color:#666">=</span>current_prices_dict
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
        fast_span<span style="color:#666">=</span><span style="color:#444">16</span><span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#888;font-style:italic">## buffering</span>
    buffered_position_dict <span style="color:#666">=</span> apply_buffering_to_position_dict<span style="color:#888">(</span>
        position_contracts_dict<span style="color:#666">=</span>position_contracts_dict<span style="color:#888">,</span>
        average_position_contracts_dict<span style="color:#666">=</span>average_position_contracts_dict<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#888;font-style:italic">## note doesn&#39;t include roll costs</span>
    perc_return_dict <span style="color:#666">=</span> calculate_perc_returns_for_dict_with_costs<span style="color:#888">(</span>
        position_contracts_dict<span style="color:#666">=</span>buffered_position_dict<span style="color:#888">,</span>
        fx_series<span style="color:#666">=</span>fx_series_dict<span style="color:#888">,</span>
        multipliers<span style="color:#666">=</span>multipliers<span style="color:#888">,</span>
        capital<span style="color:#666">=</span>capital<span style="color:#888">,</span>
        adjusted_prices<span style="color:#666">=</span>adjusted_prices_dict<span style="color:#888">,</span>
        cost_per_contract_dict<span style="color:#666">=</span>cost_per_contract_dict<span style="color:#888">,</span>
        std_dev_dict<span style="color:#666">=</span>std_dev_dict<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return_dict<span style="color:#888">[</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">us10</span><span style="color:#b83838">&#34;</span><span style="color:#888">]</span><span style="color:#888">)</span><span style="color:#888">)</span>
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
