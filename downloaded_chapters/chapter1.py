<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <meta name="robots" content="noindex" />
        <link rel="stylesheet" href="../style.css">
        <title>chapter1.py · AFTS-CODE · GitFront</title>
    </head>
    <body>
        <div class="container">
            <div class="location">
                <a href="..">AFTS-CODE</a> /
                <span>chapter1.py</span>
            </div>

            <div class="blob-view">
                <div class="header">
                    <div>chapter1.py</div>
                    <div class="last">
                        <a class="btn" href="../raw/chapter1.py">Raw</a>
                    </div>
                </div>
                <div class="content ">
                    <pre style="background-color:#fff"><span style="color:#444"></span><span style="color:#b83838">&#34;&#34;&#34;</span><span style="color:#b83838">
</span><span style="color:#b83838"></span><span style="color:#b83838">This is the provided example python code for Chapter one of the book:</span><span style="color:#b83838">
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

<span style="color:#2838b0">from</span> <span style="color:#289870">enum</span> <span style="color:#2838b0">import</span> Enum
<span style="color:#2838b0">from</span> <span style="color:#289870">scipy.stats</span> <span style="color:#2838b0">import</span> norm
<span style="color:#2838b0">import</span> <span style="color:#289870">pandas</span> <span style="color:#2838b0">as</span> <span style="color:#289870">pd</span>
<span style="color:#2838b0">import</span> <span style="color:#289870">numpy</span> <span style="color:#2838b0">as</span> <span style="color:#289870">np</span>


DEFAULT_DATE_FORMAT <span style="color:#666">=</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">%</span><span style="color:#b83838">Y-</span><span style="color:#b83838">%</span><span style="color:#b83838">m-</span><span style="color:#b83838;text-decoration:underline">%d</span><span style="color:#b83838">&#34;</span>

<span style="color:#2838b0">def</span> <span style="color:#785840">pd_readcsv</span><span style="color:#888">(</span>
    filename<span style="color:#888">:</span> <span style="color:#388038">str</span><span style="color:#888">,</span>
        date_format<span style="color:#666">=</span>DEFAULT_DATE_FORMAT<span style="color:#888">,</span>
        date_index_name<span style="color:#888">:</span> <span style="color:#388038">str</span><span style="color:#666">=</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">index</span><span style="color:#b83838">&#34;</span><span style="color:#888">,</span>
<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>DataFrame<span style="color:#888">:</span>

    ans <span style="color:#666">=</span> pd<span style="color:#666">.</span>read_csv<span style="color:#888">(</span>filename<span style="color:#888">)</span>
    ans<span style="color:#666">.</span>index <span style="color:#666">=</span> pd<span style="color:#666">.</span>to_datetime<span style="color:#888">(</span>ans<span style="color:#888">[</span>date_index_name<span style="color:#888">]</span><span style="color:#888">,</span> format<span style="color:#666">=</span>date_format<span style="color:#888">)</span><span style="color:#666">.</span>values

    <span style="color:#2838b0">del</span> ans<span style="color:#888">[</span>date_index_name<span style="color:#888">]</span>

    ans<span style="color:#666">.</span>index<span style="color:#666">.</span>name <span style="color:#666">=</span> <span style="font-style:italic">None</span>

    <span style="color:#2838b0">return</span> ans


<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_perc_returns</span><span style="color:#888">(</span>position_contracts_held<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                            adjusted_price<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                           fx_series<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                           multiplier<span style="color:#888">:</span> <span style="color:#388038">float</span><span style="color:#888">,</span>
                           capital_required<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                           <span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    return_price_points <span style="color:#666">=</span> <span style="color:#888">(</span>adjusted_price <span style="color:#666">-</span> adjusted_price<span style="color:#666">.</span>shift<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">)</span><span style="color:#888">)</span><span style="color:#666">*</span>position_contracts_held<span style="color:#666">.</span>shift<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">)</span>

    return_instrument_currency <span style="color:#666">=</span> return_price_points <span style="color:#666">*</span> multiplier
    fx_series_aligned <span style="color:#666">=</span> fx_series<span style="color:#666">.</span>reindex<span style="color:#888">(</span>return_instrument_currency<span style="color:#666">.</span>index<span style="color:#888">,</span> method<span style="color:#666">=</span><span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">ffill</span><span style="color:#b83838">&#34;</span><span style="color:#888">)</span>
    return_base_currency <span style="color:#666">=</span> return_instrument_currency <span style="color:#666">*</span> fx_series_aligned

    perc_return <span style="color:#666">=</span> return_base_currency <span style="color:#666">/</span> capital_required

    <span style="color:#2838b0">return</span> perc_return



Frequency <span style="color:#666">=</span> Enum<span style="color:#888">(</span>
    <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">Frequency</span><span style="color:#b83838">&#34;</span><span style="color:#888">,</span>
    <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">Natural Year Month Week BDay</span><span style="color:#b83838">&#34;</span><span style="color:#888">,</span>
<span style="color:#888">)</span>

NATURAL <span style="color:#666">=</span> Frequency<span style="color:#666">.</span>Natural
YEAR <span style="color:#666">=</span> Frequency<span style="color:#666">.</span>Year
MONTH <span style="color:#666">=</span> Frequency<span style="color:#666">.</span>Month
WEEK <span style="color:#666">=</span> Frequency<span style="color:#666">.</span>Week



<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_stats</span><span style="color:#888">(</span>perc_return<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                at_frequency<span style="color:#888">:</span> Frequency <span style="color:#666">=</span> NATURAL<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">dict</span><span style="color:#888">:</span>

    perc_return_at_freq <span style="color:#666">=</span> sum_at_frequency<span style="color:#888">(</span>perc_return<span style="color:#888">,</span> at_frequency<span style="color:#666">=</span>at_frequency<span style="color:#888">)</span>

    ann_mean <span style="color:#666">=</span> ann_mean_given_frequency<span style="color:#888">(</span>perc_return_at_freq<span style="color:#888">,</span> at_frequency<span style="color:#666">=</span>at_frequency<span style="color:#888">)</span>
    ann_std <span style="color:#666">=</span> ann_std_given_frequency<span style="color:#888">(</span>perc_return_at_freq<span style="color:#888">,</span> at_frequency<span style="color:#666">=</span>at_frequency<span style="color:#888">)</span>
    sharpe_ratio <span style="color:#666">=</span> ann_mean <span style="color:#666">/</span> ann_std

    skew_at_freq <span style="color:#666">=</span> perc_return_at_freq<span style="color:#666">.</span>skew<span style="color:#888">(</span><span style="color:#888">)</span>
    drawdowns <span style="color:#666">=</span> calculate_drawdown<span style="color:#888">(</span>perc_return_at_freq<span style="color:#888">)</span>
    avg_drawdown <span style="color:#666">=</span> drawdowns<span style="color:#666">.</span>mean<span style="color:#888">(</span><span style="color:#888">)</span>
    max_drawdown <span style="color:#666">=</span> drawdowns<span style="color:#666">.</span>max<span style="color:#888">(</span><span style="color:#888">)</span>
    quant_ratio_lower <span style="color:#666">=</span> calculate_quant_ratio_upper<span style="color:#888">(</span>perc_return_at_freq<span style="color:#888">)</span>
    quant_ratio_upper <span style="color:#666">=</span> calculate_quant_ratio_upper<span style="color:#888">(</span>perc_return_at_freq<span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> <span style="color:#388038">dict</span><span style="color:#888">(</span>
        ann_mean <span style="color:#666">=</span> ann_mean<span style="color:#888">,</span>
        ann_std <span style="color:#666">=</span> ann_std<span style="color:#888">,</span>
        sharpe_ratio <span style="color:#666">=</span> sharpe_ratio<span style="color:#888">,</span>
        skew <span style="color:#666">=</span> skew_at_freq<span style="color:#888">,</span>
        avg_drawdown <span style="color:#666">=</span> avg_drawdown<span style="color:#888">,</span>
        max_drawdown <span style="color:#666">=</span> max_drawdown<span style="color:#888">,</span>
        quant_ratio_lower <span style="color:#666">=</span> quant_ratio_lower<span style="color:#888">,</span>
        quant_ratio_upper <span style="color:#666">=</span> quant_ratio_upper
    <span style="color:#888">)</span>

BUSINESS_DAYS_IN_YEAR <span style="color:#666">=</span> <span style="color:#444">256</span>
WEEKS_PER_YEAR <span style="color:#666">=</span> <span style="color:#444">52.25</span>
MONTHS_PER_YEAR <span style="color:#666">=</span> <span style="color:#444">12</span>
SECONDS_PER_YEAR <span style="color:#666">=</span> <span style="color:#444">365.25</span> <span style="color:#666">*</span> <span style="color:#444">24</span> <span style="color:#666">*</span> <span style="color:#444">60</span> <span style="color:#666">*</span> <span style="color:#444">60</span>

PERIODS_PER_YEAR <span style="color:#666">=</span> <span style="color:#888">{</span>
    MONTH<span style="color:#888">:</span> MONTHS_PER_YEAR<span style="color:#888">,</span>
    WEEK<span style="color:#888">:</span> WEEKS_PER_YEAR<span style="color:#888">,</span>
    YEAR<span style="color:#888">:</span> <span style="color:#444">1</span>

<span style="color:#888">}</span>

<span style="color:#2838b0">def</span> <span style="color:#785840">periods_per_year</span><span style="color:#888">(</span>at_frequency<span style="color:#888">:</span> Frequency<span style="color:#888">)</span><span style="color:#888">:</span>
    <span style="color:#2838b0">if</span> at_frequency <span style="color:#666">==</span> NATURAL<span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> BUSINESS_DAYS_IN_YEAR
    <span style="color:#2838b0">else</span><span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> PERIODS_PER_YEAR<span style="color:#888">[</span>at_frequency<span style="color:#888">]</span>



<span style="color:#2838b0">def</span> <span style="color:#785840">years_in_data</span><span style="color:#888">(</span>some_data<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">float</span><span style="color:#888">:</span>
    datediff <span style="color:#666">=</span> some_data<span style="color:#666">.</span>index<span style="color:#888">[</span><span style="color:#666">-</span><span style="color:#444">1</span><span style="color:#888">]</span> <span style="color:#666">-</span> some_data<span style="color:#666">.</span>index<span style="color:#888">[</span><span style="color:#444">0</span><span style="color:#888">]</span>
    seconds_in_data <span style="color:#666">=</span> datediff<span style="color:#666">.</span>total_seconds<span style="color:#888">(</span><span style="color:#888">)</span>
    <span style="color:#2838b0">return</span> seconds_in_data <span style="color:#666">/</span> SECONDS_PER_YEAR


<span style="color:#2838b0">def</span> <span style="color:#785840">sum_at_frequency</span><span style="color:#888">(</span>perc_return<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                     at_frequency<span style="color:#888">:</span> Frequency <span style="color:#666">=</span> NATURAL<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> pd<span style="color:#666">.</span>Series<span style="color:#888">:</span>

    <span style="color:#2838b0">if</span> at_frequency <span style="color:#666">==</span> NATURAL<span style="color:#888">:</span>
        <span style="color:#2838b0">return</span> perc_return

    at_frequency_str_dict <span style="color:#666">=</span> <span style="color:#888">{</span>
                        YEAR<span style="color:#888">:</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">Y</span><span style="color:#b83838">&#34;</span><span style="color:#888">,</span>
                        WEEK<span style="color:#888">:</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">7D</span><span style="color:#b83838">&#34;</span><span style="color:#888">,</span>
                        MONTH<span style="color:#888">:</span> <span style="color:#444"></span><span style="color:#b83838">&#34;</span><span style="color:#b83838">1M</span><span style="color:#b83838">&#34;</span><span style="color:#888">}</span>
    at_frequency_str <span style="color:#666">=</span> at_frequency_str_dict<span style="color:#888">[</span>at_frequency<span style="color:#888">]</span>

    perc_return_at_freq <span style="color:#666">=</span> perc_return<span style="color:#666">.</span>resample<span style="color:#888">(</span>at_frequency_str<span style="color:#888">)</span><span style="color:#666">.</span>sum<span style="color:#888">(</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> perc_return_at_freq


<span style="color:#2838b0">def</span> <span style="color:#785840">ann_mean_given_frequency</span><span style="color:#888">(</span>perc_return_at_freq<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                             at_frequency<span style="color:#888">:</span> Frequency<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">float</span><span style="color:#888">:</span>

    mean_at_frequency <span style="color:#666">=</span> perc_return_at_freq<span style="color:#666">.</span>mean<span style="color:#888">(</span><span style="color:#888">)</span>
    periods_per_year_for_frequency <span style="color:#666">=</span> periods_per_year<span style="color:#888">(</span>at_frequency<span style="color:#888">)</span>
    annualised_mean <span style="color:#666">=</span> mean_at_frequency <span style="color:#666">*</span> periods_per_year_for_frequency

    <span style="color:#2838b0">return</span> annualised_mean

<span style="color:#2838b0">def</span> <span style="color:#785840">ann_std_given_frequency</span><span style="color:#888">(</span>perc_return_at_freq<span style="color:#888">:</span> pd<span style="color:#666">.</span>Series<span style="color:#888">,</span>
                             at_frequency<span style="color:#888">:</span> Frequency<span style="color:#888">)</span> <span style="color:#666">-</span><span style="color:#666">&gt;</span> <span style="color:#388038">float</span><span style="color:#888">:</span>

    std_at_frequency <span style="color:#666">=</span> perc_return_at_freq<span style="color:#666">.</span>std<span style="color:#888">(</span><span style="color:#888">)</span>
    periods_per_year_for_frequency <span style="color:#666">=</span> periods_per_year<span style="color:#888">(</span>at_frequency<span style="color:#888">)</span>
    annualised_std <span style="color:#666">=</span> std_at_frequency <span style="color:#666">*</span> <span style="color:#888">(</span>periods_per_year_for_frequency<span style="color:#666">*</span><span style="color:#666">*</span><span style="color:#666">.</span><span style="color:#444">5</span><span style="color:#888">)</span>

    <span style="color:#2838b0">return</span> annualised_std




<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_drawdown</span><span style="color:#888">(</span>perc_return<span style="color:#888">)</span><span style="color:#888">:</span>
    cum_perc_return <span style="color:#666">=</span> perc_return<span style="color:#666">.</span>cumsum<span style="color:#888">(</span><span style="color:#888">)</span>
    max_cum_perc_return <span style="color:#666">=</span> cum_perc_return<span style="color:#666">.</span>rolling<span style="color:#888">(</span><span style="color:#388038">len</span><span style="color:#888">(</span>perc_return<span style="color:#888">)</span><span style="color:#666">+</span><span style="color:#444">1</span><span style="color:#888">,</span>
                                                  min_periods<span style="color:#666">=</span><span style="color:#444">1</span><span style="color:#888">)</span><span style="color:#666">.</span>max<span style="color:#888">(</span><span style="color:#888">)</span>
    <span style="color:#2838b0">return</span> max_cum_perc_return <span style="color:#666">-</span> cum_perc_return

QUANT_PERCENTILE_EXTREME <span style="color:#666">=</span> <span style="color:#444">0.01</span>
QUANT_PERCENTILE_STD <span style="color:#666">=</span> <span style="color:#444">0.3</span>
NORMAL_DISTR_RATIO <span style="color:#666">=</span> norm<span style="color:#666">.</span>ppf<span style="color:#888">(</span>QUANT_PERCENTILE_EXTREME<span style="color:#888">)</span> <span style="color:#666">/</span> norm<span style="color:#666">.</span>ppf<span style="color:#888">(</span>QUANT_PERCENTILE_STD<span style="color:#888">)</span>

<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_quant_ratio_lower</span><span style="color:#888">(</span>x<span style="color:#888">)</span><span style="color:#888">:</span>
    x_dm <span style="color:#666">=</span> demeaned_remove_zeros<span style="color:#888">(</span>x<span style="color:#888">)</span>
    raw_ratio <span style="color:#666">=</span> x_dm<span style="color:#666">.</span>quantile<span style="color:#888">(</span>QUANT_PERCENTILE_EXTREME<span style="color:#888">)</span> <span style="color:#666">/</span> x_dm<span style="color:#666">.</span>quantile<span style="color:#888">(</span>
        QUANT_PERCENTILE_STD
    <span style="color:#888">)</span>
    <span style="color:#2838b0">return</span> raw_ratio <span style="color:#666">/</span> NORMAL_DISTR_RATIO

<span style="color:#2838b0">def</span> <span style="color:#785840">calculate_quant_ratio_upper</span><span style="color:#888">(</span>x<span style="color:#888">)</span><span style="color:#888">:</span>
    x_dm <span style="color:#666">=</span> demeaned_remove_zeros<span style="color:#888">(</span>x<span style="color:#888">)</span>
    raw_ratio <span style="color:#666">=</span> x_dm<span style="color:#666">.</span>quantile<span style="color:#888">(</span><span style="color:#444">1</span> <span style="color:#666">-</span> QUANT_PERCENTILE_EXTREME<span style="color:#888">)</span> <span style="color:#666">/</span> x_dm<span style="color:#666">.</span>quantile<span style="color:#888">(</span>
        <span style="color:#444">1</span> <span style="color:#666">-</span> QUANT_PERCENTILE_STD
    <span style="color:#888">)</span>
    <span style="color:#2838b0">return</span> raw_ratio <span style="color:#666">/</span> NORMAL_DISTR_RATIO

<span style="color:#2838b0">def</span> <span style="color:#785840">demeaned_remove_zeros</span><span style="color:#888">(</span>x<span style="color:#888">)</span><span style="color:#888">:</span>
    x<span style="color:#888">[</span>x <span style="color:#666">==</span> <span style="color:#444">0</span><span style="color:#888">]</span> <span style="color:#666">=</span> np<span style="color:#666">.</span>nan
    <span style="color:#2838b0">return</span> x <span style="color:#666">-</span> x<span style="color:#666">.</span>mean<span style="color:#888">(</span><span style="color:#888">)</span>


<span style="color:#2838b0">if</span> <span style="color:#b85820">__name__</span> <span style="color:#666">==</span> <span style="color:#444"></span><span style="color:#b83838">&#39;</span><span style="color:#b83838">__main__</span><span style="color:#b83838">&#39;</span><span style="color:#888">:</span>
    <span style="color:#888;font-style:italic">## Get the file from https://gitfront.io/r/user-4000052/iTvUZwEUN2Ta/AFTS-CODE/blob/sp500.csv</span>
    data <span style="color:#666">=</span> pd_readcsv<span style="color:#888">(</span><span style="color:#444"></span><span style="color:#b83838">&#39;</span><span style="color:#b83838">sp500.csv</span><span style="color:#b83838">&#39;</span><span style="color:#888">)</span>
    data <span style="color:#666">=</span> data<span style="color:#666">.</span>dropna<span style="color:#888">(</span><span style="color:#888">)</span>

    adjusted_price <span style="color:#666">=</span> data<span style="color:#666">.</span>adjusted
    current_price <span style="color:#666">=</span> data<span style="color:#666">.</span>underlying
    multiplier <span style="color:#666">=</span> <span style="color:#444">5</span>
    fx_series <span style="color:#666">=</span> pd<span style="color:#666">.</span>Series<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">,</span> index<span style="color:#666">=</span>data<span style="color:#666">.</span>index<span style="color:#888">)</span>  <span style="color:#888;font-style:italic">## FX rate, 1 for USD / USD</span>
    position_contracts_held <span style="color:#666">=</span> pd<span style="color:#666">.</span>Series<span style="color:#888">(</span><span style="color:#444">1</span><span style="color:#888">,</span> index<span style="color:#666">=</span>data<span style="color:#666">.</span>index<span style="color:#888">)</span>  <span style="color:#888;font-style:italic">## applies only to strategy 1</span>

    capital_required <span style="color:#666">=</span> multiplier <span style="color:#666">*</span> current_price  <span style="color:#888;font-style:italic">## applies only to strategy 1</span>

    perc_return <span style="color:#666">=</span> calculate_perc_returns<span style="color:#888">(</span>
        position_contracts_held<span style="color:#666">=</span>position_contracts_held<span style="color:#888">,</span>
        adjusted_price <span style="color:#666">=</span> adjusted_price<span style="color:#888">,</span>
        fx_series<span style="color:#666">=</span>fx_series<span style="color:#888">,</span>
        capital_required<span style="color:#666">=</span>capital_required<span style="color:#888">,</span>
        multiplier<span style="color:#666">=</span>multiplier
    <span style="color:#888">)</span>

    <span style="color:#2838b0">print</span><span style="color:#888">(</span>calculate_stats<span style="color:#888">(</span>perc_return<span style="color:#888">,</span> at_frequency<span style="color:#666">=</span>MONTH<span style="color:#888">)</span><span style="color:#888">)</span>
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
