from uteis import*
j = escjogo('Deseja calcular de CS2 para Valorant ou de Valorant para CS2?\n[1]: CS2 > VALORANT\n[2] VALORANT > CS2\n: ')
s = float(input(f'Qual sua sense no {j}? :'))
if j == 'CS2':
    print(f'Sua sense no VALORANT é {s/3.18:.3f}')
elif j == 'VALORANT':
    print(f'Sua sense no CS2 é {s*3.18:.3f}')
