ch = input("Saisire une chaine : ")
if not((ch[0] == (ch[0]).upper()) and (ch[-1] == ".")):
    ch = (ch[0]).upper() + ch[1:] + "."

print(ch)
