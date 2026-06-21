import math

def mcd_euclide(a, b):
    #Divido il primo per il secondo, e poi il secondo per il resto..
    #Scambio per non dividere un numero piccolo per un numero più grande
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
        #print(a)
        #print(b)
    return a

def mcm(a, b):
    return a * b // mcd_euclide(a, b)

def leggi_primi():
    with open("./numeri_primi.txt", "r") as f:
        return [int(riga.strip()) for riga in f.readlines()]


def e_primo(n):
    #tolgo casi base
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    #Arrivo come limite fino alla radice del numero che sto cercando
    limite = int(math.sqrt(n)) + 1 #SI può fare anche con la potenza
    #Con l'algoritmo di Euclide controllo se quel divisore è in comune...
    #Nessuna divisione deve avere resto 0!
    for k in range(3, limite):
        if n % k == 0:
            return False
    
    return True

if __name__=="__main__":
    with open("./numeri_primi.txt", "w") as file: #O lo faccio con with o con file.open
        for n in range(1000, 10000):
            if e_primo(n):
                file.write(f"{n}\n")

