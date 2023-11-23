def my_long_word(longueur_minimale, chaine):
    mot_actuel = '' 
    resultats = [] 

    for caractere in chaine:
        if caractere.isalpha() or caractere == chaine[-1]:
            mot_actuel += caractere
        else:
            # Utiliser une boucle for pour compter les caractères sans utiliser len
            longueur_mot = 0
            for _ in mot_actuel:
                longueur_mot += 1
            
            if longueur_mot > longueur_minimale:
                resultats.append(mot_actuel)

            mot_actuel = ''

    resultat_final = ' '.join(resultats)
    
    return resultat_final

longueur_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(longueur_minimale, phrase)
print("Output :", resultat)
