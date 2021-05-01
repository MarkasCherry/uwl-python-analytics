# Seminar 8, Exercise 1, Databases and Analytics (CP60056E)
# University of West London
# Assignment 2
# Markas Vysniauskas (21372173)

import numpy as np
import math
from matplotlib import pyplot as plt

z = np.arange(1, 21, 1).reshape(4, 5)

ls = np.linspace(1, 5, 10)

x = np.linspace(0, 2 * math.pi, 1000)

y = []
for i in x:
    y.append(math.sin(i))


print('Shape of z: ', z.shape)
print('Length of z: ', z.size)
print('10 numbers between 1 - 5: ', ls)
print('Array x: ', x)
print('Array y: ', y)

plt.plot(x, y)
plt.grid()
plt.show()
