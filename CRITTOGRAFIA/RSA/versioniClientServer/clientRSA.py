import socket
import RSAbello as rs

IP_SERVER = "127.0.0.1"
PORTA_SERVER = 10000
BUFFER = 1024

def main():
    #Socket TCP del client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Connette al server
    s.connect((IP_SERVER, PORTA_SERVER))
    print("Client connesso al server")
    
    #Invia un qualcosa al server
    messaggio = "Ciao!"
    s.send(messaggio.encode())
    print("messaggio inviato al server")
    
    #Riceve la chiave pubblica dal server
    risposta = s.recv(BUFFER)
    chiave_pubblica = risposta.decode()
    
    print(f"Chiave pubblica: {chiave_pubblica}")

    n,c = chiave_pubblica.split(",")
    n = int(n)
    c = int(c)

    while True:
        messaggio = input("Inserisci messaggio da codificare -> ")
        if messaggio == 'exit':
            #Chiude la connessione
            s.close()
            break
        messaggio_num = [ord(c) for c in messaggio]
        messaggio_num_codificato = [rs.codifica(x, c, n) for x in messaggio_num]
        tosend = ",".join([str(x) for x in messaggio_num_codificato])
        print(tosend)
        s.send(tosend.encode())


if __name__=="__main__":
    main()