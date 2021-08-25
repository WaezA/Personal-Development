import random

def start_screen():
    dice_selection = input("Select one of the following options: \n 1- Single Dice \n 2 - Dual Dice \n 3 - Custom Dice Roller \n 4 - Quit \n")
    if dice_selection == "1":
        single_dice()
    elif dice_selection == "2":
        double_dice()
    elif dice_selection == "3":
        custom_dice()
    elif dice_selection == "4":
        quit()
    else:
        print ("Incorrect value entered, please try again : ")
        start_screen()

def single_dice():
    random_value = random.randint(1,6)
    print ("Dice 1 is : ", random_value)

def double_dice():
    for i in range(1,3):
        random_value_i = random.randint(1,6)
        print ("Dice ", i," is : ", random_value_i)
def custom_dice():
    custom_number = input ("Please enter the number of dices you would like random numbers for: ")
    if type(custom_number) != str:
        print("Incorrect value entered please re-enter")
        custom_dice()
    else:
        for i in range(1,(int(custom_number)+1)):
            random_value_i = random.randint(1,6)
            print ("Dice ", i," is : ", random_value_i)

print ("Welcome to Dice Roller ")
start_screen()
