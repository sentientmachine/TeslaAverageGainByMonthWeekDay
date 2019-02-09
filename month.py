#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n_bins = 5

x = np.random.randn(1000, 3)

# Make a multiple-histogram of data-sets with different length.
fig, ax = plt.subplots(nrows=1, ncols=1)

colors = ['black', 'orange', 'green']

x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]

ax.hist(x_multi, n_bins, histtype='bar', color=colors, label=colors)
ax.legend(prop={'size': 10})
ax.set_title('different sample sizes')

fig.tight_layout()
plt.show()



print("done")
