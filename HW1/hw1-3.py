from __future__ import division, absolute_import, print_function,\
  unicode_literals
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fn = 'gardner_et_al_2011_time_to_catastrophe_dic.csv'
data = pd.read_csv(fn, comment='#')
data.rename(columns={data.columns[0]: 'lab', data.columns[1]: 'ulab'}, inplace=True)

plt.close('all') # Close open figures

# Plot Labeled histogram
plt.figure('Labeled')
x = data.lab
# Capture histogram information to calculate (x,y) cumulative points
labcounts, binedge = plt.hist(x, bins=max(x), cumulative=True)
# Calculate cumulative distribution (x,y) coordinates
labcenters = (binedge[:-1] + binedge[1:])/2
plt.draw()
plt.show()

# Plot Unlabeled histogram. Same procedure as above.
plt.figure('Unlabeled')
x = data.dropna()['ulab']
ulabcounts, binedge, c = plt.hist(x, bins=max(x), cumulative=True)
ulabcenters = (binedge[:-1] + binedge[1:])/2
plt.draw()
plt.show()

# Plot a mimic of the cumulative distributions seen in the paper
plt.figure('Dot Cumulative')
# Convert counts to 0 to 1 floating points
uNormCounts = ulabcounts / max(ulabcounts)
lNormCounts = labcounts / max(labcounts)
plt.plot(ulabcenters, uNormCounts, 'b.', \
  labcenters, lNormCounts, 'g.')
plt.title('Distribution')
plt.xlabel('Catastrophe time (s)')
plt.ylabel('Cumulative Distribution')
plt.draw()
plt.show()