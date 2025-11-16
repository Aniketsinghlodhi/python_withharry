def sum(a,b):
    print("hey i am summing")
    c = a+b
    global z # please modified global z 
    z = 0 # this will refer to global and not create local variable 
    return c
z = 3 
print(sum(4,4))
print(z)
# This allows functions to change global variables, but excessive use of global is discouraged as it can make debugging harder.