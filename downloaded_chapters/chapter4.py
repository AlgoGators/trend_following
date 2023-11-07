<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <meta name="robots" content="noindex" />
        <link rel="stylesheet" href="../style.css">
        <title>chapter4.py · AFTS-CODE · GitFront</title>
    </head>
    <body>
        <div class="container">
            <div class="location">
                <a href="..">AFTS-CODE</a> /
                <span>chapter4.py</span>
            </div>

            <div class="blob-view">
                <div class="header">
                    <div>chapter4.py</div>
                    <div class="last">
                        <a class="btn" href="../raw/chapter4.py">Raw</a>
                    </div>
                </div>
                <div class="content ">
                    <pre style="background-color:#fff"><span style="color:#444"></span><span style="color:#b83838">&#34;&#34;&#34;</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This is the provided example python code for Chapter four of the book:</span><span style="color:#b83838">
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

<span style="color:#2838b0">from</span> <span style="color:#289870">chapter1</span> <span style="color:#2838b0">import</span> pd_readcsv<span style="color:#888">,</span> calculate_stats<span style="color:#888">,</span> MONTH
<span style="color:#2838b0">from</span> <span style="color:#289870">chapter3</span> <span style="color:#2838b0">import</span> <span style="color:#888">(</span>
    standardDeviation<span style="color:#888">,</span>
    calculate_position_series_given_variable_risk<span style="color:#888">,</span>
    calculate_perc_returns<span style="color:#888">,</span>
<span style="color:#888">)</span>

INSTRUMENT_LIST <span style="color:#666">=</span> <span style="color:#888">[</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">sp500</span><span style="color:#b83838">&#34;</span><span style="color:#888">,</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">us10</span><span style="color:#b83838">&#34;</span><span style="color:#888">]</span>


<span style="color:#2838b0">def</span> <span style="color:#785840">get_data_dict</span><span style="color:#888">(</span><span style="color:#888">)</span><span style="color:#888">:</span>

    all_data <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>instrument_code<span style="color:#888">,</span> pd_readcsv<span style="color:#888">(</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838;text-decoration:underline">%s</span><span style="color:#b83838">.csv</span><span style="color:#b83838">&#34;</span> <span style="color:#666">%</span> instrument_code<span style="color:#888">)</span><span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> INSTRUMENT_LIST
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    adjusted_prices <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>instrument_code<span style="color:#888">,</span> data_for_instrument<span style="color:#666">.</span>adjusted<span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code<span style="color:#888">,</span> data_for_instrument <span style="color:#a848a8">in</span> all_data<span style="color:#666">.</span>items<span style="color:#888">(</span><span style="color:#888">)</span>
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    current_prices <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>instrument_code<span style="color:#888">,</span> data_for_instrument<span style="color:#666">.</span>underlying<span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code<span style="color:#888">,</span> data_for_instrument <span style="color:#a848a8">in</span> all_data<span style="color:#666">.</span>items<span style="color:#888">(</span><span style="color:#888">)</span>
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> adjusted_prices<span style="color:#888">,</span> current_prices


fx_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>eurostx<span style="color:#666">=</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">eur</span><span style="color:#b83838">&#34;</span><span style="color:#888">)</span>


<span style="color:#2838b0">def</span> <span style="color:#785840">create_fx_series_given_adjusted_prices_dict</span><span style="color:#888">(</span>adjusted_prices_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>
    fx_series_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                create_fx_series_given_adjusted_prices<span style="color:#888">(</span>
                    instrument_code<span style="color:#888">,</span> adjusted_prices
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code<span style="color:#888">,</span> adjusted_prices <span style="color:#a848a8">in</span> adjusted_prices_dict<span style="color:#666">.</span>items<span style="color:#888">(</span><span style="color:#888">)</span>
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>
    <span style="color:#2838b0">return</span> fx_series_dict


<span style="color:#2838b0">def</span> <span style="color:#785840">create_fx_series_given_adjusted_prices</span><span style="color:#888">(</span>
    instrument_code<span style="color:#888">:</span> <span style="color:#388038">str</span><span style="color:#888">,</span> adjusted_prices<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    currency_for_instrument <span style="color:#666">=</span> fx_dict<span style="color:#666">.</span>get<span style="color:#888">(</span>instrument_code<span style="color:#888">,</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">usd</span><span style="color:#b83838">&#34;</span><span style="color:#888">)</span>
    <span style="color:#2838b0">if</span> currency_for_instrument <span style="color:#666">==</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">usd</span><span style="color:#b83838">&#34;</span><span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> pd<span style="color:#666">.</span>Series<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">,</span> index<span style="color:#666">=</span>adjusted_prices<span style="color:#666">.</span>index<span style="color:#888">)</span>  <span style="color:#888;font-style:italic">## FX rate, 1 for USD / USD</span>

    fx_prices <span style="color:#666">=</span> get_fx_prices<span style="color:#888">(</span>currency_for_instrument<span style="color:#888">)</span>
    fx_prices_aligned <span style="color:#666">=</span> fx_prices<span style="color:#666">.</span>reindex<span style="color:#888">(</span>adjusted_prices<span style="color:#666">.</span>index<span style="color:#888">)</span><span style="color:#666">.</span>ffill<span style="color:#888">(</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> fx_prices_aligned


<span style="color:#2838b0">def</span> <span style="color:#785840">get_fx_prices</span><span style="color:#888">(</span>currency<span style="color:#888">:</span> <span style="color:#388038">str</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>
    prices_as_df <span style="color:#666">=</span> pd_readcsv<span style="color:#888">(</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838;text-decoration:underline">%s</span><span style="color:#b83838">_fx.csv</span><span style="color:#b83838">&#34;</span> <span style="color:#666">%</span> currency<span style="color:#888">)</span>
    <span style="color:#2838b0">return</span> prices_as_df<span style="color:#666">.</span>squeeze<span style="color:#888">(</span><span style="color:#888">)</span>


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_variable_standard_deviation_for_risk_targeting_from_dict</span><span style="color:#888">(</span>
    adjusted_prices<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    current_prices<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    use_perc_returns<span style="color:#888">:</span> <span style="color:#388038">bool</span> <span style="color:#666">=</span> <span style="font-style:italic">True</span><span style="color:#888">,</span>
    annualise_stdev<span style="color:#888">:</span> <span style="color:#388038">bool</span> <span style="color:#666">=</span> <span style="font-style:italic">True</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    std_dev_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                standardDeviation<span style="color:#888">(</span>
                    adjusted_price<span style="color:#666">=</span>adjusted_prices<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    current_price<span style="color:#666">=</span>current_prices<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    use_perc_returns<span style="color:#666">=</span>use_perc_returns<span style="color:#888">,</span>
                    annualise_stdev<span style="color:#666">=</span>annualise_stdev<span style="color:#888">,</span>
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> adjusted_prices<span style="color:#666">.</span>keys<span style="color:#888">(</span><span style="color:#888">)</span>
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> std_dev_dict


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_position_series_given_variable_risk_for_dict</span><span style="color:#888">(</span>
    capital<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    risk_target_tau<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    idm<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    weights<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    fx_series_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    multipliers<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    std_dev_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    position_series_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                calculate_position_series_given_variable_risk<span style="color:#888">(</span>
                    capital<span style="color:#666">=</span>capital <span style="color:#666">*</span> idm <span style="color:#666">*</span> weights<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    risk_target_tau<span style="color:#666">=</span>risk_target_tau<span style="color:#888">,</span>
                    multiplier<span style="color:#666">=</span>multipliers<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    fx<span style="color:#666">=</span>fx_series_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    instrument_risk<span style="color:#666">=</span>std_dev_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> std_dev_dict<span style="color:#666">.</span>keys<span style="color:#888">(</span><span style="color:#888">)</span>
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> position_series_dict


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_perc_returns_for_dict</span><span style="color:#888">(</span>
    position_contracts_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    adjusted_prices<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    multipliers<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    fx_series<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">,</span>
    capital<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    perc_returns_dict <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        <span style="color:#888">[</span>
            <span style="color:#888">(</span>
                instrument_code<span style="color:#888">,</span>
                calculate_perc_returns<span style="color:#888">(</span>
                    position_contracts_held<span style="color:#666">=</span>position_contracts_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    adjusted_price<span style="color:#666">=</span>adjusted_prices<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    multiplier<span style="color:#666">=</span>multipliers<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    fx_series<span style="color:#666">=</span>fx_series<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
                    capital_required<span style="color:#666">=</span>capital<span style="color:#888">,</span>
                <span style="color:#888">)</span><span style="color:#888">,</span>
            <span style="color:#888">)</span>
            <span style="color:#2838b0">for</span> instrument_code <span style="color:#a848a8">in</span> position_contracts_dict<span style="color:#666">.</span>keys<span style="color:#888">(</span><span style="color:#888">)</span>
        <span style="color:#888">]</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> perc_returns_dict


<span style="color:#2838b0">def</span> <span style="color:#785840">aggregate_returns</span><span style="color:#888">(</span>perc_returns_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>
    both_returns <span style="color:#666">=</span> perc_returns_to_df<span style="color:#888">(</span>perc_returns_dict<span style="color:#888">)</span>
    agg <span style="color:#666">=</span> both_returns<span style="color:#666">.</span>sum<span style="color:#888">(</span>axis<span style="color:#666">=</span><span style="color:#444">1</span><span style="color:#888">)</span>
    <span style="color:#2838b0">return</span> agg


<span style="color:#2838b0">def</span> <span style="color:#785840">perc_returns_to_df</span><span style="color:#888">(</span>perc_returns_dict<span style="color:#888">:</span> <span style="color:#388038">dict</span><span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>DataFrame<span style="color:#888">:</span>
    both_returns <span style="color:#666">=</span> pd<span style="color:#666">.</span>concat<span style="color:#888">(</span>perc_returns_dict<span style="color:#888">,</span> axis<span style="color:#666">=</span><span style="color:#444">1</span><span style="color:#888">)</span>
    both_returns <span style="color:#666">=</span> both_returns<span style="color:#666">.</span>dropna<span style="color:#888">(</span>how<span style="color:#666">=</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">all</span><span style="color:#b83838">&#34;</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> both_returns


<span style="color:#2838b0">def</span> <span style="color:#785840">minimum_capital_for_sub_strategy</span><span style="color:#888">(</span>
    multiplier<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    price<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    fx<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    instrument_risk_ann_perc<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    risk_target<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    idm<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    weight<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
    contracts<span style="color:#888">:</span> <span style="color:#388038">int</span> <span style="color:#666">=</span> <span style="color:#444">4</span><span style="color:#888">,</span>
<span style="color:#888">)</span><span style="color:#888">:</span>
    <span style="color:#888;font-style:italic"># (4 × Multiplier i × Price i, t × FX rate i, t × σ % i, t) ÷ (IDM × Weight i × τ)</span>
    <span style="color:#2838b0">return</span> <span style="color:#888">(</span>
        contracts
        <span style="color:#666">*</span> multiplier
        <span style="color:#666">*</span> price
        <span style="color:#666">*</span> fx
        <span style="color:#666">*</span> instrument_risk_ann_perc
        <span style="color:#666">/</span> <span style="color:#888">(</span>risk_target <span style="color:#666">*</span> idm <span style="color:#666">*</span> weight<span style="color:#888">)</span>
    <span style="color:#888">)</span>


<span style="color:#2838b0">if</span> <span style="color:#b85820">__name__</span> <span style="color:#666">==</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">__main__</span><span style="color:#b83838">&#34;</span><span style="color:#888">:</span>
    <span style="color:#888;font-style:italic">## Get the files from:</span>
    <span style="color:#888;font-style:italic"># https://gitfront.io/r/user-4000052/iTvUZwEUN2Ta/AFTS-CODE/blob/sp500.csv</span>
    <span style="color:#888;font-style:italic"># and https://gitfront.io/r/user-4000052/iTvUZwEUN2Ta/AFTS-CODE/blob/US10.csv</span>
    adjusted_prices<span style="color:#888">,</span> current_prices <span style="color:#666">=</span> get_data_dict<span style="color:#888">(</span><span style="color:#888">)</span>

    multipliers <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>sp500<span style="color:#666">=</span><span style="color:#444">5</span><span style="color:#888">,</span> us10<span style="color:#666">=</span><span style="color:#444">1000</span><span style="color:#888">)</span>
    risk_target_tau <span style="color:#666">=</span> <span style="color:#444">0.2</span>

    fx_series_dict <span style="color:#666">=</span> create_fx_series_given_adjusted_prices_dict<span style="color:#888">(</span>adjusted_prices<span style="color:#888">)</span>

    capital <span style="color:#666">=</span> <span style="color:#444">1000000</span>
    idm <span style="color:#666">=</span> <span style="color:#444">1.5</span>
    instrument_weights <span style="color:#666">=</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>sp500<span style="color:#666">=</span><span style="color:#444">0.5</span><span style="color:#888">,</span> us10<span style="color:#666">=</span><span style="color:#444">0.5</span><span style="color:#888">)</span>

    std_dev_dict <span style="color:#666">=</span> calculate_variable_standard_deviation_for_risk_targeting_from_dict<span style="color:#888">(</span>
        adjusted_prices<span style="color:#666">=</span>adjusted_prices<span style="color:#888">,</span>
        current_prices<span style="color:#666">=</span>current_prices<span style="color:#888">,</span>
        annualise_stdev<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>  <span style="color:#888;font-style:italic">## can also be False if want to use daily price diff</span>
        use_perc_returns<span style="color:#666">=</span><span style="font-style:italic">True</span><span style="color:#888">,</span>  <span style="color:#888;font-style:italic">## can also be False if want to use daily price diff</span>
    <span style="color:#888">)</span>

    position_contracts_dict <span style="color:#666">=</span> calculate_position_series_given_variable_risk_for_dict<span style="color:#888">(</span>
        capital<span style="color:#666">=</span>capital<span style="color:#888">,</span>
        risk_target_tau<span style="color:#666">=</span>risk_target_tau<span style="color:#888">,</span>
        idm<span style="color:#666">=</span>idm<span style="color:#888">,</span>
        weights<span style="color:#666">=</span>instrument_weights<span style="color:#888">,</span>
        std_dev_dict<span style="color:#666">=</span>std_dev_dict<span style="color:#888">,</span>
        fx_series_dict<span style="color:#666">=</span>fx_series_dict<span style="color:#888">,</span>
        multipliers<span style="color:#666">=</span>multipliers<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    perc_return_dict <span style="color:#666">=</span> calculate_perc_returns_for_dict<span style="color:#888">(</span>
        position_contracts_dict<span style="color:#666">=</span>position_contracts_dict<span style="color:#888">,</span>
        fx_series<span style="color:#666">=</span>fx_series_dict<span style="color:#888">,</span>
        multipliers<span style="color:#666">=</span>multipliers<span style="color:#888">,</span>
        capital<span style="color:#666">=</span>capital<span style="color:#888">,</span>
        adjusted_prices<span style="color:#666">=</span>adjusted_prices<span style="color:#888">,</span>
    <span style="color:#888">)</span>

    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return_dict<span style="color:#888">[</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">sp500</span><span style="color:#b83838">&#34;</span><span style="color:#888">]</span><span style="color:#888">)</span><span style="color:#888">)</span>

    perc_return_agg <span style="color:#666">=</span> aggregate_returns<span style="color:#888">(</span>perc_return_dict<span style="color:#888">)</span>
    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return_agg<span style="color:#888">)</span><span style="color:#888">)</span>

    instrument_code <span style="color:#666">=</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">us10</span><span style="color:#b83838">&#34;</span>
    <span style="color:#2838b0">print</span><span style="color:#888">(</span>
        minimum_capital_for_sub_strategy<span style="color:#888">(</span>
            multiplier<span style="color:#666">=</span>multipliers<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
            risk_target<span style="color:#666">=</span>risk_target_tau<span style="color:#888">,</span>
            fx<span style="color:#666">=</span>fx_series_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">[</span><span style="color:#666">-</span><span style="color:#444">1</span><span style="color:#888">]</span><span style="color:#888">,</span>
            idm<span style="color:#666">=</span>idm<span style="color:#888">,</span>
            weight<span style="color:#666">=</span>instrument_weights<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">,</span>
            instrument_risk_ann_perc<span style="color:#666">=</span>std_dev_dict<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">[</span><span style="color:#666">-</span><span style="color:#444">1</span><span style="color:#888">]</span><span style="color:#888">,</span>
            price<span style="color:#666">=</span>current_prices<span style="color:#888">[</span>instrument_code<span style="color:#888">]</span><span style="color:#888">[</span><span style="color:#666">-</span><span style="color:#444">1</span><span style="color:#888">]</span><span style="color:#888">,</span>
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
