alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

for i in range(1, len(alphabet)):
    subset = alphabet[:i*2-1]
    repeated_subset = (subset * 2)[:i*2-1]  # Répéter la chaîne et prendre la même longueur que subset
    print(repeated_subset)