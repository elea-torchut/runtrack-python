def supprimer_doublons(liste):
    liste_sans_doublons = [] 

    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

print("Avant la suppression des doublons :", ma_liste)

ma_liste_sans_doublons = supprimer_doublons(ma_liste)

print("Après la suppression des doublons :", ma_liste_sans_doublons)
