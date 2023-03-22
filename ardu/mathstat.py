# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# the two give the same results
print(scipy.special.binom(10, 5))

# Creating vectors X and Y

# Show the plot
a = np.array([8, 4, 5, 4, 2, 15, 1, 6])
aver = np.average(a)
x = np.linspace(0, 20, 100)
y = np.exp(-x*(1/aver))
y2 = x/a.size
fig = plt.figure(figsize=(10, 5))

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
