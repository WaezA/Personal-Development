print ("Practice Python Exercises")
exercises =["1: Character Input", "2: Odd Or Even", "3: List Less Than Ten", "4: Divisors", "5: List Overlap", "6: String Lists", "7: List Comprehensions", "8: Rock Paper Scissors", "9: Guessing Game One", "10: List Overlap Comprehensions", "11: Check Primality Functions", "12: List Ends", "13: Fibonacci", "14: List Remove Duplicates", "15: Reverse Word Order", "16: Password Generator", "17: Decode A Web Page", "18: Cows And Bulls", "19: Decode A Web Page Two", "20: Element", "21: Write To A File", "22: Read From File", "23: File Overlap", "24: Draw A Game Board", "25: Guessing Game Two", "26: Check Tic Tac Toe", "27: Tic Tac Toe Draw", "28: Max Of Three", "29: Tic Tac Toe Game", "30: Pick Word", "31: Guess Letters", "32: Hangman", "33: Birthday Dictionaries", "34: Birthday Json" ,"35: Birthday Months", "36: Birthday"]

def task_3():
    print (exercises[2])
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    choice = input("Would you to \n 1 - Use to base program \n 2 - Input? \n Anything else - Quit \n Choice: ")
    while choice.isnumeric() == False:
        choice = input("Invalid number entered please re-enter a number:")
        if choice.isnumeric() == True:
            break
        else:
            continue
    if choice == "1":
        for i in range(len(a)):
            if a[i] <=5:
                print(a[i], end=" ")
            else:
                continue
    elif choice == "2":
        number = input("Please enter a number: ")
        while number.isnumeric() == False:
            number = input("Invalid number entered please re-enter a number:")
            if number.isnumeric() == True:
                break
            else:
                continue
        for i in range(len(a)):
            if a[i] <= int(number):
                print(a[i], end=" ")
            else:
                continue
    else:
        quit
        
task_3()