import socket

IP_SERVER = "127.0.0.1"
PORTA_SERVER = 10000
BUFFER = 1024
CHIAVE = "VIVA LA QUINTA A ROBOTICA"

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    dizVern = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
        "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
        "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
        "Y": 24, "Z": 25, " ":26
    }
    dim = len(dizVern)


    dizInv = {v: k for k, v in dizVern.items()}

    while True:
        mess = input("Inserisci il messaggio da cifrare massimo 6 lettere: ").upper()
        daMand = ""
        for i in range(len(mess)):
            valore_cifrato = (dizVern[mess[i]] + dizVern[CHIAVE[i]]) % dim
            daMand += dizInv[valore_cifrato]
    

        #for con lettera in parola

        s.sendto(daMand.encode(), (IP_SERVER, PORTA_SERVER))
        

        risposta, address = s.recvfrom(BUFFER)
        ris = risposta.decode().upper()
        deci = ""

        for i in range(len(ris)):
            valore_plain = (dizVern[ris[i]] - dizVern[CHIAVE[i]]) % dim
            deci += dizInv[valore_plain]
        print(ris)
        print(deci)

if __name__=="__main__":
    main()
