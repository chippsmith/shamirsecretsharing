import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y1 = 3*x**2 + 2*x + 1  # degree 2 polynomial
y2 = x**3 - 2*x + 1    # degree 3 polynomial

plt.plot(x, y1, label='3x^2 + 2x + 1')
plt.plot(x, y2, label='x^3 - 2x + 1')

plt.title("Example of Polynomial Plots")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()