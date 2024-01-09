import time                                 # Importing the time function
import random                           #Importing the random function
from random import randint    #Importing the random integer module from the random function
from tkinter import *

count=0
#---------------------DIFFICULTY SELECTION------------#
difficulty= input ("Difficultly Rating: \n 1- Easy \n 2- Intermediate \n 3- Hard \n Please select a Difficulty: ")
#-------------------- MAKING THE QUESTIONS -----------#
var = (random.randint(0,100))    # Picks out a number between the range
var2 = (random.randint(0,100))  #Picks out another number within the range
arithmetic = "*/+-"
code = random.randint(0,3)        # Selects a random number in the range
arithmetic = arithmetic[code]       #Chooses an operator using the random number
if arithmetic == arithmetic[1]:
  var2 = (random.randint(0,var))
question= (var,arithmetic,var2)   # Creates the qustions using the saved variables
print (count,") What is ", question, "= ")
user_answer= int(input())
                  #-------------DATA VALIDATION---------#
if user_answer != int () or float():
  user_answer= int(input("Incorrect Data Type \n Re-enter the you answer:"))
#-------------------- TIMING FOR THE QUESTIONS ---------#
# This is where the timings for these questions will be decided
if arithmetic == code[1] :
  time.sleep (10)
elif arithmetic == code[2]:
    time.sleep (7)
elif artihmetic == code[3]:
    time.sleep (5)
else:
 time.sleep(5)
#--------------------ANSWER FOR THE QUESTION----------#
if code==0:
  answer= var*var2
elif code==1:
  answer= var/var2
elif code==2:
  answer=var+var2
else:
  answer= var-var2

#---------------------MARKING THE ANSWERS--------------#

if answer != question:
  print ( "Sorry incorrect")
elif answer == question:
  print ("Correct !")
