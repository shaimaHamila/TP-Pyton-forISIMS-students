n = int(input("donnez un emtier superieur a 5 et inferieur a 20 : "))
while (n < 5) or (n > 20):
    n = int(input("donnez un emtier superieur a 5 et inferieur a 20 : "))\


print("figure 1 : ")
for i in range(1, n+1):
    print(i * '* ')


print("figure 2 : ")
for i in range(n, 0, -1):
    print(i * '* ')

print("figure 3 : ")
for i in range(1, n+1):
    v = i * ' *'
    print(v.rjust(2*n))

print("figure 4 : ")
for i in range(n, 0, -1):
    v = i * ' *'
    print(v.rjust(2*n))

print("figure 5 : ")

for i in range(1, n+1):
    alpha = 'abc'*(i//3 + 1)
    print(alpha[0:i])




