def paire(liste):
    NbPaire = []
    for i in liste:
        if i % 2 == 0:
            NbPaire.append(i)
    return NbPaire


def impaire(liste):
    NbImpaire = []
    for i in liste:
        if i % 2 != 0:
            NbImpaire.append(i)
    return NbImpaire


l = [2, 2, 0, 1, 6, 5, 8, 3]
print(f"Les nombres paire : {paire(l)} \n Les nombres impaire : {impaire(l)}")