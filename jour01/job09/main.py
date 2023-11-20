nom = "Smartphone XYZ"
prix = 500
quantite = 50

print(f"Nom : {nom}")
print(f"Prix : {prix} $")
print(f"Quantité en stock : {quantite}")

quantite_ajoutee = int(input("Quantité de produits à ajouter en stock : "))
quantite += quantite_ajoutee

quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))

if quantite_achetee <= quantite:
    quantite -= quantite_achetee
    print(f"Vous avez acheté {quantite_achetee} unités. Nouveau stock : {quantite} unités")
else:
    print("Désolé, la quantité demandée n'est pas disponible en stock.")

prix *= 1.10

print(f"Nom : {nom}")
print(f"Prix : {prix} $")
print(f"Quantité en stock : {quantite}")