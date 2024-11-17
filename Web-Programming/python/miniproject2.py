#Random Password Generator 

import random 
import string
print("------------------Let's start-------------------")
print("Let's generate your random password...")
pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation
password = " "
for i in range(pass_len):
    password += random.choice(charValues)

print("Your password is :", password)

#print(charValues)
#punctuators  %, /, \, -, ?, !
#print(type(string.ascii_letters))          #american standard code for information interchange
#print(string.digits)
#print(string.punctuation)

















#val = random.choice(['a','b','c','d'])
#print(val)