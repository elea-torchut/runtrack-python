L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
paire = []
somme = 0

for nombre in L:
    if nombre % 2 == 0:
        paire.append(nombre)

print(paire)

for nombre in paire:
    somme += nombre

print(f"Le resultat de la somme des valeurs paires est de : {somme}")