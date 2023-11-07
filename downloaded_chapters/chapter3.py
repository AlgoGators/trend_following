<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <meta name="robots" content="noindex" />
        <link rel="stylesheet" href="../style.css">
        <title>chapter3.py · AFTS-CODE · GitFront</title>
    </head>
    <body>
        <div class="container">
            <div class="location">
                <a href="..">AFTS-CODE</a> /
                <span>chapter3.py</span>
            </div>

            <div class="blob-view">
                <div class="header">
                    <div>chapter3.py</div>
                    <div class="last">
                        <a class="btn" href="../raw/chapter3.py">Raw</a>
                    </div>
                </div>
                <div class="content ">
                    <pre style="background-color:#fff"><span style="color:#444"></span><span style="color:#b83838">&#34;&#34;&#34;</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This is the provided example python code for Chapter three of the book:</span><span style="color:#b83838">
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

<span style="color:#2838b0">from</span> <span style="color:#289870">chapter1</span> <span style="color:#2838b0">import</span> <span style="color:#888">(</span>
    pd_readcsv<span style="color:#888">,</span>
    BUSINESS_DAYS_IN_YEAR<span style="color:#888">,</span>
    calculate_perc_returns<span style="color:#888">,</span>
    calculate_stats<span style="color:#888">,</span>
    MONTH<span style="color:#888">,</span>
<span style="color:#888">)</span>
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter2</span> <span style="color:#2838b0">import</span> calculate_minimum_capital


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_variable_standard_deviation_for_risk_targeting</span><span style="color:#888">(</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    current_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    use_perc_returns<span style="color:#888">:</span> <span style="color:#388038">bool</span> <span style="color:#666">=</span> <span style="font-style:italic">True</span><span style="color:#888">,</span>
    annualise_stdev<span style="color:#888">:</span> <span style="color:#388038">bool</span> <span style="color:#666">=</span> <span style="font-style:italic">True</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    <span style="color:#2838b0">if</span> use_perc_returns<span style="color:#888">:</span>
        daily_returns <span style="color:#666">=</span> calculate_percentage_returns<span style="color:#888">(</span>
            adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">,</span> current_price<span style="color:#666">=</span>current_price
        <span style="color:#888">)</span>
    <span style="color:#2838b0">else</span><span style="color:#888">:</span>
        daily_returns <span style="color:#666">=</span> calculate_daily_returns<span style="color:#888">(</span>adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">)</span>

    <span style="color:#888;font-style:italic">## Can do the whole series or recent history</span>
    daily_exp_std_dev <span style="color:#666">=</span> daily_returns<span style="color:#666">.</span>ewm<span style="color:#888">(</span>span<span style="color:#666">=</span><span style="color:#444">32</span><span style="color:#888">)</span><span style="color:#666">.</span>std<span style="color:#888">(</span><span style="color:#888">)</span>

    <span style="color:#2838b0">if</span> annualise_stdev<span style="color:#888">:</span>
        annualisation_factor <span style="color:#666">=</span> BUSINESS_DAYS_IN_YEAR <span style="color:#666">*</span><span style="color:#666">*</span> <span style="color:#444">0.5</span>
    <span style="color:#2838b0">else</span><span style="color:#888">:</span>
        <span style="color:#888;font-style:italic">## leave at daily</span>
        annualisation_factor <span style="color:#666">=</span> <span style="color:#444">1</span>

    annualised_std_dev <span style="color:#666">=</span> daily_exp_std_dev <span style="color:#666">*</span> annualisation_factor

    <span style="color:#888;font-style:italic">## Weight with ten year vol</span>
    ten_year_vol <span style="color:#666">=</span> annualised_std_dev<span style="color:#666">.</span>rolling<span style="color:#888">(</span>
        BUSINESS_DAYS_IN_YEAR <span style="color:#666">*</span> <span style="color:#444">10</span><span style="color:#888">,</span> min_periods<span style="color:#666">=</span><span style="color:#444">1</span>
    <span style="color:#888">)</span><span style="color:#666">.</span>mean<span style="color:#888">(</span><span style="color:#888">)</span>
    weighted_vol <span style="color:#666">=</span> <span style="color:#444">0.3</span> <span style="color:#666">*</span> ten_year_vol <span style="color:#666">+</span> <span style="color:#444">0.7</span> <span style="color:#666">*</span> annualised_std_dev

    <span style="color:#2838b0">return</span> weighted_vol


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_percentage_returns</span><span style="color:#888">(</span>
    adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span> current_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    daily_price_changes <span style="color:#666">=</span> calculate_daily_returns<span style="color:#888">(</span>adjusted_price<span style="color:#888">)</span>
    percentage_changes <span style="color:#666">=</span> daily_price_changes <span style="color:#666">/</span> current_price<span style="color:#666">.</span>shift<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> percentage_changes


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_daily_returns</span><span style="color:#888">(</span>adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    <span style="color:#2838b0">return</span> adjusted_price<span style="color:#666">.</span>diff<span style="color:#888">(</span><span style="color:#888">)</span>


<span style="color:#2838b0">class</span> <span style="color:#287088">standardDeviation</span><span style="color:#888">(</span>pd<span style="color:#666">.</span>Series<span style="color:#888">)</span><span style="color:#888">:</span>
    <span style="color:#888;font-style:italic">## class that can be eithier % or price based standard deviation estimate</span>
    <span style="color:#2838b0">def</span> <span style="color:#b85820">__init__</span><span style="color:#888">(</span>
        <span style="font-style:italic">self</span><span style="color:#888">,</span>
        adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
        current_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
        use_perc_returns<span style="color:#888">:</span> <span style="color:#388038">bool</span> <span style="color:#666">=</span> <span style="font-style:italic">True</span><span style="color:#888">,</span>
        annualise_stdev<span style="color:#888">:</span> <span style="color:#388038">bool</span> <span style="color:#666">=</span> <span style="font-style:italic">True</span><span style="color:#888">,</span>
    <span style="color:#888">)</span><span style="color:#888">:</span>

        stdev <span style="color:#666">=</span> calculate_variable_standard_deviation_for_risk_targeting<span style="color:#888">(</span>
            adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">,</span>
            current_price<span style="color:#666">=</span>current_price<span style="color:#888">,</span>
            annualise_stdev<span style="color:#666">=</span>annualise_stdev<span style="color:#888">,</span>
            use_perc_returns<span style="color:#666">=</span>use_perc_returns<span style="color:#888">,</span>
        <span style="color:#888">)</span>
        <span style="color:#388038">super</span><span style="color:#888">(</span><span style="color:#888">)</span><span style="color:#666">.</span><span style="color:#b85820">__init__</span><span style="color:#888">(</span>stdev<span style="color:#888">)</span>

        <span style="font-style:italic">self</span><span style="color:#666">.</span>_use_perc_returns <span style="color:#666">=</span> use_perc_returns
        <span style="font-style:italic">self</span><span style="color:#666">.</span>_annualised <span style="color:#666">=</span> annualise_stdev
        <span style="font-style:italic">self</span><span style="color:#666">.</span>_current_price <span style="color:#666">=</span> current_price

    <span style="color:#2838b0">def</span> <span style="color:#785840">daily_risk_price_terms</span><span style="color:#888">(</span><span style="font-style:italic">self</span><span style="color:#888">)</span><span style="color:#888">:</span>
        stdev <span style="color:#666">=</span> copy<span style="color:#888">(</span><span style="font-style:italic">self</span><span style="color:#888">)</span>
        <span style="color:#2838b0">if</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>annualised<span style="color:#888">:</span>
            stdev <span style="color:#666">=</span> stdev <span style="color:#666">/</span> <span style="color:#888">(</span>BUSINESS_DAYS_IN_YEAR <span style="color:#666">*</span><span style="color:#666">*</span> <span style="color:#444">0.5</span><span style="color:#888">)</span>

        <span style="color:#2838b0">if</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>use_perc_returns<span style="color:#888">:</span>
            stdev <span style="color:#666">=</span> stdev <span style="color:#666">*</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>current_price

        <span style="color:#2838b0">return</span> stdev

    <span style="color:#2838b0">def</span> <span style="color:#785840">annual_risk_price_terms</span><span style="color:#888">(</span><span style="font-style:italic">self</span><span style="color:#888">)</span><span style="color:#888">:</span>
        stdev <span style="color:#666">=</span> copy<span style="color:#888">(</span><span style="font-style:italic">self</span><span style="color:#888">)</span>
        <span style="color:#2838b0">if</span> <span style="color:#a848a8">not</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>annualised<span style="color:#888">:</span>
            <span style="color:#888;font-style:italic"># daily</span>
            stdev <span style="color:#666">=</span> stdev <span style="color:#666">*</span> <span style="color:#888">(</span>BUSINESS_DAYS_IN_YEAR <span style="color:#666">*</span><span style="color:#666">*</span> <span style="color:#444">0.5</span><span style="color:#888">)</span>

        <span style="color:#2838b0">if</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>use_perc_returns<span style="color:#888">:</span>
            stdev <span style="color:#666">=</span> stdev <span style="color:#666">*</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>current_price

        <span style="color:#2838b0">return</span> stdev

    <span style="color:#287088">@property</span>
    <span style="color:#2838b0">def</span> <span style="color:#785840">annualised</span><span style="color:#888">(</span><span style="font-style:italic">self</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">bool</span><span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>_annualised

    <span style="color:#287088">@property</span>
    <span style="color:#2838b0">def</span> <span style="color:#785840">use_perc_returns</span><span style="color:#888">(</span><span style="font-style:italic">self</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">bool</span><span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>_use_perc_returns

    <span style="color:#287088">@property</span>
    <span style="color:#2838b0">def</span> <span style="color:#785840">current_price</span><span style="color:#888">(</span><span style="font-style:italic">self</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> <span style="font-style:italic">self</span><span style="color:#666">.</span>_current_price


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_position_series_given_variable_risk</span><span style="color:#888">(</span>
    capital<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    risk_target_tau<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    fx<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
    multiplier<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    instrument_risk<span style="color:#888">:</span> standardDeviation<span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    <span style="color:#888;font-style:italic"># N = (Capital × τ) ÷ (Multiplier × Price × FX × σ %)</span>
    <span style="color:#888;font-style:italic">## resolves to N = (Capital × τ) ÷ (Multiplier × FX × daily stdev price terms × 16)</span>
    <span style="color:#888;font-style:italic">## for simplicity we use the daily risk in price terms, even if we calculated annualised % returns</span>
    daily_risk_price_terms <span style="color:#666">=</span> instrument_risk<span style="color:#666">.</span>daily_risk_price_terms<span style="color:#888">(</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> <span style="color:#888">(</span>
        capital
        <span style="color:#666">*</span> risk_target_tau
        <span style="color:#666">/</span> <span style="color:#888">(</span>multiplier <span style="color:#666">*</span> fx <span style="color:#666">*</span> daily_risk_price_terms <span style="color:#666">*</span> <span style="color:#888">(</span>BUSINESS_DAYS_IN_YEAR <span style="color:#666">*</span><span style="color:#666">*</span> <span style="color:#444">0.5</span><span style="color:#888">)</span><span style="color:#888">)</span>
    <span style="color:#888">)</span>


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_turnover</span><span style="color:#888">(</span>position<span style="color:#888">,</span> average_position<span style="color:#888">)</span><span style="color:#888">:</span>
    daily_trades <span style="color:#666">=</span> position<span style="color:#666">.</span>diff<span style="color:#888">(</span><span style="color:#888">)</span>
    as_proportion_of_average <span style="color:#666">=</span> daily_trades<span style="color:#666">.</span>abs<span style="color:#888">(</span><span style="color:#888">)</span> <span style="color:#666">/</span> average_position<span style="color:#666">.</span>shift<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">)</span>
    average_daily <span style="color:#666">=</span> as_proportion_of_average<span style="color:#666">.</span>mean<span style="color:#888">(</span><span style="color:#888">)</span>
    annualised_turnover <span style="color:#666">=</span> average_daily <span style="color:#666">*</span> BUSINESS_DAYS_IN_YEAR

    <span style="color:#2838b0">return</span> annualised_turnover


<span style="color:#2838b0">if</span> <span style="color:#b85820">__name__</span> <span style="color:#666">==</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">__main__</span><span style="color:#b83838">&#34;</span><span style="color:#888">:</span>
    <span style="color:#888;font-style:italic">## Get the file from https://gitfront.io/r/user-4000052/iTvUZwEUN2Ta/AFTS-CODE/blob/sp500.csv</span>
    data <span style="color:#666">=</span> pd_readcsv<span style="color:#888">(</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">sp500.csv</span><span style="color:#b83838">&#34;</span><span style="color:#888">)</span>
    data <span style="color:#666">=</span> data<span style="color:#666">.</span>dropna<span style="color:#888">(</span><span style="color:#888">)</span>

    adjusted_price <span style="color:#666">=</span> data<span style="color:#666">.</span>adjusted
    current_price <span style="color:#666">=</span> data<span style="color:#666">.</span>underlying
    multiplier <span style="color:#666">=</span> <span style="color:#444">5</span>
    risk_target_tau <span style="color:#666">=</span> <span style="color:#444">0.2</span>
    fx_series <span style="color:#666">=</span> pd<span style="color:#666">.</span>Series<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">,</span> index<span style="color:#666">=</span>data<span style="color:#666">.</span>index<span style="color:#888">)</span>  <span style="color:#888;font-style:italic">## FX rate, 1 for USD / USD</span>

    capital <span style="color:#666">=</span> <span style="color:#444">100000</span>  <span style="color:#888;font-style:italic">## applies only to strategy 1</span>

    <span style="color:#888;font-style:italic">## eithier use annual # % returns, or daily price differences to calculate</span>
    instrument_risk <span style="color:#666">=</span> standardDeviation<span style="color:#888">(</span>
        adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">,</span>
        current_price<span style="color:#666">=</span>current_price<span style="color:#888">,</span>
        use_perc_returns<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>
        annualise_stdev<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#888;font-style:italic">## or</span>
    <span style="color:#444"></span><span style="color:#b83838">&#34;&#34;&#34;</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">    instrument_risk = standardDeviation(adjusted_price=adjusted_price,</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">                                                current_price=current_price,</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">                                                 use_perc_returns=False,</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">                                                 annualise_stdev=False)</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">    </span><span style="color:#b83838">&#34;&#34;&#34;</span>

    position_contracts_held <span style="color:#666">=</span> calculate_position_series_given_variable_risk<span style="color:#888">(</span>
        capital<span style="color:#666">=</span>capital<span style="color:#888">,</span>
        fx<span style="color:#666">=</span>fx_series<span style="color:#888">,</span>
        instrument_risk<span style="color:#666">=</span>instrument_risk<span style="color:#888">,</span>
        risk_target_tau<span style="color:#666">=</span>risk_target_tau<span style="color:#888">,</span>
        multiplier<span style="color:#666">=</span>multiplier<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    perc_return <span style="color:#666">=</span> calculate_perc_returns<span style="color:#888">(</span>
        position_contracts_held<span style="color:#666">=</span>position_contracts_held<span style="color:#888">,</span>
        adjusted_price<span style="color:#666">=</span>adjusted_price<span style="color:#888">,</span>
        fx_series<span style="color:#666">=</span>fx_series<span style="color:#888">,</span>
        capital_required<span style="color:#666">=</span>capital<span style="color:#888">,</span>
        multiplier<span style="color:#666">=</span>multiplier<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return<span style="color:#888">)</span><span style="color:#888">)</span>
    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return<span style="color:#888">)</span><span style="color:#888">,</span> MONTH<span style="color:#888">)</span>

    <span style="color:#2838b0">print</span><span style="color:#888">(</span>
        calculate_minimum_capital<span style="color:#888">(</span>
            multiplier<span style="color:#666">=</span>multiplier<span style="color:#888">,</span>
            risk_target<span style="color:#666">=</span>risk_target_tau<span style="color:#888">,</span>
            fx<span style="color:#666">=</span><span style="color:#444">1</span><span style="color:#888">,</span>
            instrument_risk_ann_perc<span style="color:#666">=</span>instrument_risk_ann_perc<span style="color:#888">[</span><span style="color:#666">-</span><span style="color:#444">1</span><span style="color:#888">]</span><span style="color:#888">,</span>
            price<span style="color:#666">=</span>current_price<span style="color:#888">[</span><span style="color:#666">-</span><span style="color:#444">1</span><span style="color:#888">]</span><span style="color:#888">,</span>
        <span style="color:#888">)</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">print</span><span style="color:#888">(</span>
        calculate_turnover<span style="color:#888">(</span>
            position_contracts_held<span style="color:#888">,</span> average_position<span style="color:#666">=</span>position_contracts_held
        <span style="color:#888">)</span>
    <span style="color:#888">)</span>
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
