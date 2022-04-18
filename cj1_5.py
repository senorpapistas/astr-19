'''This program will print out a table of sin(x) vs x where x is a floating point number between
0 and 2pi. There will be a thousand entries of x, which results in a thousand prints.'''

# Numpy will be used for creating the x values, pi, and the sin function.
import numpy as np

# This is the main function that will create the table.
def main():
    # This is an empty list that will soon contain all the pairs of x's and sin(x)'s
    tabulation = []
    # We will use the numpy arange() function to create an array of values between 0 and 2pi.
    x_table = np.arange(0, 2 * np.pi + 2 * np.pi/1000, 2 * np.pi / 1000, dtype = float)
    for i in x_table:
        tabulation.append([i, np.sin(i)])
    print("x                      | sin(x)\n-----------------------------------------------")
    # This for-loop with loop through the table and print out the x and sin(x) pair.
    for i in range(len(tabulation)):
        # These prints will be formatted so that the output looks pleasant.
        print(f"{tabulation[i][0]:.20f} | {tabulation[i][1]:.20f}")

if __name__ == '__main__':
    main()