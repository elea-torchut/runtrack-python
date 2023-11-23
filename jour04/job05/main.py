L = [1,2,3,4,5]

def somme():
    L[3] = L[2] + L[4]
    return L

print(L)
print(L[1])
print(somme())
print(L[4])