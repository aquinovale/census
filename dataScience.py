# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])


import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

mean = df.mean(axis=1)
std = df.std(axis=1)
mean.values


import math
# confidence interval, 1.96 comes from the fact we want 95% confidence interval (z* value)
# http://www.dummies.com/education/math/statistics/how-to-calculate-a-confidence-interval-for-a-population-mean-when-you-know-its-standard-deviation/
confidence = 1.96 * (std.values / math.sqrt(len(df.columns)))
confidence

threshold = 42500

def colorForBar(mean, threshold, confidence):
    if (mean - confidence) <= threshold and (mean + confidence) >= threshold:
        return "white"
    
    if mean < threshold:
        return "blue"
    
    if mean > threshold:
        return "red"
fig, ax = plt.subplots()

colors=[colorForBar(mean.iloc[0], threshold, confidence[0]),
        colorForBar(mean.iloc[1], threshold, confidence[1]), 
        colorForBar(mean.iloc[2], threshold, confidence[2]), 
        colorForBar(mean.iloc[3], threshold, confidence[3])]

ax.axhline(y=threshold, zorder=10, linestyle="--", color="orange")
trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
ax.text(0,threshold, "{:.0f}".format(threshold), color="orange", transform=trans, 
        ha="right", va="center")

ax.bar(range(df.shape[0]), mean, yerr=confidence,
        align='center', color=colors)

ax.set_facecolor("lightgray")

plt.xticks(np.arange(len(df.index)), df.index)

plt.title("Assignment 3, easy option (threshold = {})".format(threshold))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()

