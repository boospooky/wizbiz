from __future__ import division, absolute_import, print_function,\
  unicode_literals
import numpy as np
import matplotlib.pyplot as plt
#######################################
### HW 1
#######################################

#######################################
### Q1
#######################################

#######################################
### 1.c
#######################################
def hill_func(p, x):
    k, a = p
    return ((x)**a) / (k**a + x**a) 
    
# Make a set of evenly spaced points in x
x = np.linspace(0,20.0, 100)

# Compute y
y = hill_func(np.array([7.0, 4.0]), x)

# Plot as dots to verify it was calculated for each value of x
plt.clf()
plt.plot(x, y, 'k.')
plt.grid(True)
plt.margins(x=0.02, y=0.02)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.draw()
plt.show()

