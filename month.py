#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time

#1.  Load tsla.csv file

#2.  Have a structure that defines the current lookbehind,  8 through 2 years ago.

#3.  have a structure that gets beginning and end date 2019/01/17 of the group: Month, later (quarter/month/week/day)
#    Feb:  02/01/yyyy through 02/28/yyyy

#3.  Loop over each year, scan over the lookbehind, over the Average the first half and last half of the group
#    calculate gain as (new-old)/old and average over all years

#4.  Plunk that final float value in the below table:


import pandas
csv_delimiter = ','
def open_with_pandas_read_csv(filename):
    df = pandas.read_csv(filename, sep=csv_delimiter)
    data = df.values
    return data

X = open_with_pandas_read_csv("/home/el/bin/TeslaAverageGainByMonthWeekDay/tsla.csv")

#delete the volume column:
X = np.delete(X, [2], 1)

cols = [1, 2, 3, 4]   # columns to calculate average, omit 0 which is date
data = X[:, cols]

avg_col = data.mean(axis=1)

truncate_X = np.delete(X, cols, axis=1)

#Concatenate
X = np.c_[truncate_X, avg_col]

datecol = [0]
data = X[:, datecol]

def getyear(x):
    return x[0][0:4]

#months is ones based in python
def getmonth(x):
    return x[0][5:7]
def getdayofmonth(x):
    return x[0][8:10]

year_col  = np.apply_along_axis(getyear,  1, data)
month_col = np.apply_along_axis(getmonth, 1, data)
day_of_month_col = np.apply_along_axis(getdayofmonth, 1, data)

X = np.c_[year_col, month_col, day_of_month_col, X]
X = np.delete(X, [3], axis=1)


#1.  Delete the first row regardless if it's a header
#2.  Delete the second row if it's an intraday row
#3.  Isolate to only the columns we need:  date, open, high, low, close

#4.  Iterate over every year from 8 to 2  years ago
#5.  Iterate over every month from January to December

def get_price_for_month_year(startpct, endpct, month, year):

    total = 0.0
    rows_in_month = 0

    #I need to know how many rows are in this month:
    rows_in_month = 0.0
    for row in X:
        if str(year) == str(row[0]) and int(month) == int(row[1]):
            rows_in_month += 1

    #print("rows_in_month: '" + str(rows_in_month) + "'")
    #time.sleep(1)

    #throw out months with less than 14 days in it
    if rows_in_month < 16:
        print("month: '" + str(month) + "' and year: '" + str(year) + "' insufficient data")
        return 0.0

    #Filter csv rows by concrete year and concrete month, roughly 20 rows
    count_day = 0
    total_cnt = 0
    for row in X:
        if int(year) == int(row[0]) and int(month) == int(row[1]):
            percent_through_month = float(count_day) / float(rows_in_month)
            #print("percent_through_month: '" + str(percent_through_month) + "'")

            if percent_through_month > startpct and percent_through_month < endpct:
                total += float(row[3])
                total_cnt += 1

            count_day += 1
            #time.sleep(0.1)
            #print(row) 


    #iterate over each row, 

    #If the row is betweeen startpct and endpct then record it

    #get average: of (open, high, low, close) / 4

    #accumulate total and increment counter

    #print("rows_in_month: '" + str(rows_in_month) + "'")
    #print("total: '" + str(total) + "'")
    #time.sleep(0.1)
    try:
        price = float(total) / float(total_cnt)
    except:
        price = 0.0
        print("programmer error, on month: ' " + str(int(month)) + "' year: '" + str(int(year)) + "' this equation should always work")
        #exit()

    return float(price)

def calculate_gain_from_month_and_year(month, year):
    #I know concrete year, concrete month, and I have the csv data in X

    #Jan 2005,


    #woah woah, don't look at this backwards, we're looking at the rows top down 
    #which is present -> past, first means top which means present
    startpct = 0.0
    endpct = 0.3
    last_third = get_price_for_month_year(startpct, endpct, month, year)

    startpct = 0.7
    endpct = 1.0
    first_third  = get_price_for_month_year(startpct, endpct, month, year)

    #month_data is a list of [ date, open, high,  low,  close ]

    #get first 30% of the data
    #get the last 30% of the data
    #Get the gain from the first 3rd averaged and the last 3rd averaged



    #return that
    if (float(first_third) == 0):
        print("There isn't enough data for this year/month")
        return 0

    else:
        print("year: '" + str(year) + "' first_third: '" + str(first_third) + "' last_third: '" + str(last_third) + "' thegain: '" + str( ((last_third - first_third) / first_third)) + "'")
        return ((last_third - first_third) / first_third)



def calculate_gain_from_month_and_year_range(month, year_range):

    #year_range is a list of years to average
    #calculate gain based on month and year_range

    total_gain = 0.0
    total_cnt = 0
    for year in year_range:
        total_gain += calculate_gain_from_month_and_year(month, year)
        total_cnt += 1

    print("month: '" + str(month) + "' year: '" + str(year) + "gain: " + str(total_gain))

    return float(total_gain) / float(total_cnt)


now = datetime.datetime.now()
thisyear = now.year

month_map={
    1 : 'Jan', 
    2 : 'Feb',
    3 : 'Mar',
    4 : 'Apr',
    5 : 'May',
    6 : 'Jun',
    7 : 'Jul',
    8 : 'Aug',
    9 : 'Sep',
    10 : 'Oct',
    11 : 'Nov',
    12 : 'Dec'
}
lookbehind_map={
    9 : '9_yr', 
    8 : '8_yr', 
    7 : '7_yr',
    6 : '6_yr',
    5 : '5_yr',
    4 : '4_yr',
    3 : '3_yr',
    2 : '2_yr'
}

raw_data = {'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        '9_yr':      [4,     2.4,   3.1,    2,      3,     9.0,  2, 3, 4, 5, 6, 7],
        '8_yr':      [4,     2.4,   3.1,    2,      3,     9.0,  2, 3, 4, 5, 6, 7],
        '7_yr':      [2.5,   9.4,   5.7,    6.2,   7.0,    1.0,  2, 3, 4, 5, 6, 7],
        '6_yr':      [2.5,   3.4,   5.7,    6.2,   7.0,    1.0,  2, 3, 4, 5, 6, 7],
        '5_yr':      [2.5,   8.4,  -5.7,    3.2,   1.0,    1.0,  2, 3, 4, 5, 6, 7],
        '4_yr':      [2.5,   9.4,  -5.7,    6.2,   7.0,    5.2,  2, 3, 4, 5, 6, 7],
        '3_yr':      [2.5,   1.4,  -5.7,    0.2,   7.0,    1.0,  2, 3, 4, -5, 6, 7],
        '2_yr':      [5,     4.3,   2.3,    2.3,   5.1,   2.0,   2, 3, 4, 5, 6, 7]}

print("begin the program")
#time.sleep(1)

#months is integer, ones based
for month in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
    #print("looking at month " + str(month))
    #time.sleep(1)

    for year_lookbehind in [9, 8, 7, 6, 5, 4, 3, 2]:

        #print("using year_lookbehind: " + str(year_lookbehind))
        #time.sleep(1)

        total_gain = 0
        counter = 0
        #go from 2 to n years ago
        int_year_range = range(0, year_lookbehind)
        thisyear_list = [thisyear]*len(int_year_range)
        year_range = [a - b for a, b in zip(thisyear_list, int_year_range)]
        
        #print("year_range: '" + str(year_range) + "'")

        gain = calculate_gain_from_month_and_year_range(month, year_range)
        #print("gain: '" + str(gain) + "'")
        #exit()
        #print("month: '" + str(month) + "'")
        #print("gain: '" + str(gain) + "'")
        #print(month_map[int(month)])
        #print(lookbehind_map[int(year_lookbehind)])

        #print(raw_data[lookbehind_map[int(year_lookbehind)]][int(month)-1])
        raw_data[lookbehind_map[int(year_lookbehind)]][int(month)-1] = gain




df = pd.DataFrame(raw_data, columns = ['month', '9_yr', '8_yr', '7_yr', '6_yr', '5_yr', '4_yr', '3_yr', '2_yr'])

pos = list(range(len(df['8_yr'])))
width = 0.10

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with 8_yr data,
# in position pos,
plt.bar(pos,
        df['9_yr'],
        width,
        alpha=0.5,
        color='#FF2919',
        label=df['month'][0])
print(type(plt.bar))

# Create a bar with 8_yr data,
# in position pos,
plt.bar([p + width for p in pos],
        df['8_yr'],
        width,
        alpha=0.5,
        color='#FF3F1E',
        label=df['month'][2])


# Create a bar with 7_yr data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],
        df['7_yr'],
        width,
        alpha=0.5,
        color='#F78F1E',
        label=df['month'][2])

# Create a bar with 6_yr data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos],
        df['6_yr'],
        width,
        alpha=0.5,
        color='#FFC222',
        label=df['month'][3])

# Create a bar with 5_yr data,
# in position pos + some width buffer,
plt.bar([p + width*4 for p in pos],
        df['5_yr'],
        width,
        alpha=0.5,
        color='#FFC233',
        label=df['month'][4])

# Create a bar with 4_yr data,
# in position pos + some width buffer,
plt.bar([p + width*5 for p in pos],
        df['4_yr'],
        width,
        alpha=0.5,
        color='#FAA233',
        label=df['month'][5])

# Create a bar with 3_yr data,
# in position pos + some width buffer,
plt.bar([p + width*6 for p in pos],
        df['3_yr'],
        width,
        alpha=0.5,
        color='#2AA283',
        label=df['month'][6])

# Create a bar with 2_yr data,
# in position pos + some width buffer,
plt.bar([p + width*7 for p in pos],
        df['2_yr'],
        width,
        alpha=0.5,
        color='#2AA2FF',
        label=df['month'][7])

# Set the y axis label
ax.set_ylabel('Gain')

# Set the chart's title
ax.set_title('TSLA average Gain by month over lookbehind')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['month'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*8)

#hardcode height:
#plt.ylim([-0.5, max(df['8_yr'] + df['7_yr'] + df['6_yr'])] )
#plt.ylim([-0.5, 0.7] )
plt.ylim([-0.08, 0.15] )

# Adding the legend and showing the plot
plt.legend(['9 year 2011-2019', '8 year 2012-2019', '7 year 2013-2019', '6 year 2014-2019', '5 year 2015-2019', '4 year 2016-2019', '3 year 2017-2019', '2 year 2018-2019'],
            prop={'size': 16}, loc='upper left')
plt.grid()
plt.show()


print("done")
