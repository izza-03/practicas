#excepciones
x = 0
try: 
   print(x)
except NameError:
    print("Variable x its not defined")
finally:
    print("the try except is finished")


if x == 0:
    raise Exception("sorry, variable cannot be 0")
