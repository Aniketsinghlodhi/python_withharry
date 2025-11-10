# Walrus operator
# Introduction
# The walrus operator (:=), introduced in Python 3.8, is an assignment expression operator. It allows you to assign a value to a variable within an expression. This can make your code more concise and, in some cases, more efficient by avoiding repeated calculations or function calls. The name "walrus operator" comes from the operator's resemblance to the eyes and tusks of a walrus.

# Use Cases
# Conditional Expressions: The most common use case is within if statements, while loops, and list comprehensions, where you need to both test a condition and use the value that was tested.

def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

# # a = very_slow_func()
# if((a:=very_slow_func())>10):
#     print(a)

# else:
#     print("Its not greater than 10")

while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break 

#     Considerations
# Readability: While the walrus operator can make code more concise, it can also make it harder to read if overused. Use it judiciously where it improves clarity.
# Scope: The variable assigned using := is scoped to the surrounding block (e.g., the if statement, while loop, or list comprehension).
# Precedence: The walrus operator has lower precedence than most other operators. Parentheses are often needed to ensure the expression is evaluated as intended.
