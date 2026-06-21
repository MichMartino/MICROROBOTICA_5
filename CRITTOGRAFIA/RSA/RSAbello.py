import EuclidePrimalità as primalita
import random

def generaChiavi():
    primi = primalita.leggi_primi()
    p = random.choice(primi)
    q = random.choice(primi)
    n = p * q
    m = primalita.mcm(p - 1, q - 1)
    while True:
        c = random.randint(2, m - 1)
        if primalita.mcd_euclide(c, m) == 1:
            break
    while True:
        d = random.randint(2, m - 1)
        if (c*d)%m == 1:
            break
    return p, q, n, m, d, c

def codifica(a,c,n):
    return (a**c)%n

def decodifica(b, d, n):
    return (b**d) %n

def main():
    p, q, n, m, d, c= generaChiavi()
    print(f"chiave privata: {p},{q},{m},{d}")
    print(f"chiave pubblica: {n},{c}")

    messaggio = "ciao"
    messaggio_num = [ord(c) for c in messaggio]
    messaggio_num_codificato = [codifica(x, c, n) for x in messaggio_num]
    print(messaggio_num_codificato)

    messaggio_num_decodificato = [decodifica(x, d, n) for x in messaggio_num_codificato]
    print(messaggio_num_decodificato)

    stringa = "".join([chr(car) for car in messaggio_num_decodificato])
    print(stringa)
if __name__ == "__main__":
    main()