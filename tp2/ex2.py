mois = int(input("Saisir le mois : "))
ListeDeMois31j = [1, 3, 5, 7, 8, 10, 12]
test = bool
if mois in ListeDeMois31j:
    test = True
    print("True")
else:
    print("False")

if test:
    jour = int(input("Saisir le jours : "))
    while jour <= 0 or jour > 31:
        jour = int(input("Saisir le jours : "))

    annee = int(input("Saisir l'annee : "))
    while len(str(annee)) != 4:
        annee = int(input("Saisir l'annee : "))

    print("La date saisie est le", "%02d"%jour, "/", "%02d"%mois, "/", annee)