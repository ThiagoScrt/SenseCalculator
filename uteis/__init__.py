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
        Sense = Sense/3.18
        print(f'A conversão direta da sua sense do CS2 para o VALORANT seria : {Sense}')
        print(f'Para melhor compatibilidade recomendamos usar a sense : {Sense:.2f}')

    elif Jogoescolhido['Sense'] == 'VALORANT':
        Sense = Sense*3.18
        print(f'A conversão direta da sua sense do VALORANT para o CS2 é : {Sense}')
        print(f'Para melhor compatibilidade recomendamos usar a sense : {Sense:.2f}')

    else:
        print('Alguma coisa deu errado!')
