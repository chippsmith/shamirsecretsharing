import sympy
import random

def polynomial(secret, degree):
    coeffs = [random.randint(1, 1000) for _ in range(degree)]
    coeffs.append(secret)
    return sympy.Poly(coeffs, sympy.symbols('x'))

def evaluate_polynomial(poly, x):
    return poly.subs(sympy.symbols('x'), x)

def lagrange_interpolation(points):
    x_values, y_values = zip(*points)
    poly = sympy.Poly([0], sympy.symbols('x'))
    for j in range(len(y_values)):
        term = sympy.Poly([y_values[j]], sympy.symbols('x'))
        for m in range(len(x_values)):
            if m != j:
                term *= sympy.Poly([1, -x_values[m]], sympy.symbols('x')) / (x_values[j] - x_values[m])
        poly += term
    return sympy.simplify(poly)

def secret_sharing():
    print("Shamir's Secret Sharing Scheme: Split a secret number into n shares such that "
          "any t of them can be used to reconstruct the secret.")
    secret = int(input("Enter the secret number (between 1 and 1000): "))
    t = int(input("Enter the threshold number of shares needed to reconstruct the secret: "))
    n = int(input("Enter the total number of shares to create: "))
    poly = polynomial(secret, t - 1)
    shares = [(i, evaluate_polynomial(poly, i)) for i in range(1, n + 1)]
    print(f"Polynomial: {poly.as_expr()}")
    print("Shares:", shares)
    return shares

def recover_secret():
    t = int(input("Enter the threshold number of shares needed to reconstruct the secret: "))
    shares = []
    for _ in range(t):
        x, y = map(int, input("Enter a share as 'x,y': ").split(','))
        shares.append((x, y))
    poly = lagrange_interpolation(shares)
    secret = poly.eval(0)
    print(f"Recovered polynomial: {poly.as_expr()}")
    print(f"Recovered secret: {secret}")
    return secret

def main():
    while True:
        print("\nPress 1 to create secret shares, 2 to recover, or 3 to exit.")
        option = input("Your choice: ")
        if option == '1':
            secret_sharing()
        elif option == '2':
            recover_secret()
        elif option == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
