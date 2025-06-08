import random
import functions
import lists

def main():
    inputval = int(input(f"Are you ready for your character? 1= yes, 0 = No: "))

    if inputval == 1:
        print(f"\nHere is your random character:\n")
        functions.Character_Race()
        functions.Character_Class()
        functions.Character_Background()
        functions.Character_Alignment()
        functions.Point_Buy_Randomizer()
        print(f'\nNotes for the user:\nThis is a good starting point, feel free to build from here or go your own direction... that is half the fun!')
    else:
        print("Try again......")

    

main()