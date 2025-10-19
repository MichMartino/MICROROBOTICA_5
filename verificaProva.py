"""
## Esercizio 9: Strutture Annidate - Biblioteca Digitale
**Descrizione:** Gestisci una biblioteca con libri, autori e prestiti. 
Calcola i libri più prestati, trova l'autore più popolare e gestisci le disponibilità.

**Input di esempio:**
```python
biblioteca = {
    "1984": {"autore": "George Orwell", "prestiti": 15, "disponibili": 3},
    "Il Signore degli Anelli": {"autore": "J.R.R. Tolkien", "prestiti": 22, "disponibili": 1},
    "Fondazione": {"autore": "Isaac Asimov", "prestiti": 8, "disponibili": 5},
    "Neuromante": {"autore": "William Gibson", "prestiti": 12, "disponibili": 0},
    "Io, Robot": {"autore": "Isaac Asimov", "prestiti": 18, "disponibili": 2}
}
```

**Output atteso:**
```
Libri più prestati (top 3): [('Il Signore degli Anelli', 22), ('Io, Robot', 18), ('1984', 15)]
Autore più popolare: Isaac Asimov (26 prestiti totali)
Libri non disponibili: ['Neuromante']
Prestiti totali biblioteca: 75
"""

def calcolaPrestiti(biblioteca):
    listaTuplePrestiti = []
    for libro, caratteristica in biblioteca.items():
        for campo, valore in caratteristica.items():
            if campo == "prestiti":
                listaTuplePrestiti.append((libro, valore))
    return sorted(listaTuplePrestiti, key=lambda x:x[1], reverse=True)

def autorePiùFamoso(biblioteca):
    autoreMigliore = ""
    maxPrestiti = 0
    indexAutore = 0
    for libro, caratteristica in biblioteca.items():
        print(libro)
        for campo, valore in caratteristica.items():
            if campo == "prestiti":
                if maxPrestiti < valore:
                    maxPrestiti = valore
                    autoreMigliore = caratteristica
        indexAutore += 1
    return autoreMigliore, maxPrestiti




biblioteca = {
    "1984": {"autore": "George Orwell", "prestiti": 15, "disponibili": 3},
    "Il Signore degli Anelli": {"autore": "J.R.R. Tolkien", "prestiti": 22, "disponibili": 1},
    "Fondazione": {"autore": "Isaac Asimov", "prestiti": 8, "disponibili": 5},
    "Neuromante": {"autore": "William Gibson", "prestiti": 12, "disponibili": 0},
    "Io, Robot": {"autore": "Isaac Asimov", "prestiti": 18, "disponibili": 2}
}

print(calcolaPrestiti(biblioteca)[:3])
print(autorePiùFamoso(biblioteca))