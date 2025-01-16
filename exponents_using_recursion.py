
# Exponents using recursion
"""
This application asks the user to enter appropriate numbers for base and exponent before utilizing a recursive method to compute
the outcome of raising a base to an exponent. The application makes sure the user enters proper values for the exponent before
calculating and displaying the result using a straightforward but successful approach.    
    """
def recursive_power(base, exponent):
    
    if exponent == 0: # base case
        return 1
    else:
        return base * recursive_power(base, (exponent - 1))


def main():
    # Request a base and exponent from the user.
    base = int(input("Enter the base: "))
    exponent = int(input("Enter a whole number between 2 and 50: "))
# Validate the exponent input until a valid value is entered
    while exponent < 2 or exponent > 50:
        exponent = int(input("Invalid. Please enter a whole number between 2 and 50: ")) 
    result = recursive_power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}") # Compute the outcome and print it using the recursive power function.
    


if __name__ == '__main__':
    main()
