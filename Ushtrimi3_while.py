'''
Ushtrimi 3 me while loop
'''
import random

random_number = random.randint(0,10)

print(random_number)
# i_am_a_loser = True

while i_am_a_loser:
    num = input("Please enter a number ")
    try:
        val = int(num)
        if val == random_number:
            print("U got it")
            i_am_a_loser = False
        else:
            print('Try again')
    except ValueError:
        try:
            float(num)
            print("Input is a float number.")         
        except ValueError:
            print("This is not a number. Please enter a valid number")
     
if i_am_a_loser is not True:
    print('You are a genius!')