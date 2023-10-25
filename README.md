# trend-following
Will hold development and strategy testing for divergence.

## Chapter 5: Slow Trend Following, Long Only
Long positions using Exponetially Weight Moving Average Crossovers, typically with 64 and 256 day periods.
However, we can also use groups of indicators to determine a trend. Consider EWMAC to be a binary function.
So EWMAC(64, 256) is a binary function that returns 1 if the 64 day EWMAC is greater than the 256 day EWMAC.
We can use and array of 64-256, 32-128, and so on either longer or shorter do give us better insight into the trend.
