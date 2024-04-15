sou = 0
while (sou <= 0):
    sou = float(input("Introdueix l'import anual:"))
    if (sou < 0):
        print("Introdueix un número vàlid")

if (sou <= 12450):
    irpf = sou * 0.19
elif (sou <= 20200):
    irpf = (sou - 12450) * 0.24 + 12450 * 0.19
elif (sou <= 35200):
    irpf = (sou - 20200) * 0.3 + 12450 * 0.19 + (20200-12450) * 0.24
elif (sou <= 60000):
    irpf = (sou - 35200) * 0.37 + 12450 * 0.19 + (20200-12450) * 0.24 + (35200 - 20200) * 0.3
elif (sou <= 300000):
    irpf = (sou - 60000) * 0.45 + 12450 * 0.19 + (20200-12450) * 0.24 + (35200 - 20200) * 0.3 + (60000 - 35200) * 0.45
else:
    irpf = (sou - 300000) * 0.47 + 12450 * 0.19 + (20200-12450) * 0.24 + (35200 - 20200) * 0.3 + (60000 - 35200) * 0.45 + (300000 - 60000) * 0.45

round(irpf, 2)

print("La taxa d'IRPF és :", irpf)