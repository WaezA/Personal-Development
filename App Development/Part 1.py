import time                                 # Importing the time function
import random                           #Importing the random function
from random import randint    #Importing the random integer module from the random function

count=1
#-------------------- MAKING THE QUESTIONS -----------#
var = (random.randint(0,100))    # Picks out a number between the range
var2 = (random.randint(0,100))  #Picks out another number within the range
arithmetic = "÷x+-"

code = random.randint(0,3)        # Selects a random number in the range
arithmetic = arithmetic[code]       #Chooses an operator using the random number
question= (var,arithmetic,var2)   # Creates the qustions using the saved variables
print (count,") What is ", question, "= ")
user_answer= int(input())

                  #-------------DATA VALIDATION---------#
if user_answer != int () or float():
  user_answer= int(input("Incorrect Data Type \n Re-enter the you answer:"))
