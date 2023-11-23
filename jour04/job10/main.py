L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
produit = 1

for nombre in L:
    if 90 >= nombre >= 25:
        produit *= nombre

print(f"le produit de toutes les valeurs de la liste comprises dans l'intervalle [25,90] est : {produit}")