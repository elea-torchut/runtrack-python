def dessiner_rectangle(longueur, largeur):
    print("|" + "-" * (longueur - 2) + "|")

    for i in range(largeur - 2):
        print("|" + " " * (longueur - 2) + "|")

    print("|" + "-" * (longueur - 2) + "|")

longueur = int (input("Veillez entrer votre longueur : "))
largeur = int (input("Veillez entrer votre largeur : "))
dessiner_rectangle(longueur, largeur)