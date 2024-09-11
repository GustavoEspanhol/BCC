import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = pow(b,2)-(4*a*c)

if delta < 0:
    print("raizes complexas")
elif delta == 0:
    Raiz = -b + math.sqrt(delta) / 2*a

    raiz = -b - math.sqrt(delta) / 2*a

    print("Raizes: ",Raiz, raiz)
else:
    raiz = -b/ 2*a
    print(raiz)