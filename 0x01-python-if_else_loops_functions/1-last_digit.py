#!/usr/bin/python3
def get_last_digit(number):
    last_digit = abs(number) % 10
    return last_digit if number >= 0 else -last_digit

import random
number = random.randint(-10000, 10000)
last_digit = get_last_digit(number)
if (last_digit > 5):
    print("Last digit of "+str(number)+" is "+str(last_digit)+" and is greater than 5")

elif (last_digit < 6 and last_digit != 0):
    print("Last digit of "+str(number)+" is "+str(last_digit)+" and is less than 6 and not 0")

else:
    print("Last digit of "+str(number)+" is "+str(last_digit)+" and is 0")
