Sentence = "programming in python is fun"
sum = 0 
vowels = [ "a" , "e" , "i" , "o" ,"u"]

for char in Sentence.lower():
    if (char in vowels):
        sum += 1 
    

print(f"There are {sum} vowels in the sentences ")