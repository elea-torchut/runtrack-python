def tri_a_bulles(liste):
    n = 0

    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

def arrondir_nombres(liste):
    i = 0
    try:
        while True:
            liste[i] = int(liste[i] + 0.5)
            i += 1
    except IndexError:
        pass
    
liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("Avant arrondi et tri :", liste_nombres)

arrondir_nombres(liste_nombres)

tri_a_bulles(liste_nombres)

print("Après arrondi et tri :", liste_nombres)
