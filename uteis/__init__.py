def escjogo(msg):
    try:
        while True:
            n = int(input(msg))
            if n == 1:
                jogo = 'CS2'
                break
            elif n == 2:
                jogo = 'VALORANT'
                break
            else:
                print('VALOR INVALIDO')
    except(ValueError,TypeError):
        print('\033[31mERROR! Por favor digite um valor valido!\033[m')
    except(KeyboardInterrupt):
        print('\033[31mERROR! Nenhum valor digitado')
        return 0
    else:
        return jogo
