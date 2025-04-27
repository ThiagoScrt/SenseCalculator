from uteis import*
calculadora = Sensecalculator()
jogo1 = calculadora.Esc_Jogo("Digite o número do seu jogo atual \n[1]: CS2\n[2]: VALORANT\n[3]: APEX LEGENDS\n[4]: ARK\nEscolha : ")
jogo2 = calculadora.Esc_Jogo("Digite o número do jogo para o qual você quer converter a sensibilidade \n[1]: CS2\n[2]: VALORANT\n[3]: APEX LEGENDS\n[4]: ARK\nEscolha : ")
calculadora.Sense_jogo(f"Digite sua sensibilidade no jogo {jogo2}: ")