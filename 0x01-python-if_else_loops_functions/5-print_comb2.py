#!/usr/bin/python3
for i in range(99):
    if i < 10 and i >= 0:
        print("0"+str(i), end=', ')
    elif(i < 98 and i >= 10):
        print(str(i), end=', ')
    else:
        print(str(i))
