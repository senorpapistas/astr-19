''' This program will take in input for 2 floating point numbers and print out the sum, take in
input for 2 integers and print out the difference, and take in a floating point number and
integer and print out the product. It will also print out the datatypes of each output. '''

# This is the main function
def main():
    ''' These variables will contain the user input; each one will print out what type of number
    to input and will then ask for the input'''

    # input takes in user input, the parameter for it prints out a statement before asking for input
    fp1 = float(input("enter a floating point number: "))
    fp2 = float(input("enter another floating point number: "))
    fp1_2 = fp1 + fp2
    # type() will print out the type of the datatype inputted
    print("sum of fp1 and fp2 = ", fp1_2, "\ntype of fp1 + fp2 = ", type(fp1_2), "\n")
    int1 = int(input("enter an integer: "))
    int2 = int(input("enter another integer: "))
    int1_2 = int1 - int2
    print("difference of int1 and int2 = ", int1_2, "\ntype of int1 - int2 = ", type(int1_2), "\n")
    fp3 = float(input("enter one last floating point number: "))
    int3 = int(input("enter one last integer: "))
    fp3_int3 = fp3 * int3
    print("product of fp3 and int3 = ", fp3_int3, "\ntype of fp3 * int3 = ", type(fp3_int3))

if __name__ == '__main__':
    main()