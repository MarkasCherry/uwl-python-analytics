# Seminar 8, Databases and Analytics (CP60056E)
# University of West London
# Assignment 2
# Markas Vysniauskas (21372173)

import numpy as np
import math
from matplotlib import pyplot as plt

# Exercise 1 tasks and outputs:

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

# Exercise 2 tasks and outputs:

print('3rd row of z: ', z[2])
print('4th column of z: ', [dim[4] for dim in z])
print('Mask true, where z[i] > 10: ', z > 10)

z = np.where(z > 10, 5, z)
print('New z = ', z)
print('Sum of each z column: ', np.sum(z, axis=0))
print('Sum of each z row: ', np.sum(z, axis=1))
