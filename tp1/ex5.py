n = int(input("donnez un entier n strictemrnt positif et de 4 chiffres: "))
while (n <= 0) or (len(str(n)) > 4):
    n = int(input("donnez un entier n strictemrnt positif et de 4 chiffres: "))

print(f"les nombre parfait inferieur ou egale a {n} sont : ", end=" ")
for nombre in range(1, n+1):
    sommes_diviseur = 0
    for diviseur in range(1, nombre):
       if nombre % diviseur ==0 :
          sommes_diviseur = sommes_diviseur + diviseur

    if sommes_diviseur == nombre:
         print(nombre, end="  ")
