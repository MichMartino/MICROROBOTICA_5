"""
Esercizio 1: Liste - Filtro e trasformazione prodotti

Descrizione: Data una lista di prezzi di prodotti, filtra quelli sopra una soglia e applica uno
sconto. Restituisci la lista ordinata con i prezzi originali e scontati.

Input di esempio: prezzi = [25.99, 45.50, 12.30, 67.80, 33.25, 89.99], soglia =
30, sconto = 0.15

Output atteso: [(33.25, 28.26), (45.5, 38.68), (67.8, 57.63), (89.99, 76.49)]
"""

prezzi = [25.99, 45.50, 12.30, 67.80, 33.25, 89.99]
soglia = 30
sconto = 0.15

#Ricordo bene, se devo fare list_comprehension...L'ordine è questo: 
#1) COSA RESTITUISCO, INSIEME ALLE OPERAZIONI DA FARE. CICLO + IF
lista_finale = [(prezzo, prezzo - prezzo * sconto) for prezzo in prezzi if prezzo > soglia]
print(lista_finale)

"""
Descrizione: Data una lista di voti di studenti, filtra quelli sopra la sufficienza e applica un bonus. 
Restituisci la lista ordinata con i voti originali e quelli con bonus applicato.
Input di esempio: voti = [16, 22, 15, 28, 19, 25, 30, 14, 21, 27], soglia = 18, bonus = 0.10
Output atteso: [(19, 20.9), (21, 23.1), (22, 24.2), (25, 27.5), (27, 29.7), (28, 30), (30, 30)]
Note: Il voto con bonus non può superare 30.
"""

def filtraSopraSoglia(voti, soglia, bonus):
    lista_soglie = sorted((voto, voto + voto * bonus) for voto in voti if voto > soglia)
    lista_finale = []
    for voto, votoSpeciale in lista_soglie:
        if votoSpeciale > 30:
            votoSpeciale = 30
        nuovaTupla = voto,votoSpeciale
        lista_finale.append(nuovaTupla)
    return lista_finale

voti = [16, 22, 15, 28, 19, 25, 30, 14, 21, 27]
soglia = 18
bonus = 0.10

print(filtraSopraSoglia(voti, soglia, bonus))


