import random

print ("Practice Python Exercises")
exercises =["1: Character Input", "2: Odd Or Even", "3: List Less Than Ten", "4: Divisors", "5: List Overlap", "6: String Lists", "7: List Comprehensions", "8: Rock Paper Scissors", "9: Guessing Game One", "10: List Overlap Comprehensions", "11: Check Primality Functions", "12: List Ends", "13: Fibonacci", "14: List Remove Duplicates", "15: Reverse Word Order", "16: Password Generator", "17: Decode A Web Page", "18: Cows And Bulls", "19: Decode A Web Page Two", "20: Element", "21: Write To A File", "22: Read From File", "23: File Overlap", "24: Draw A Game Board", "25: Guessing Game Two", "26: Check Tic Tac Toe", "27: Tic Tac Toe Draw", "28: Max Of Three", "29: Tic Tac Toe Game", "30: Pick Word", "31: Guess Letters", "32: Hangman", "33: Birthday Dictionaries", "34: Birthday Json" ,"35: Birthday Months", "36: Birthday"]

def task_5():
    print (exercises[4])
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    c = []
    if len(a) < len(b):
        j =0
        for i in range (len(b)-1):
            if a[j] == b[i]:
                c.append(a[j])
                i +=1
                j +=1
            elif a[j] != b[i]:
                k=0
                while k < len(b):
                    if a[j] == b[k]:
                        c.append(a[j])
                        print(c)
                        k=0
                        break
                    else:
                        k += 1
                        continue
                i +=1
                j +=1
            else:
                i +=1
                j +=1
            if j >=11:
                j=0
        
        
    elif len(a) > len(b):
        print("TBF")
    else:
        print("TBF")    
        
task_5()