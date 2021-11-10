liste1 = [2, 2, 0, 1, 6, 5, 8, 3, 3, 3]
liste2 = [2, 2, 3, 7, 0, 3, 9, 0]
# La somme
somme = 0
for i in liste1:
    somme += i
print(f"La somme des element de la liste : {somme}")

# Multiplication
nb = int(input("Saisire un nombre : "))
i = len(liste1)
for j in range(i):
    liste1[j] *= nb
print(liste1)

# Supprition des elements dupliquer
for i in liste1:
    if liste1.count(i) != 1:
        liste1.remove(i)
print(liste1)

# Les valeur commune
commune = []
for i in liste2:
    if i in liste1:
        commune.append(i)
if len(commune) == 0:
    print("Les deux listes n'ont pas des valeur commune !")
else:
    print(f"Les valeur commune entre la liste 1 et la liste 2 sont : {commune}")