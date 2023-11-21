N=int(input("Veuillez rentrer un nombre : "))
i=1
y=1
for i in range(1,N+1):
    print(f"Table de multiplication de {i}")
    for y in range(1,11):
        z=i*y
        print(f"{i} X {y} = {z}")