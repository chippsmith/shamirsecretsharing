import numpy as np
import matplotlib.pyplot as plt


def lagrange_polynomial(x_values, y_values):

    def _basis(j):
        return lambda x: np.product([(x - x_values[m]) /
                                     (x_values[j] - x_values[m])
                                     for m in range(k) if m != j])

    assert len(x_values) != 0 and (len(x_values) == len(
        y_values)), "x and y cannot be empty and must have the same length"
    k = len(x_values)

    return lambda x: sum(_basis(j)(x) * y_values[j] for j in range(k))


def get_input():
    x_values = []
    y_values = []

    print("Enter each point as a pair of 'x,y' values. Type 'ok' when you're done.")
    
    while True:
        try:
            user_input = input("Enter a x,y point or type 'ok' to run: ")

            if user_input.lower() == 'ok':
                break

            x, y = map(float, user_input.split(','))

            x_values.append(x)
            y_values.append(y)
        except ValueError:
            print("Please enter the point as 'x,y'.")
    
    return x_values, y_values

def main():
    while True:
        x_values, y_values = get_input()

        # Create the Lagrange polynomial for the given points
        lp = lagrange_polynomial(x_values, y_values)

        # Plot the polynomial
        x_range = np.linspace(-10, 10, num=1000)  # adjust as per your requirement
        plt.plot(x_range, [lp(x) for x in x_range], label='Interpolation')

        # Plot the original points
        plt.scatter(x_values, y_values, color='red', zorder=5, label='Points')
        plt.legend()
        plt.grid(True)

        ax = plt.gca()
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # Plot and annotate y-intercept
        y_intercept = lp(0)
        plt.scatter(0, y_intercept, color='green')  # mark the y-intercept
        plt.annotate(f'y-intercept: {y_intercept}', (0, y_intercept),
                     textcoords="offset points",
                     xytext=(-10, -10),
                     ha='center',
                     color='green')

        plt.savefig('polynomial_interpolation.png')
        print("Plot saved as 'polynomial_interpolation.png'")

        repeat = input("Do you want to run the program again? (Y/N) ")
        if repeat.lower() != 'y':
            break

if __name__ == '__main__':
    main()