def distance_toilettes(nb_marches, hauteur_marche):
    hauteur_marche_m = hauteur_marche / 100.0  # Conversion de centimètres en mètres
    nb_marches_total = nb_marches * 2  # Le gardien descend et remonte à chaque fois

    distance_quotidienne = nb_marches_total * hauteur_marche_m
    distance_hebdomadaire = distance_quotidienne * 7

    return distance_hebdomadaire

nb_marches = int(input("Entrer le nombre de marches : "))
hauteur_marche = int(input("Entrer la hauteur de la marche en cm : ")) 

distance_total = distance_toilettes(nb_marches, hauteur_marche)

# Affichage du résultat
print(f"Pour {nb_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_total:.2f} m par semaine.")
