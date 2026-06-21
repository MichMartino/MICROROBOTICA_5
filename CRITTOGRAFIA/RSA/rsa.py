def calcola_mcm(a, b):
    mcd = calcola_MCD(a, b)
    return a*b/mcd

def calcola_MCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


p = 5
q = 7

n = p*q
m = int(calcola_mcm(p-1, q-1))

for i in range(2, m):
    if calcola_MCD(i, m) == 1:
        c = i
        break

for i in range(0, m):
    if (c*i)%m == 1:
        d = i
        break

messaggio = input("Inserisci un messaggio da criptare -> ")
lista = []
for car in messaggio:
    car_ascii = ord(car)
    print(car_ascii)
    b = (car_ascii*c)%n
    lista.append(b)


lista_ascii = []
for b in lista:
    lista_ascii.append((b**d)%n)
print(lista_ascii)

for car in lista_ascii:
    print(car)