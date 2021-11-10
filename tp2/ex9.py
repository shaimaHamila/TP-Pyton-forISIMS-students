def NotesAuDessusdelaMoyenne(liste):
    l = []
    for i in liste:
        if i >= 10:
            l.append(i)
    return l


notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
print(f"Les notes au-dessus de la moyenne sont : {NotesAuDessusdelaMoyenne(notes)}")
