def esTraspas(any):
    if (any % 400 == 0):
        return True
    elif(any % 4 == 0 and any % 100 != 0):
        return True
    return False

list = [1900, 2000, 2016, 1987]

for any in list:
    if (esTraspas(any)):
        print(any , "és de traspàs")
    else:
        print(any , "no és de traspàs")