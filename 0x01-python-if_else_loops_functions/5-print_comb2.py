#!/usr/bin/python3
result = ""
for i in range(100):
    if i < 10 and i >= 0:
        result = "0{}".format(i) + ', '
    elif (i < 99 and i >= 10):
        result = "{}".format(i) + ', '
    else:
        result = "{}".format(i)

    if i != 99:
        print(result, end='')

    else:
        print(result)
