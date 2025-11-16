try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    print("What kind of operation do you want to perform?\n"
          "Press + for addition\n"
          "Press - for subtraction\n"
          "Press * for multiplication\n"
          "Press / for division ")
    
    O = input("Enter operation: ")  # keep it as string
    
    match O:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            print(f"The result is: {a / b}")
        case _:
            print("Invalid operation!")
            
except Exception as e:
    print("Enter a valid value of a and b.")