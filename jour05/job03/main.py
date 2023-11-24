# Variable
E = int(input("Veuillez entrer la valeur : "))

# Script toit
for i in range(1, E + 1):
    for j in range(1, E - i + 1):
        print("  ", end="")
    for j in range(1, 2 * i + 1):
        if j == 1:
            print("/ ", end="")
        elif j == 2 * i:
            print('\ ', end="")
        elif i == E:
            print("-", end=" ")
        else:
            print("  ", end="")
    print()
