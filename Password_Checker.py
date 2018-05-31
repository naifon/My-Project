import re

def check(Password=""):
    upper_case = 0
    lower_case = 0
    number = 0
    symbol = 0

    for i in Password:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        elif i.isdigit():
            number += 1
        else:
            symbol += 1

    if len(Password) <= 6:
        return "This is a weak password  "
    elif upper_case > 0 and lower_case > 0 and number > 0 and symbol > 0:
        return "Good"
    else:
        return "Stil weak, try to use uppercase, lowercase and symbols"