
# TeslaAverageGainByMonthWeekDay

Sole author of this project for this writeup, images and code: Eric Leschinski.

Inspired by a snuck glance at a chart from a Bloomberg terminal, I decided to recreate it from first principles in Python2.7 for my favorite company: TSLA.

## I feasted my eyes on this image:

<a href="https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1">
https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1</a><br>

<img border=2 src="https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1" />

It's a histogram with average percentage growth on the vertical and month broken out into 50,20,10 year lookbehind groups, averaged.  It attempts to answer the question: "Which month is the best month to buy stocks?"<br>
<br>

Backup image: <a href="./snp_february_weak_for_stocks.png">./snp_february_weak_for_stocks.png</a><br>

### The purpose for this chart is to attempt to answer the question: 

TLDR: Does the old stock market adage: "sell in may and walk away" have any truth to it in Tesla?

More specifically: Assuming all we know about a stock is the current open/high/low/close for the quarter, month, week, or day of a year over time, which month, week, or day of year is best to buy shares, to maximize probability of gain?  Historically speaking.

Also show trends, for which day/week/month of the year is the most profitable one as time goes on.  



## Data Source:

Nasdaq exchange:

<a href="https://www.nasdaq.com/symbol/tsla/historical">https://www.nasdaq.com/symbol/tsla/historical</a><br>

The data file I used is stored locally as 'tsla.csv'<br>

## Which Programming Language should I select for this charting job?

Brainstorming, It's a histogram, and based on my experience, 4 languages can do this, but Python wins.

1.  Python's matplotlib, second to none and lots of examples.
2.  R's ggplot2, designed for statistics and data analysis.
3.  Javascript D3js 3rd party graphing plugin with every chart variation under the sun.
4.  Gnu Octave 2D and 3D charting for matrix operations.

Python is advertised heavily to novices and non programmers, however, it's popularity, and the matplotlib data analysis libraries for financial charting is second to none.  Python2.7 gets the job.


## Result Image: 

![Alt text](./final.png?raw=true "so far so good")

## The Python2.7 code that produces the above image:

Open <a href="./month.py">month.py</a>

## What does this data show?  Final Conclusion:

For Tesla, the old adage: "Sell in May and walk away" is not good advice, because based on this histogram, June is a consistently strong month for riding Tesla gains.  These June gains have been almost a trend for the last 10 years, perhaps because Tesla fanboys give their friends rides to the beach, prompting a sales boost in June.  Of course history is no indication of future because the market is zero sum and fluctuations occur based on hedge fund algorithms, not on the stock's performance.  

If anything, the new rule of thumb for Tesla stock trading is: "Buy in May, hold for about a month, catch the Tesla's clockwork June gains, then sell at the end of June.

The purpose of this page is to demonstrate my data charting abilities and my skills in translating that into potentially actionable information. 
