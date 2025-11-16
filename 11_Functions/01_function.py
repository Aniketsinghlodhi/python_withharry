# function definition 
# function help in reusability and modularity in python. 
# Syntax: 
def greet(name):
    return f"Hello, {name}"

print(greet("Aniket" ))

# key points 
# Defineed using def keyword. 
# function should be meaningful .
# use return to send a value back .
   


a = 12
b = 2 
c = 4 

average = (a+b+c)/3
print(average)


a1 = 13 
b1 = 2 
c1 = 1 
average = (a1+b1+c1)/3
# print(average)

def average(a,b,c): # def is keywork , average is variable and inside of ()is parameter 
    d = average = (a+b+c)/3
    # print(d)
    return d # return is used for assigning the any functions for recalling back 

    
b = average(2,3,4)
print(b)
 