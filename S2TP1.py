m = 4
n = 4
def saisieMatrice(m, n):
    #initialisation des matrice a 0
    mat = [[0 for i in range(n)] for j in range(m)]

    for i in range(n):
        for j in range(m):
            mat[i][j] = int(input("Saisir l'element mat[{0}][{1}] : ".format(i, j)))


    return mat

print("saisir matrice 1")
mat1 = saisieMatrice(2, 4)