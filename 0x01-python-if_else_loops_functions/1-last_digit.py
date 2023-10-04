#!/usr/bin/python3
import random


def get_last_digit(number):
    last_digit = abs(number) % 10
    return last_digit if number >= 0 else -last_digit


number = random.randint(-10000, 10000)
last_digit = get_last_digit(number)
str1 = "Last digit of "
str2 = " and is less than 6 and not 0"
if (last_digit > 5):
    print(str1+str(number)+" is "+str(last_digit)+" and is greater than 5")

elif (last_digit < 6 and last_digit != 0):
    print(str1+str(number)+" is "+str(last_digit)+str2)

else:
    print(str1+str(number)+" is "+str(last_digit)+" and is 0")
