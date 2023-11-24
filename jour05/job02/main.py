# Variables
L = int(input("Veuillez entrer la longueur : "))
C = int(input("Veuillez entrer la largeur : "))

# Script carré
for i in range(L):
    for j in range(C):
        if i == 0 or i == L - 1:
            print("-", end=" ")
        elif j == 0 or j == C - 1:
            print("|", end=" ")
        else:
            print(" ", end=" ")
    print()
