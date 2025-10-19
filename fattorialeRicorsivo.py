n = int(input("Inserisci un numero -> "))

def fattoriale(n):
    if n == 1:
        return 1
    else :
        return n * fattoriale(n - 1)