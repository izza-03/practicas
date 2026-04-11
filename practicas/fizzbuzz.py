#if a number is multiple of 3 print fizz
#if a number is multiple of 5 print buzz
#if both fizz buzz
number = 0

def fizzbuzz(number):
    if(number %3 == 0 & number %5 == 0):
        print("fizzbuzz")
    elif number %3 == 0:
        print("Fizz")
    elif number %5 == 0:
        print("buzz")
   

try:
    number = int(input("Digite un numero"))
except: 
    print("Digit a integer")

fizzbuzz(number)