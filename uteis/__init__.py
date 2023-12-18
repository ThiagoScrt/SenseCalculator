Jogoescolhido = {}
def Esc_Jogo(msg):
    try:
        while True:
            Jogo = int(input(msg))
            if Jogo == 1:
                Jogo = 'CS2'
                break
            elif Jogo == 2:
                Jogo = 'VALORANT'
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
        Jogoescolhido['Sense'] = Jogo

def Sense_Jogo(num):
    Sense = float(input(num))
    if Jogoescolhido['Sense'] == 'CS2':
        print(f'Sua sense no VALORANT é : {Sense/3.18:.3f}')
    elif Jogoescolhido['Sense'] == 'VALORANT':
        print(f'Sua sense no CS2 é : {Sense*3.18:.3f}')
    else:
        print('Alguma coisa deu errado!')