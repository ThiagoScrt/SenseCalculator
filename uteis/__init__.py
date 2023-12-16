def escjogo(msg):
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
        return Jogo
