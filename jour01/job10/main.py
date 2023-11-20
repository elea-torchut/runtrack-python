montant_initial_de_l_investissement = 1000
taux_de_rendement_annuel = 2
gain_annuel = montant_initial_de_l_investissement*taux_de_rendement_annuel/100

print(f"Montant initial de l'investissement: {montant_initial_de_l_investissement} $")
print(f"Taux de rendement annuel: {taux_de_rendement_annuel} %")
print(f"Votre gain annuel s'élève à : {gain_annuel} $")

montant_ajoutee = int(input("Montant à ajouter : "))
montant_initial_de_l_investissement += montant_ajoutee

if montant_ajoutee == 5000:
    taux_de_rendement_annuel += 2
    gain_annuel = montant_initial_de_l_investissement*taux_de_rendement_annuel/100

print(f"Montant de l'investissement: {montant_initial_de_l_investissement} $")
print(f"Taux de rendement annuel: {taux_de_rendement_annuel} %")
print(f"Votre gain annuel s'élève à : {gain_annuel} $")

montant_retire = int(input("Montant à retirer en pourcentage :"))
montant_initial_de_l_investissement -= montant_initial_de_l_investissement*montant_retire/100

if montant_retire == 10:
    taux_de_rendement_annuel -= 1
    gain_annuel = montant_initial_de_l_investissement*taux_de_rendement_annuel/100

print(f"Montant de l'investissement: {montant_initial_de_l_investissement} $")
print(f"Taux de rendement annuel: {taux_de_rendement_annuel} %")
print(f"Votre gain annuel s'élève à : {gain_annuel} $")
