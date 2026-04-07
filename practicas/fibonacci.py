
a = 0
b = 1
c = 0
for i in range(2,50):
    c = a + b
    b = c
    a = b
    print(f"Serie fibonacci: {a}")