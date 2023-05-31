
import matplotlib.pyplot as plt
import numpy as np
import random


def lagrange_interpolation(x, y):
    """
    Returns the coefficients of the Lagrange interpolation polynomial
    """
    coeffs = []
    for i in range(len(y)):
        p = [y[i]]
        for j in range(len(x)):
            if i != j:
                p = np.convolve(p, [-x[j], 1])
                p = [c / (x[i] - x[j]) for c in p]
        coeffs.append(p)
    return [sum(c) for c in zip(*coeffs)]

def polynomial(x, coeffs):
    """
    Evaluates the polynomial with the given coefficients at x.
    """
    return sum(coeff * x**power for power, coeff in enumerate(reversed(coeffs)))

secret = 12345678912341234
min_shares = 6
num_shares = 11
coeffs = [random.random() for _ in range(min_shares - 1)]
coeffs.append(secret)


# Create shares
shares = [(x, polynomial(x, coeffs)) for x in range(100, num_shares + 100)]

# Plot the polynomial and the shares
x = np.linspace(0, num_shares + 100, 100)
y = [polynomial(i, coeffs) for i in x]
plt.plot(x, y, label='Polynomial')

share_x, share_y = zip(*shares)
plt.scatter(share_x, share_y, color='red', label='Shares')

plt.legend()
plt.show()
