class calculator():
    print("Welcome to the Basic Calculator!\n")

    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    # add funtion :
    def add(self):
        return self.x + self.y

    # subtract funtion :
    def subtract(self):
        return self.x - self.y
    
    # multiply funtion :
    def multiply(self):
        return self.x * self.y
    
    # division function :
    def divide(self):
        if self.y == 0:
            return "Error! Division by zero."
        return self.x / self.y
    def operation(self):
        # Select operation :
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input( "Enter choice (1 or 2 or  3 or 4 or 5): " )

        # Addition
        if self.choice == '1':
            result = add(self.x,self.y)
            print(f"The result of adding {self.x} and {self.y} is {self.result}.")
                
        # Subtraction    
        elif self.choice == '2':
            result = subtract(self.x,self.y)
            print(self.result)
                
        # Multiplication    
        elif self.choice == '3':
            result = multiply(self.x,self.y)
            print(f"The result of multiplying {self.x} and {self.y} is {self.result}.")
                
        # Division    
        elif self.choice == '4':
             result = divide(self.x,self.y)
             print(f"The result of dividing {self.x} by {self.y} is {self.result}.")
                
        # Exit calculator    
        elif self.choice == '5':
             print("Thank you for using the calculator! Goodbye!")
             
        else:
            print("Invalid choice. Please select a valid operation.")
            
calculator()            