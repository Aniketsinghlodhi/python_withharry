# create a list containing the table of 5 

a = 5 
table = []

for i in range (1,11):
    table.append(5*i)

print(table)
#example 01
table = [5*i for i in range (1,11)] # comprehensio way for writing above code in one line 

print(table)

#example 02
squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]