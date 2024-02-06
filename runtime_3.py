import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time

# Define the function to be timed
def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

# Function to time the execution of f(n)
def time_function(n):
    start_time = time.time()
    f(n)
    end_time = time.time()
    return end_time - start_time

# Values of n to test
n_values = np.arange(1, 501)

# Time the function for each value of n
times = np.array([time_function(n) for n in n_values])

# Define the polynomial function
def poly_func(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the curve
popt, _ = curve_fit(poly_func, n_values, times)

# Get coefficients of fitted polynomial
a, b, c = popt

# Find lower bound coefficients
d = a / 2
e = b / 2
f = c / 2

# Find upper bound coefficients
g = 2 * a
h = 2 * b
i = 2 * c

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(n_values, times, label='Data')
plt.plot(n_values, poly_func(n_values, *popt), color='blue', label='Fitted curve: {:.2f}n^2 + {:.2f}n + {:.2f}'.format(*popt))
plt.plot(n_values, poly_func(n_values, g, h, i), color='green', linestyle='--', label='Upper bound: {:.2f}n^2 + {:.2f}n + {:.2f}'.format(g, h, i))
plt.plot(n_values, poly_func(n_values, d, e, f), color='red', linestyle='--', label='Lower bound: {:.2f}n^2 + {:.2f}n + {:.2f}'.format(d, e, f))
plt.xlabel('n')
plt.ylabel('Time')
plt.title('Time vs n for Function f(n)')
plt.legend()
plt.grid(True)
plt.show()

# Analysis of big-O, big-Omega, and big-theta
print("Big-O notation: O(n^2)")
print("Big-Omega notation: Omega(n^2)")
print("Big-theta notation: Theta(n^2)")
