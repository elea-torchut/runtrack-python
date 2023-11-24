def my_sort(my_list):
    sorted_list = my_list.copy()  # Copie de la liste pour ne pas modifier l'originale
    n = len(sorted_list)
    coups = 0  # Initialisation du nombre de coups

    # Boucle jusqu'à ce que la liste soit triée
    while True:
        sorted_flag = True  # Drapeau pour vérifier si la liste est triée à chaque itération
        for i in range(n - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                # Échange d'éléments adjacents
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                sorted_flag = False  # La liste n'est pas encore triée
                coups += 1  # Incrémentation du nombre de coups

        if sorted_flag:
            # La liste est triée, sortie de la boucle
            break

    # Affichage du nombre total de coups
    print(f"Nombre total de coups nécessaires pour trier la liste : {coups}")

    return sorted_list

# Exemple d'utilisation
liste_non_triee = [4, 2, 7, 1, 9, 5]
liste_triee = my_sort(liste_non_triee)
print("Liste triée :", liste_triee)
