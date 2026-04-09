#cuenta atras
#recibes un numero para hacer la cuenta atras
#si el numero es = 0 ya esta listo
#si el numero es mayor a 0, que se reste una a una hasta que sea 0




def countdown(n):
    
    if n <= 0:
        print("Listo!")
    else:
        print(n)
        countdown(n-1)

countdown(10)