# add function :
def add(x, y):
    return x + y

# subtract funtion :
def subtract(x, y):
    return x - y

# multiply funtion :
def multiply(x, y):
    return x * y

# division function :
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    
    print("Welcome to the Basic Calculator!\n")
    
    while True:
        # Select operation :
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input( "Enter choice (1 or 2 or  3 or 4 or 5): " )

        if choice in ['1', '2', '3', '4']: 
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Addition
            if choice == '1':
                result = add(num1, num2)
                print(f"The result of adding {num1} and {num2} is {result}.")
                
            # Subtraction    
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result of subtracting {num2} from {num1} is {result}.")
                
            # Multiplication    
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result of multiplying {num1} and {num2} is {result}.")
                
            # Division    
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of dividing {num1} by {num2} is {result}.")
                
            # Exit calculator    
        elif choice == '5':
             print("Thank you for using the calculator! Goodbye!")
             break
        
    else:
        print("Invalid choice. Please select a valid operation.")
            
calculator()            