def answer():
    #global allows me to use that specified variable throughout the program
    global answerOne
    answerOne=input('Write a message:')
    #to continue to the next bit of the function
    encrypt()
def encrypt():
    reply= input('Would you like to encrypt your message?')
    if reply=='yes' or 'yh' or 'yeah':
        print ("This is your encrypted message:")
        for i in answerOne:
            #this shows the character with its corresponding ASCII number
            print(chr(ord(i)+5), '=', ord(i)+5)
        print('This is your encrypt message:')
        for i in answerOne:
            # this shows the user only the enctyped letters
            print(chr(ord(i)+5), end= '')
    else:
        print('OK Bye')
        #links all of my functions together
    decrypt()
def decrypt():
    replyTwo= input ('\n Would you like to decrypt?')
    if replyTwo=='yes' or 'yh' or 'yeah':
        print ("This is your decrypted message:")
        for i in answerOne:
            #this shows the original word with the the corresponding ASCII
            print(chr(ord(i)), '=', ord(i))
        # this is the original word
        print(answerOne)
    else:
        print('OK Bye')
#how to print the functions
answer()
