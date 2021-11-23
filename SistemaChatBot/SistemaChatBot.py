from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Bom dia, bem vindo ao sistema de chatbots da empresa {self.empresa}!\n')

    def mostra_menu(self):
        print('Bots disponíveis:')
        for i,bot in enumerate(self.lista_bots):
            print(f'{i} - Bot: {bot.nome} - Apresentação: ', end='')
            bot.apresentacao()
        print()

    
    def escolhe_bot(self):
        while True:
            escolha = input('Digite o numero do bot desejado: ')
            try: escolha = int(escolha)
            except: escolha=-1
            if escolha >= 0 and escolha < len(self.lista_bots):
                self.bot = self.lista_bots[escolha]
                break
            else: print('Escolha inválida')

    def mostra_comandos_bot(self):
        self.bot.mostra_comandos()
        print()

    def le_envia_comando(self):
        while True:
            escolha = input('Digite o numero do comando desejado (ou -1 para sair): ')
            try: escolha = int(escolha)
            except: escolha=-2
            if escolha >= 0 and escolha < len(self.bot.comandos):
                self.bot.executa_comando(escolha)
                return False
            elif escolha == -1:
                return True
            else: print('Escolha inválida')

    def inicio(self):
        self.boas_vindas() #mostra a tela de boas vindas
        self.mostra_menu() #mostra o menu com os bots disponiveis
        self.escolhe_bot() #o usuario escolhe um bot da lista de bots
        self.bot.boas_vindas() #imprime a mensagem de boas vindas do bot
        while True: #entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
            self.mostra_comandos_bot()
            if self.le_envia_comando(): break
        self.bot.despedida() #ao sair mostra a mensagem de despedida do bot
    
    @property
    def empresa(self): return(self.__empresa)

    @property
    def lista_bots(self): return(self.__lista_bots)

    @property
    def bot(self): return(self.__bot)

    @bot.setter
    def bot(self, bot): self.__bot = bot
