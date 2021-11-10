from math import*
a = float(input("donnez l'entier a  : "))
b = float(input("donnez l'entier b : "))
perimetre = 2 * a + 2 * b
surface = a * b
print(f"le perimetre de rectangle de dimention {a} et {b} egale {perimetre}")
print(f"la surface  de rectangle de dimention {a} et {b} egale {surface}")
if a==b:
    print("le rectangle est un carre")
else:
    print("le rectangle n'est pes un carre")

diametre = sqrt(a **2 + b**2)
print("le diametre egale : %2d"%diametre)
r = float(input("donnez le rayon r : "))
volume_de_cylindre = r*r*pi*a
print(f"le volume de cylindre egale : {volume_de_cylindre}")