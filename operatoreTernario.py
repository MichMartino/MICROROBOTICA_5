n = int(input("Inserisci un numero -> "))

if n % 2 == 0:
    print(f"{n} è pari")
else:
    print(f"{n} è dispari")

#Operatore ternario
print(f"{n} è {'pari' if n % 2 == 0 else 'dispari'}")

#Anche per dizionari ce lo abbiamo
d = {0: "Pari", 1:"dispari"}
print(f"{n} è {d[n % 2]}")