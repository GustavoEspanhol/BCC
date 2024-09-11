import random as rd

escolha = input("cara ou coroa? ")
sorteio = rd.random()
print(sorteio)

if sorteio < 0.5:
    moeda = "cara"
else:
    moeda ="coroa"

if moeda == escolha:
    print("ganhou")
else:
    print("perdeu")
    