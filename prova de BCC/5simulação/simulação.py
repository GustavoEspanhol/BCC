import random as rd

faturou = 0
faliu = 0

for i in range(0,1000):

    saldo = 100
    aposta = 20
   
    while saldo > 0 and saldo < 200:

    
        sorteio = rd.randint(1,2)
        print(sorteio)

        if sorteio == 1:
            saldo = saldo+aposta
            print("Ganhou")
        else:
            saldo = saldo-aposta
            print("Perdeu")
    if saldo <= 0:
        faliu += 1
    elif saldo >= 200:
        faturou += 1

print("Faliu", faliu, "vezes")
print("Faturou", faturou, "vezes")
print("Saldo Final: ", saldo)

