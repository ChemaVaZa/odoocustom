import getpass
import os
import re
import crypt
fo = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./dades.txt"), "a+")

usuari = "_"
#while (usuari.isalnum() == False):
while (re.match("^[a-z0-9]+$", usuari, 0) == None):
    usuari = input("Usuari:")

contrasenya = "_"
while (contrasenya.isalnum() == False):  
    contrasenya = getpass.getpass("Contrasenya:")

salt = crypt.mksalt(crypt.METHOD_SHA512)
hashed_password = crypt.crypt(contrasenya, salt)

str = "\n" + usuari + ":" + hashed_password
fo.write(str)

fr = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./dades.txt"), "r+")
str = fr.read()
print("Usuaris:\n",str)
print("No puc utilitzar la llibreria stdiomask")
fr.close()
fo.close()