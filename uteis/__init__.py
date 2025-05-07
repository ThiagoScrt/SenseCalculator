class Sensecalculator:
    def __init__(self):
        self.Jogoescolhido = []
    def Esc_Jogo(self, num):
        try:
            Jogo = int(input(num))
            if 1 <= Jogo <= 4:
                Jogo -= 1
                Jogos = ["CS2", "VALORANT", "APEX", "ARK"] 
                valor = Jogos[Jogo]  

        except(ValueError,TypeError):
            print('\033[31mERROR! Por favor digite um valor valido!\033[m')

        except(KeyboardInterrupt):
            print('\033[31mERROR! Nenhum valor digitado')
            return 0
        else:
            self.Jogoescolhido.append(valor)
        
    def Sense_jogo(self, num):
        try:
            Sense_inicial = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mERROR! Por favor digite um valor valido para a sensibilidade!\033[m')
            return
        except KeyboardInterrupt:
            print('\033[31mOperação interrompida pelo usuário.')
            return

        Sense = Sense_inicial  # Inicializa Sense com o valor digitado

        if len(self.Jogoescolhido) >= 2:
            jogo_inicial = self.Jogoescolhido[0]
            jogo_final = self.Jogoescolhido[1]

            if jogo_inicial == "VALORANT":
                Sense *= 3.1820
            elif jogo_inicial == "ARK":
                Sense /= 0.1260
            elif jogo_inicial == "APEX" or jogo_inicial == "CS2":
                Sense = Sense

            if jogo_final == "VALORANT":
                Sense /= 3.1820
            elif jogo_final == "ARK":
                Sense *= 0.1260
            elif jogo_inicial == "APEX" or jogo_inicial == "CS2":
                Sense = Sense

            print(f"Sua sense no jogo {jogo_final} É {Sense:.3f}")
        elif len(self.Jogoescolhido) == 1:
            print("Você escolheu apenas um jogo. Execute Esc_Jogo novamente para escolher o segundo jogo para a conversão.")
        else:
            print("Nenhum jogo foi escolhido.")
