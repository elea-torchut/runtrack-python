def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    
    for lettre in message:
        if lettre.isalpha():  # Vérifier si la caractère est une lettre
            if lettre.islower():
                nouvelle_lettre = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))
            elif lettre.isupper():
                nouvelle_lettre = chr((ord(lettre) - ord('A') + decalage) % 26 + ord('A'))
        else:
            nouvelle_lettre = lettre  # Conserver les caractères non alphabétiques tels quels
        
        message_chiffre += nouvelle_lettre
    
    return message_chiffre

# Exemple d'utilisation
message_original = input("Entrer votre message : ")
decalage = int(input("Entrer le nombre de rang : "))
message_chiffre = chiffrement_cesar(message_original, decalage)
print("Message original :", message_original)
print("Message chiffré :", message_chiffre)
