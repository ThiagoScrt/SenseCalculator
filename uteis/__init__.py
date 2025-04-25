Jogoescolhido = []
def Esc_Jogo(num):
    try:
        while True:
            Jogo = int(input(num))
            if Jogo == 1 or 2 or 3 or 4:
                Jogo -= 1
                Jogos = ["CS2", "VALORANT", "APEX", "ARK"] 
                valor = Jogos[Jogo]
                break
            else:
                print('VALOR INVALIDO')
                break
    except(ValueError,TypeError):
        print('\033[31mERROR! Por favor digite um valor valido!\033[m')

    except(KeyboardInterrupt):
        print('\033[31mERROR! Nenhum valor digitado')
        return 0
    else:
        Jogoescolhido.append(valor)

def Sense_jogo1(num):
    Sense = float(input(num))
    while True:
        if Jogoescolhido[0] == "CS2" "APEX":
            Sense = Sense
            break
        elif Jogoescolhido[0] == "VALORANT":
            Sense *= 3.1820
            break
        elif Jogoescolhido[0] == "ARK":
            Sense /= 0.1260
            break
        else:
            break
    while True:
        if Jogoescolhido[1] == "CS2" "APEX":
            Sense = Sense
            break
        elif Jogoescolhido[1] == "VALORANT":
            Sense /= 3.1820
            break
        elif Jogoescolhido[1] == "ARK":
            Sense *= 0.1260
            break
        else:
            break
    
    print(f"Sua sense no jogo {Jogoescolhido[1]} É {Sense:.3f}")
