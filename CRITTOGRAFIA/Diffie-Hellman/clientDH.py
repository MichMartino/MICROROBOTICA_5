import socket
import random

IP_SERVER = "127.0.0.1"
PORTA_SERVER = 10000
BUFFER = 1024

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    messaggio = "ciao"
    s.sendto(messaggio.encode(), (IP_SERVER, PORTA_SERVER))
    numeri,_ = s.recvfrom(BUFFER)
    parti = numeri.decode().split(",")
    n = int(parti[0])
    g = int(parti[1])
    print(f"n, il numero primo arrivato dal server -> {n}")
    print(f"numero maggiore di 1 minore di n arrivato dal server-> {g}")
    b = random.randint(1, n-1)
    print(f"il numero segreto del client -> {b}")

    B = (g**b)% n
    print(f"B, numero da passare al server -> {B}")

    numero,_ = s.recvfrom(BUFFER)
    A = int(numero.decode())
    print(f"numero ricevuto dal server (A) -> {A}")
    messaggio = f"{B}"
    s.sendto(messaggio.encode(), (IP_SERVER, PORTA_SERVER))
    key = (A**b)%n
    print(f"Chiave di sessione -> {key}")

if __name__=="__main__":
    main()
