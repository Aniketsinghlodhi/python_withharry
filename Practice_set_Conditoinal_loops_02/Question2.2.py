num1 = int(input("enter a first number!"))
num2 = int(input("enter a second number!"))

operation = input("choose operation:")

match operation:
    case "+":
        print(num1+num2)

    case "-":
        print(num1-num2)

    case "*":
        print(num1*num2)

    case "/":
        print(num1/num2)

    case "%":
        print(num1%num2)    
