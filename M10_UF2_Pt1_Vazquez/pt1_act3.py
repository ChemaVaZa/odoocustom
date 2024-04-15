list = []
list.append("La Fumiga")
list.append("The Tyets")
list.append("Ginestà")

print(list)

for i in range(0,2):
    list.append(input("Següent element de la llista"))

print(list)

for i in range((len(list))-3, len(list)-1):
    list.pop(i)

print(list)

list.insert(0, "La iaia")

print(list)