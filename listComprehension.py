#Dato un elenco 1,2,3,4,5 e prenda solo i numeri dispari

lista = [1,2,3,4,5,6,7,8]

q = [num ** 2 for num in lista if num % 2 != 0]
print(q)

#FLAT IS BETTER THAN NETTED, SU PYTHON è SEMPRE MEGLIO AVERE TUTTO SU UNA RIGA SOLA