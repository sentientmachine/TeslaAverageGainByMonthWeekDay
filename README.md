
# TeslaAverageGainByMonthWeekDay

Sole author of this project for this writeup, images and code: Eric Leschinski.

Inspired by a snuck glance at a chart from a Bloomberg terminal, I decided to recreate it from first principles in Python2.7 for my favorite company: TSLA.

## I feasted my eyes on this image:

<a href="https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1">
https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1</a><br>

<img border=2 src="https://i0.wp.com/lplresearch.com/wp-content/uploads/2019/01/february-can-be-weak-for-stocks.png?ssl=1" />

It's a histogram with average percentage growth on the vertical and month broken out into 50,20,10 year lookbehind groups, averaged.  It attempts to answer the question: "**Which month is the best month to buy stocks?**"<br>
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

## Actionable information for May of 2019

How to use this analysis to potentially profit in May of 2019: If data I downloaded was correct and the histogram analysis made from it tells a correct story, and if the code doesn't have any mathematical errors in conversion to stacked histogram, and if the greater sentiment and ideology of 2019 keeps with the trend over the last decade, and if the hedge funds aren't using this trend as an elaborate mechanism to trap dumb money into taking the wrong end of their trades...

#### Then:

Load up on Tesla at $235 right now, May 1 through May 15, 2019.  And hold on for about 4 weeks, give or take 2 weeks, and sell it all once all the suited bobbleheads on the big-media screens get to irrational exuberence and say that NOW is the time for YOU to load up on Tesla at $350.  

Revisit from the future: Looks like there's egg on my face because hedge funds see the same thing we see and hammered the stock down to $180.  Double down for next stop $420!

#### Fun commentary:

Corroborating this signal is the hedge funds employing journalists to say that Tesla is dead, April 28 2019: https://www.youtube.com/watch?v=AZRycRUCkdA  When the billionaires are employing journalists to say that Tesla is doomed at 52 week lows, and now is the time to sell your shares to me before it's too late, then it's time to agree with the lie and do the opposite of what they say.  And hope they're not employing a double or triple reverse psychology.


# Revisit from December 18 2019

You can see I'm not fibbing about any of the preceeding paragraphs because the commit history is confirmed by github.

https://www.youtube.com/watch?v=HMuYfScGpbE

Looks like it's time for a wider house.  `:-D`

# Revisit from Sept 2020

hashtag angry noises. 

Hindsight is 2020, Tesla went up to $1500/share before the stock split.

Being $60k long Tesla from 200 to 400 and selling off the last of it at 550.  The world isn't fair, they do forget to teach you that in school.

https://www.youtube.com/watch?v=IW19xASnqw8

# Revisit from Oct 2020

The same stock experts lifted to the media screens, saying why "Tesla is dead" and destined for $17 a share, back when it was $180 in first quarter 2019, are now dressed to the nines with incredibly comforting pastel primary color back drops, and on the horn enumerating 50 masters degree level psychological reasons as to why NOW is the time for you to buy at `$1500` (up from $180 Q1 2019 pre-split).  Post-split equivalent `($60 -> $500)`.  Somehow a beautiful hybrid between a confidance man, a dark triad and an establishment getting a rake turning a blind eye, is what the world's economy is all about in the first place.  
