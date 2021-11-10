x = int(input("Saisir x : "))
m = int(input("Saisir m : "))
while len(str(x)) != 2 or m > 10:
    x = int(input("Saisir x : "))
    m = int(input("Saisir m : "))

for i in range(1, m+1):

    print(x, "*", "%02d" % i, "=",  "%03d" % (x * i))

X = int(input("Saisir x : "))
M = int(input("Saisir m : "))
longX = len(str(X))
longM = len(str(M))
for i in range(1, M+1):
    print(X, "*", "%0 longX d" % i, "=",  "%0 longM d" % (X * i))