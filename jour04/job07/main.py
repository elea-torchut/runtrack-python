L = [8,24,48,2,16]

compteur_multiples_de_3 = 0

for nombre in L:
    if nombre % 3 == 0:
        compteur_multiples_de_3 += 1

print(L)
print(f"Le nombre de multiple de 3 dans la liste est de : {compteur_multiples_de_3}")