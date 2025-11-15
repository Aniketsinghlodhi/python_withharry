# this progam check that whether your password correcr or not . 
password = "Aniket$9301@"
enter_pass = input("Enter password\n:")

while (enter_pass != password):
    enter_pass = input("Wrong password! Try again and Enter password")

print("succes! you are logged in ")