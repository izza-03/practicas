#aprendiendo clases

class persona:
    #si no hacemos uso del def __init__
    pass

p1 = persona #tendriamos que crear una iainstanc del tipo persona 
p1.nombre = "luis"
p1.apellido = "R"

#tendriamos que hacerlo de esta forma ya que no podriamos hacerlo adentro
#en cambio con el init

class persona1: 
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    def greet(self):
        print(f"Hello my name is {self.name}")

p1 = persona1("Luis","R")        

print(p1.name)
print(p1.surname)
p1.greet()