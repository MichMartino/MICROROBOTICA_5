class Gatto:
    #membro statico, condiviso tra tutte le istanze
    numero_gatti = 0

    def __init__(self, nome):
        #Membro di istanza
        self.nome = nome

        Gatto.numero_gatti += 1

    def __str__(self):
        return f"{self.nome}"
    

gatto1 = Gatto("Robbi")
gatto2 = Gatto("Bob")

print(gatto1)
print(gatto2)

print(f"Numero gatti: {Gatto.numero_gatti}")