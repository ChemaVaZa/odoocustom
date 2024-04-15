num = int(input("Introdueix l'últim nombre natural per realitzar la suma aritmètica:"))
result = 0

for i in range(1 , num + 1):
    result = result + i

print("La suma aritmètica de " , num , "  és " , result)