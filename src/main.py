import random
import functions

def main():
    inputval = int(input(f"Are you ready for your character? 1= yes, 0 = No: "))

    if inputval == 1:
        print(f"Here is the character you ordered:")
        functions.Character_Race()
        functions.Character_Class()
        functions.Character_Alignment()
        functions.Point_Buy_Randomizer()
    else:
        print("Try again......")

    

main()