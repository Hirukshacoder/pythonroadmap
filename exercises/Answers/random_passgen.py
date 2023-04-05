import string
import random

def new_password():
    length_password = int(input("Enter length of password: "))

    password = []
    password_format = ""

    for i in range(length_password):
        password_format += string.ascii_letters
        randomchars = random.choice(password_format)
        password.append(randomchars)
        
    print("".join(password))

app_on = True 
main_page = """
- - - - - - - - - - - - - - - - -
  ~ Random Password Generator ~
                                 
    1. Create New Password   
    2. Quit  
- - - - - - - - - - - - - - - - -
"""
print(main_page)

while app_on:
    select = int(input("Enter an option: \n"))
    if select == 1:
        new_password()
    else:
        app_on = False 
        break