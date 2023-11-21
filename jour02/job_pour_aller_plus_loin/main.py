def est_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def type_triangle(a, b, c):
    if a == b == c:
        return "équilatéral"
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "rectangle et isocèle"
        else:
            return "isocèle"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "rectangle"
    else:
        return "quelconque"

# Demander à l'utilisateur les longueurs a, b, c
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Vérifier si les longueurs permettent de construire un triangle
if est_triangle(a, b, c):
    print("Ces longueurs peuvent former un triangle de type", type_triangle(a, b, c))
else:
    print("Ces longueurs ne peuvent pas former un triangle.")