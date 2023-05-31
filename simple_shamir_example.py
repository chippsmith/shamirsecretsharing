
import matplotlib.pyplot as plt
import numpy as np

secret = 5
coeffs = [2, 3, secret]


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

# Create shares
shares = [(x, polynomial(x, coeffs)) for x in range(3)]

'''
print(f"Shares: {shares}")
# Plot the polynomial and the shares
x = np.linspace(0, 6, 100)
y = [polynomial(i, coeffs) for i in x]
plt.plot(x, y, label='Polynomial')

share_x, share_y = zip(*shares)
plt.scatter(share_x, share_y, color='red', label='Shares')

plt.legend()
plt.show()
'''


# Now, let's interpolate using any 2 shares to recover the polynomial
share_x, share_y = zip(*shares[:2])
print(share_x)
print(share_y)
reconstructed_coeffs = lagrange_interpolation(share_x, share_y)
print("Reconstructed polynomial: ")
print_polynomial(reconstructed_coeffs)


