import sympy
import random

def polynomial(degree):
    secret = random.randint(1, 1000)
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

def dkg(t, n):
    if not 1 <= t <= n:
        raise ValueError("Threshold t must be in the range [1, n]")

    # Generate participant names
    names = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Kim', 'Liam', 'Mike', 'Nina', 'Olivia', 'Pat', 'Quinn', 'Rachel', 'Sarah', 'Terry', 'Ursula', 'Victor', 'Wendy', 'Xavier', 'Yvonne', 'Zack']
    names += [f"Participant_{i}" for i in range(26, n + 1)]
    names = names[:n]

    print(f"Participants: {names}")

    # Each participant generates a polynomial of degree t - 1
    polynomials = {name: polynomial(t - 1) for name in names}

    for name, poly in polynomials.items():
        print(f"{name}'s Polynomial: {poly.as_expr()}")

    # Each participant generates shares for all the others and themselves using their polynomial
    shares = {name: [(x, evaluate_polynomial(poly, x)) for x in range(1, n + 1)] for name, poly in polynomials.items()}

    for name, share in shares.items():
        print(f"\n{name}'s shares:", share)

    # Initialization of sum_poly has been removed

    while True:
        removed_participant = input("\nPlease select a participant to remove or type 'done' to finish: ")
        removed_participant = removed_participant.capitalize()  # Ensure first letter is capitalized
        if removed_participant == 'Done':
            break
        elif removed_participant not in names:
            print(f"No participant named {removed_participant}. Please try again.")
            continue

        names.remove(removed_participant)
        del shares[removed_participant]

        # Each participant sums their shares to compute a point on the sum polynomial
        points = {name: (i + 1, sum(shares[names[j - 1]][i][1] for j in range(len(names)))) for i, name in enumerate(names)}

        for name, point in points.items():
            print(f"\n{name}'s point on the sum polynomial:", point)

        # The participants pool their points and use Lagrange interpolation to reconstruct the sum polynomial
        sum_points = list(points.values())
        sum_poly = lagrange_interpolation(sum_points)

        print(f"\nReconstructed sum polynomial after removing {removed_participant}: {sum_poly.as_expr()}")
        print(f"Intermediate DKG Secret key (known to no one): {sum_poly.coeffs()[0]}")  # sum_poly.eval(0) would not give you the secret, you should access the constant term of the polynomial

    # Compute sum_poly in case no participant is removed
    if 'sum_poly' not in locals():  # This checks if sum_poly has not been defined in the loop
        points = {name: (i + 1, sum(shares[names[j - 1]][i][1] for j in range(len(names)))) for i, name in enumerate(names)}
        sum_points = list(points.values())
        sum_poly = lagrange_interpolation(sum_points)
    print(f"\nReconstructed sum polynomial: {sum_poly.as_expr()}")
    print(f"\nFinal DKG Secret key (known to no one): {sum_poly.coeffs()[-1]}")


def recover_dkg_secret():
    while True:
        try:
            t = int(input("Enter the threshold number of shares needed to reconstruct the dkg sum polynomial: "))
            if t < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
    shares = []
    for _ in range(t):
        while True:
            try:
                x, y = map(int, input("Enter a point on the sum polynomial as 'x,y': ").split(','))
                shares.append((x, y))
                break
            except ValueError:
                print("Invalid input. Please enter a point as 'x,y'.")
    sum_poly = lagrange_interpolation(shares)
    secret = sum_poly.coeffs()[-1]  # accessing the constant term of the sum_poly
    print(f"Reconstructed dkg sum polynomial: {sum_poly.as_expr()}")
    print(f"Recovered secret: {secret}")

def main():
    while True:
        print("\nPress 1 to execute DKG, 2 to recover DKG secret, or 3 to exit.")
        option = input("Your choice: ")
        if option == '1':
            t = int(input("Enter the threshold t: "))
            n = int(input("Enter the total number n: "))
            dkg(t, n)
        elif option == '2':
            recover_dkg_secret()
        elif option == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()