def esPrimer(num):
    for i in range(2, num):
        if (num % i == 0):
            return False    
    return True

for i in range(1, 21):
    if (esPrimer(i)):
        print(i , " és primer")