import random


def generate(length, capitalLetters=True, smallLetters=True, numbers=True, specialCharacters=True, ):
    if length is None or length < 1:
        return "Bad length"

    if capitalLetters == False and smallLetters == False and numbers == False and specialCharacters == False:
        return "No options"

    password_length = length

    SL = "abcdefghijklmnopqrstuvwxyz"
    CL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NO = "0123456789"
    SC = "!@#$%^&*()?"

    options = [capitalLetters, smallLetters, specialCharacters, numbers]

    characters = [SL, CL, SC, NO]

    if password_length < 4:
        print("Bad length, must be grater than 4")
        return

    max_length = len(SL) + len(CL) + len(NO) + len(SC)

    if password_length > max_length:
        print("Bad length, must be less than: " + str(max_length))
        return

    dev = 0

    for i in range(len(options)):
        if options[i]:
            dev += 1

    el = password_length // dev

    extra = ""

    if (dev * el) != password_length:
        extra = "".join(random.sample(CL, password_length - (el * dev)))

    s = ""

    for j in range(len(options)):
        if options[j]:
            s += "".join(random.sample(characters[j], el))

    password_1 = list(s + extra)
    random.shuffle(password_1)
    scrambled_pass = ''.join(password_1)

    return scrambled_pass
