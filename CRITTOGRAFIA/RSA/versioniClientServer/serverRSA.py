import socket
import RSAbello as rs

IP_SERVER = "127.0.0.1"
PORTA_SERVER = 10000
BUFFER = 1024
nClient = 1

def main():
    p, q, n, m, d, c = rs.generaChiavi()
    print(f"chiave privata: {p},{q},{m},{d}")
    print(f"chiave pubblica: {n},{c}")

    #messaggio = "ciao"
    #messaggio_num = [ord(c) for c in messaggio]
    #messaggio_num_codificato = [rs.codifica(x, c, n) for x in messaggio_num]
    #print(messaggio_num_codificato)

    #messaggio_num_decodificato = [rs.decodifica(x, d, n) for x in messaggio_num_codificato]
    #print(messaggio_num_decodificato)

    #stringa = "".join([chr(car) for car in messaggio_num_decodificato])
    #print(stringa)

    #Socket TCP del server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP_SERVER, PORTA_SERVER))
    s.listen(nClient)  #Mette il server in ascolto
    print(f"Server pronto su {IP_SERVER}:{PORTA_SERVER}")
    #Accetta la connessione dal client
    conn, address = s.accept()
    print(f"Connessione accettata da {address}")
    
    #Riceve messaggio dal client
    messaggio = conn.recv(BUFFER)
    ris = messaggio.decode()
    
    print(f"Ricevuto: {ris}")
    
    #Invia la chiave pubblica
    chiave = f"{n},{c}"
    conn.send(chiave.encode())
    print(f"Chiave pubblica inviata a {address}")

    while True:
        messaggio_numerico_codificato = conn.recv(BUFFER)
        lista_stringhe = messaggio_numerico_codificato.decode().split(",")
        print(lista_stringhe)
        messaggio_num_decodificato = [rs.decodifica(int(x), d, n) for x in lista_stringhe]
        stringa = "".join([chr(car) for car in messaggio_num_decodificato])
        print(stringa)
        if stringa == "exit":
            #Chiude la connessione con questo client
            conn.close()
            break

if __name__ == "__main__":
    main()