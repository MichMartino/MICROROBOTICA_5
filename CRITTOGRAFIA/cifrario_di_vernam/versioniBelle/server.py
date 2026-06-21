import socket

IP_SERVER = "127.0.0.1"
PORTA_SERVER = 10000
BUFFER = 1024

DIZVERN = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
    "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
    "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
    "Y": 24, "Z": 25, " ":26
}

DIM = len(DIZVERN)
#Dizionario invertito per decodificare
DIZINV = {v: k for k, v in DIZVERN.items()}
CHIAVE = "VIVA LA QUINTA A ROBOTICA"

def codificaDecodifica(messaggio, CHIAVE, isCod = True):
    if isCod:
        segno = 1
    else:
        segno = -1

    deci = ""
    for lettera, letteraCHIAVE in zip(messaggio,CHIAVE): #zip cicla in parallelo
        valore = (DIZVERN[lettera] + segno * DIZVERN[letteraCHIAVE]) % DIM
        deci += DIZINV[valore]
    return deci

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
      
    s.bind((IP_SERVER, PORTA_SERVER))
    print(f"server pronto")

    while True:
        risposta, address = s.recvfrom(BUFFER)
        ris = risposta.decode().upper()

        deci = codificaDecodifica(ris, CHIAVE, False)
        
        print(ris)
        print(deci)

        mess = input("Inserisci il messaggio da cifrare massimo 6 lettere: ").upper()
        daMand = codificaDecodifica(mess, CHIAVE)
        

        s.sendto(daMand.encode(), address)

if __name__ == "__main__":
    main()
