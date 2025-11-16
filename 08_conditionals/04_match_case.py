a = int(input("Enter a number between 1 to 5: "))
match a:
    case 1:
        print("You won a charger.")
    case 2:
        print("You won a camera.")
    case 3:
        print("You won a pen .")
    case 4:
        print("you won a 4$.")
    case 5:
        print("You won a storybook.")
    case _:
        print("Better luck next time.")