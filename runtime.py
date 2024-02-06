import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(n):
    x = 1
    y = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
            y = i + j
    return x

n_values = np.arange(1, 51)
execution_times = []

for n in n_values:
    start_time = time.time()
    f(n)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Plotting
plt.plot(n_values, execution_times, label='Actual Data')

# Fit a quadratic curve to the data
params, _ = curve_fit(quadratic_fit, n_values, execution_times)
fit_curve = quadratic_fit(n_values, *params)

plt.plot(n_values, fit_curve, label='Quadratic Fit', linestyle='--')

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
