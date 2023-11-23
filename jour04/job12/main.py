def tri_a_bulles(liste):
    n = 0

    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

ma_liste = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

print("Avant le tri :", ma_liste)

tri_a_bulles(ma_liste)

print("Après le tri :", ma_liste)
