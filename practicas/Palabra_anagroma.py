
def anagroma():
    palabra1,palabra2 = input("Digite 2 cadenas: ").split()

    return "Anagrama" if sorted(palabra1) == sorted(palabra2) else "No anagrama"

print(anagroma())