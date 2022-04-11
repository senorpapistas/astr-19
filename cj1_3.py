'''This program will run the f_of_x function and
if the return value of the function is greater than 
27, the main function will print out "YAY!"'''

# This is the f_of_x function that will do the math
def f_of_x(x):
    # Saying return here will return the value to the function that called it
    return x**3 + 8

# This is the main function
def main():
    # The if function that will determine if something will be printed or not
    if f_of_x(3) > 27:
        print("YAY!")


if __name__ == '__main__':
    main()