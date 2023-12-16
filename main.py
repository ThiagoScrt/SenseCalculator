from uteis import*
Jogo = escjogo('Deseja calcular de CS2 para Valorant ou de Valorant para CS2?\n[1]: CS2 > VALORANT\n[2]: VALORANT > CS2\nEscolha: ')
Sense = float(input(f'Qual sua sense no {Jogo}? :'))
if Jogo == 'CS2':
    print(f'Sua sense no VALORANT é : {Sense/3.18:.3f}')
elif Jogo == 'VALORANT':
    print(f'Sua sense no CS2 é : {Sense*3.18:.3f}')
