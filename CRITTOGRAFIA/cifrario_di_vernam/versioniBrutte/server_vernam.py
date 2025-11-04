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
d_inverso = {
    0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 
    9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 
    17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"
}

def decodifica_vernam(cifrato, chiave):
    """Decodifica il messaggio con (c - k) mod N"""
    N = len(d)
    messaggio = []
    
    for c, k in zip(cifrato, chiave): #Zip per accoppiare gli elementi delle due liste e andare quindi in parallelo
        m = (c - k) % N
        messaggio.append(m)
    
    return messaggio

def lista_a_stringa(lista):
    return ''.join([d_inverso[num] for num in lista])

def main():
    nClient = 500
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP_SERVER, PORTA_SERVER))
    s.listen(nClient)
    
    print(f"Server in ascolto su {IP_SERVER}:{PORTA_SERVER}")

    conn, address = s.accept()
    print(f"Connessione accettata da {address}")
    
    #Riceve i dati cifrati
    dati = conn.recv(BUFFER)
    dati_str = dati.decode()
    
    parti = dati_str.split("|")
    cifrato_str = parti[0]
    chiave_str = parti[1]
    
    cifrato = [int(x) for x in cifrato_str.split()]
    chiave = [int(x) for x in chiave_str.split()]
    
    print(f"Messaggio cifrato (numeri): {cifrato}")
    print(f"Chiave (numeri): {chiave}")
    
    #Decodifica il messaggio
    messaggio_numeri = decodifica_vernam(cifrato, chiave)
    messaggio_testo = lista_a_stringa(messaggio_numeri)
    
    print(f"Messaggio decodificato (numeri): {messaggio_numeri}")
    print(f"Messaggio decodificato (testo): {messaggio_testo}")
    print(f"Da: {address}")

    conn.close()
    s.close()

if __name__=="__main__":
    main()
