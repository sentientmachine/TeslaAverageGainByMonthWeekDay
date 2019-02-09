#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np





raw_data = {'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        '8_yr':      [4,     24,   31,      2,     3,     90,  2, 3, 4, 5, 6, 7],
        '7_yr':      [25,    94,   57,      62,    70,    100, 2, 3, 4, 5, 6, 7],
        '6_yr':      [25,    94,   57,      62,    70,    100, 2, 3, 4, 5, 6, 7],
        '5_yr':      [25,    94,  -57,      62,    70,    100, 2, 3, 4, 5, 6, 7],
        '4_yr':      [25,    94,  -57,      62,    70,    100, 2, 3, 4, 5, 6, 7],
        '3_yr':      [25,    94,  -57,      62,    70,    100, 2, 3, 4, -5, 6, 7],
        '2_yr':      [5,     43,   23,      23,     51,   110, 2, 3, 4, 5, 6, 7]}

df = pd.DataFrame(raw_data, columns = ['month', '8_yr', '7_yr', '6_yr', '5_yr', '4_yr', '3_yr', '2_yr'])

pos = list(range(len(df['8_yr']))) 
width = 0.10
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with 8_yr data,
# in position pos,
plt.bar(pos, 
        df['8_yr'], 
        width, 
        alpha=0.5, 
        color='#EE3224', 
        label=df['month'][0]) 


# Create a bar with 7_yr data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        df['7_yr'],
        width, 
        alpha=0.5, 
        color='#F78F1E', 
        label=df['month'][1]) 

# Create a bar with 6_yr data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        df['6_yr'], 
        width, 
        alpha=0.5, 
        color='#FFC222', 
        label=df['month'][2]) 

# Create a bar with 5_yr data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos], 
        df['5_yr'], 
        width, 
        alpha=0.5, 
        color='#FFC233', 
        label=df['month'][3]) 

# Create a bar with 4_yr data,
# in position pos + some width buffer,
plt.bar([p + width*4 for p in pos], 
        df['4_yr'], 
        width, 
        alpha=0.5, 
        color='#FAA233', 
        label=df['month'][4]) 

# Create a bar with 3_yr data,
# in position pos + some width buffer,
plt.bar([p + width*5 for p in pos], 
        df['3_yr'], 
        width, 
        alpha=0.5, 
        color='#BAA233', 
        label=df['month'][5]) 

# Create a bar with 2_yr data,
# in position pos + some width buffer,
plt.bar([p + width*6 for p in pos], 
        df['2_yr'], 
        width, 
        alpha=0.5, 
        color='#FAA2FF', 
        label=df['month'][6]) 

# Set the y axis label
ax.set_ylabel('Gain')

# Set the chart's title
ax.set_title('TSLA average Gain by month over lookbehind')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['month'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)


#hardcode height:
plt.ylim([-100, max(df['8_yr'] + df['7_yr'] + df['6_yr'])] )


# Adding the legend and showing the plot
plt.legend(['8 year', '7 year', '6 year', '5 year', '4 year', '3 year', '2 year', '1 year'], loc='upper left')
plt.grid()
plt.show()


print("done")
