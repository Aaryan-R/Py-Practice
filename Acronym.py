def fxn(stng):
    lst = stng.split()
    oupt = ""

    for word in lst:
        oupt += word[0]

    oupt = oupt.upper()
    return oupt


inpt1 = "internet of things"

print(fxn(inpt1))

inpt1 = "talk to you later"

print(fxn(inpt1))

inpt1 = "do not disturb"

print(fxn(inpt1))
