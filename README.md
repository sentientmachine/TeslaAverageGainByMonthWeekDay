
# TeslaAverageGainByMonthWeekDay

## One day I feasted my eyes on this image:

<a href="https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1">
https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1</a><br>

<img border=2 src="https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1" />

It's a histogram with growth on the vertical and month broken out into 50,20,10 lookbehind groups.<br>
<br>

Backup image in case it goes down: <a href="./snp_february_weak_for_stocks.png">./snp_february_weak_for_stocks.png</a><br>

The question we want to ask and have the histogram attempt an answer is: 

Assuming all we know about a stock is the current quarter, month, week, or day of the year, then which month,week,day of year ought you to buy the share to maximize gain or loss?  Historically speaking.

Also show trends, for which day/week/month of the year is the most profitable one as time goes on.  
Does the old adage: "sell in may and walk away" have any merit?


## Data Source:

The nasdaq exchange should be somewhat trustworthy not to fiddle/redact the historical pricing data 
for self interested reasons, since their profit angle is invester satisfaction with their rigging system
that allows them to take a cut from every placed bet.<br>

<a href="https://www.nasdaq.com/symbol/tsla/historical">https://www.nasdaq.com/symbol/tsla/historical</a><br>

Data file stored locally as 'tsla.csv'<br>

## Which Programming Language should I select for this charting job?

Brainstorming, It's a histogram, and based on my experience, 6 languages can do this, but python wins.

1.  Python's matplotlib, second to none and lots of examples.
2.  R's ggplot2, designed for statistics and data analysis.
3.  Javascript D3js 3rd party graphing plugin with every chart variation under the sun.
4.  Gnu Octave 2D and 3D charting for matrix operations.
5.  Bash gnuplot, do it for Tux.
6.  Java Jfreechart.  Just no.

Reason being that although python is an overall shitty language, in matplotlib data analysis
and library support for financial charting is second to none.  Also there's a book on my shelf: 
"Python for finance" so there's that.


## Results

![Alt text](./final.png?raw=true "so far so good")
