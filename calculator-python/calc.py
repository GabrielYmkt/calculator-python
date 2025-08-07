# Numeric input validation function
def valid_num(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print("Error, please try again by entering numbers only!")


# Loop to allow multiple operations without restarting the program 
while True:
    num1 = valid_num("Enter the first number: ")

    #Loop to prevent the program from closing if the user types the desired operation incorrectly
    while True:
        op = input("Enter the operation to perform (+, -, *, /): ")

        if op != "+" and op != "-" and op != "*" and op != "/":
            print("Invalid option. Type '+' for addition, '-' for subtraction, '*' for multiplication or '/' for division.")

        else:
            break

    # Loop to prevent division by zero and ask for the second number again if dividing
    while True:
        num2 = valid_num("Enter the second number: ")

        if op == "/" and num2 == 0:
            print("Error: division by zero. Please try again")

        else:
            break

    if op == "+":
        result = num1+num2

    elif op == "-":
        result = num1-num2
        
    elif op == "*":
        result = num1*num2

    elif op =="/":
        result = num1/num2
        
    # Check if the result is an integer to hide decimal places (e.g 4.00) 
    if isinstance(result, float) and result.is_integer():
        result = int(result)

    else:
        result = round(result, 2)

    print(f"Result: {result}")

    #Loop to prevent invalid input and ensure the program knows how to proceed
    while True:
        repeat = input("Perform another operation? (y/n) ").lower()
        if repeat == "n" or repeat == "y":
            break

        else:
            print("Invalid option. Type 'y' for yes and 'n' for no.")

    if repeat == "n":
        print("Exiting the program...")
        break