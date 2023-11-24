def afficher_tapis(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                print("+ ", end="")
            elif i == 0 and j == n:
                print("+ ", end="")
            elif i == n and j == 0:
                print("+ ", end="")
            elif i == n and j == n:
                print("+ ", end="")
            elif i == 0 or i == n:
                print("- ", end="")
            elif j == 0 or j == n :
                print("|",end=" ")
            elif i + j == n:
                print("  ", end="")
            elif i == j:
                print("# ", end="")
            else:
                print("# ", end="")
        print()

# Saisie utilisateur avec vérification
while True:
    try:
        taille = int(input("Veuillez entrer la taille du tapis : "))
        break  # Sortir de la boucle si la conversion en entier est réussie
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Exemple d'utilisation
afficher_tapis(taille)