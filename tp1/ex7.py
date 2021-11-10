
premier = bool
print("les nombre primier inferieur a 100 sont : ")
for nombre in range(3, 100):
    premier = 1
    for i in range(2, nombre):
        if nombre % i == 0:
            premier = 0
    nb = i
    somme = 0
    while nb > 0:
        somme += nb % 10
        nb = nb / 10

    if premier == 1 and somme > 5:
        print(nombre)
