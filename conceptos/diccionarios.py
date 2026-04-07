#los sets 

myset = {"apple","banana","cherry"}
#no puedes accesar a los valores de un set mediante un index, tampoco 
#aprueban valores repetidos
print(myset)

myset2 = {"apple","banana","apple"}

print(myset2) #al imprimir no repite apple porque no estan permitidos los repetidos
#acceder a los valores de un set
for i in myset:
    print(i)

print("banana" in myset2)     #true

print("banana" not in myset2)#false

myset1 = {"perro","gato","conejo"}

myset1.update(myset)
print(myset1)


