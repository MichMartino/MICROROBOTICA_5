import socket

IP_SERVER = "127.0.0.1"
PORTA_SERVER = 10000

BUFFER = 4096

#Dizionario alfabeto
d = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, 
    "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, 
    "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}

def stringa_a_numeri(testo):
    return [d[char] for char in testo.upper()]

def codifica_vernam(messaggio, chiave):
    """Codifica il messaggio con (m + k) mod N"""
    N = len(d)
    cifrato = []
    
    for m, k in zip(messaggio, chiave):#Vado in parallelo con le due liste
        c = (m + k) % N
        cifrato.append(c)
    
    return cifrato

def main():
    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl.connect((IP_SERVER, PORTA_SERVER))
    
    msg = "ACCIDENTI"
    chiave_str = "CHIAVELUNGA"
    
    #Converte in numeri
    messaggio_numeri = stringa_a_numeri(msg)
    chiave_numeri = stringa_a_numeri(chiave_str)
    
    #Codifica
    cifrato = codifica_vernam(messaggio_numeri, chiave_numeri)
    
    print(f"Messaggio originale: {msg}")
    print(f"Messaggio (numeri): {messaggio_numeri}")
    print(f"Chiave (testo): {chiave_str[:len(msg)]}")
    print(f"Chiave (numeri): {chiave_numeri[:len(msg)]}")
    print(f"Messaggio cifrato (numeri): {cifrato}")
    
    cifrato_str = ' '.join([str(num) for num in cifrato])
    chiave_str_numeri = ' '.join([str(num) for num in chiave_numeri[:len(msg)]])
    
    dati_da_inviare = cifrato_str + "|" + chiave_str_numeri
    
    cl.send(dati_da_inviare.encode())

    cl.close()

if __name__=="__main__":
    main()
