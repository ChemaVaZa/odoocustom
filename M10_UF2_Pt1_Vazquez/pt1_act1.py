num1 = int(input("Numero 1"))
num2 = int(input("Numero 2"))

num3 = num1/num2

if (num3 % 1 == 0):
    print("Dividend: ", num1)
    print("Divisor: ", num2)
    print("Resultat: ", num3)
    print(num3," és enter")
else:
    num4 = num1 % num2
    print("Dividend: ", num1)
    print("Divisor: ", num2)
    print("Resultat: ", num3)
    print(num3," no és enter")
    print("Residu: ", num4)