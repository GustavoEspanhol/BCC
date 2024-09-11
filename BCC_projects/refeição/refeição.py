s = "sim"
n = "não"


  refeição = input("Voce quer almoçar?")

  if refeição == s:
    opções = input("Opcoes: carne, frango, vegetariano")
    if opções == 'carne':
        ponto = input("Qual o ponto da carne?")
        if ponto == 'bem passado':
            print("Bife bem passado saindo")
        elif ponto == 'mal passado':
            print("Bife vermelho saindo")
        else:
            break
    elif opções == 'frango' or 'vegetariano':
        print("Nenhum bife saindo")
    else:
        break      
  if refeição == n:
    return refeição
  else:
    print("sim ou não apenas")


  bebida = input("Voce quer beber?") 
