entier = int(input("donner un nombre paire : "))
premier = bool
liste_nb_premier = []

for nombre in range(3, entier):
    premier = 1
    for i in range(2, nombre):
        if nombre % i == 0:
            premier = 0
    if premier == 1:
        liste_nb_premier.append(nombre)

print(liste_nb_premier)

for nb_premier1 in liste_nb_premier:
    for nb_premier2 in liste_nb_premier:
        if nb_premier1 + nb_premier2 == entier:
            print(f" le nombre {entier} est decomposable en deux nombres premiers : {nb_premier1} et {nb_premier2} ")
            break
    break

