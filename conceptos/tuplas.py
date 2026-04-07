#declaracion de una tupla

tupla = (1,2,3)
#las tuplas no pueden ser modificadas una vez son inicializadas
#tupla[0] = 5 #type error

#print(tupla)

#tambien se puede convertir una lista en una tupla con tuple(lista)

lista = [15,4,8]

tupla1 = tuple(lista)

#print(tupla1)


#print(tupla1.index(15))


mitupla = tupla1 + tupla

print(mitupla)