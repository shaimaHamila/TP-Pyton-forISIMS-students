entier = int(input("Entrez un nombre decimal: "))
print(f"{entier} vaut en binaire {bin(entier)} , en octale {oct(entier)} , en hexadecimal {hex(entier)}")
ch = input("Saisire une chaine : ").split("*")
for i in ch:
    print(chr(int(i)))




""""
def conversion(n):
    if n > 1:
        conversion(n // 2)
    print(n % 2, end='')


# Demande à l'utilisateur d'entrer un nombre
nbr = int(input("Entrez un nombre decimal: "))

conversion(nbr)
"""