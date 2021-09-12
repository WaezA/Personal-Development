import random

print ("Practice Python Exercises - https://www.practicepython.org/")
exercises =["1: Character Input", "2: Odd Or Even", "3: List Less Than Ten", "4: Divisors", "5: List Overlap", "6: String Lists", "7: List Comprehensions", "8: Rock Paper Scissors", "9: Guessing Game One", "10: List Overlap Comprehensions", "11: Check Primality Functions", "12: List Ends", "13: Fibonacci", "14: List Remove Duplicates", "15: Reverse Word Order", "16: Password Generator", "17: Decode A Web Page", "18: Cows And Bulls", "19: Decode A Web Page Two", "20: Element", "21: Write To A File", "22: Read From File", "23: File Overlap", "24: Draw A Game Board", "25: Guessing Game Two", "26: Check Tic Tac Toe", "27: Tic Tac Toe Draw", "28: Max Of Three", "29: Tic Tac Toe Game", "30: Pick Word", "31: Guess Letters", "32: Hangman", "33: Birthday Dictionaries", "34: Birthday Json" ,"35: Birthday Months", "36: Birthday"]
print (exercises)

def task_1():
    print (exercises[0])
    name = input("Please enter your name: ")
    name = (name.lower()).capitalize()
    if name.isalpha() != True:
        re_enter_name = input("Incorrect characters entered please re-enter: ")
        while re_enter_name.isalpha() == False:
            re_enter_name = input("Incorrect characters entered please re-enter: ")
            if re_enter_name.isalpha() == True:
                name = (re_enter_name.lower()).capitalize()
                break
    else:
        age = input("Please enter your age you will be this year: ")
        if age.isnumeric() != True:
            re_enter_age = input("Incorrect characters entered please re-enter: ")
            while re_enter_age.isnumeric() == False:
                re_enter_age = input("Incorrect characters entered please re-enter: ")
                if re_enter_age.isnumeric() == True:
                    age = re_enter_age
                    break   
        conversion = (2021 - int(age)+100)
    
    print(name,"You will be 100 years in the year",conversion)

def task_2():
    print (exercises[1])
    num = input("Please enter a number : ")
    while num.isnumeric() != True:
        num = ("Number incorrectly entered. Please re-enter a number : ")
        if num.isnumeric() == True:
            num = int(num)
            break
    num =int(num)
    check = input("Enter a Check number :")
    while check.isnumeric() != True:
        check = ("Number incorrectly entered. Please re-enter a number : ")
        if check.isnumeric() == True:
            check = int(check)
            break
    check = int(check)
    
    if num%2 == 0:
        print("Number",num,"is even")
    elif num%2 == 1:
        print("Number",num,"is odd")
    if num%4 == 0:
        print("Number",num,"is also multiple of 4")
    if num%check == 0:
        print("Number",num,"is divisible by ",check)

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

def task_4():
    print (exercises[3])
    mod = input("Enter a number: ")
    factors = list()
    for i in range (int(mod)+1):
        factors.append(int(i))
        i += 1
    factors.remove(0)
    print ("Factors for " + mod + " are:")
    
    for i in range (int(mod)):
        if (int(mod)%int(factors[i])) ==0:
            print (factors[i])
            i += 1
        else:
            i += 1
            continue
        
def task_5():
    print (exercises[4])

def task_6():
    print (exercises[5])

def task_7():
    print (exercises[6])

def task_8():
    print (exercises[7])

def task_9():
    print (exercises[8])

def task_10():
    print (exercises[9])

def task_11():
    print (exercises[10])

def task_12():
    print (exercises[11])

def task_13():
    print (exercises[12])

def task_14():
    print (exercises[13])

def task_15():
    print (exercises[14])

def task_16():
    print (exercises[15])

def task_17():
    print (exercises[16])

def task_18():
    print (exercises[17])

def task_19():
    print (exercises[18])

def task_20():
    print (exercises[19])

def task_21():
    print (exercises[20])

def task_22():
    print (exercises[21])

def task_23():
    print (exercises[22])

def task_24():
    print (exercises[23])

def task_25():
    print (exercises[24])

def task_26():
    print (exercises[25])

def task_27():
    print (exercises[26])

def task_28():
    print (exercises[27])

def task_29():
    print (exercises[28])

def task_30():
    print (exercises[29])

def task_31():
    print (exercises[30])

def task_32():
    print (exercises[31])

def task_33():
    print (exercises[32])

def task_34():
    print (exercises[33])

def task_35():
    print (exercises[34])

def task_36():
    print (exercises[35])
