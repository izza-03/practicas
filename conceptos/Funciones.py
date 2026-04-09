

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#argumentos posicionales 
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")#error