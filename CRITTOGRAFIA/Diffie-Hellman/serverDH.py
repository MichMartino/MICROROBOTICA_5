import socket
import random
import EuclidePrimalità as primalita

IP_SERVER = "127.0.0.1"
PORTA_SERVER = 10000
BUFFER = 1024

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP_SERVER, PORTA_SERVER))

    primi = primalita.leggi_primi()
    n = random.choice(primi)
    g = random.randint(1, n-1)
    a = random.randint(1, n-1)
    print(f"numero primo scelto -> {n}")
    print(f"numero maggiore di 1 e minore di n -> {g}")
    print(f"numero segreto di server -> {a}")

    _, indirizzo_mittente = s.recvfrom(BUFFER)
    print(indirizzo_mittente)
    messaggio = f"{n},{g}"

    s.sendto(messaggio.encode(), indirizzo_mittente)
    A = (g**a) % n
    print(f"numero da passare al client (A) -> {A}")

    messaggio = f"{A}"
    s.sendto(messaggio.encode(), indirizzo_mittente)

    messaggio,_ = s.recvfrom(BUFFER)
    B = int(messaggio.decode())
    print(f"numero ricevuto dal client -> {B}")
    key = (B**a) % n
    print(f"Chiave di sessione -> {key}")

if __name__=="__main__":
    main()
        

        

