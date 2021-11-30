from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots = []
        for bot in lista_bots:
            if type(bot) is Bot:
                self.__lista_bots.append(bot)
            else:
                raise ValueError('Um dos bots inseridos nao pertence a classe Bot')
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Bom dia, bem vindo ao sistema de chatbots da empresa {self.empresa}!\n')

    def mostra_menu(self):
        print('Bots disponíveis:')
        for i,bot in enumerate(self.lista_bots):
            print(f'{i+1} - Bot: {bot.nome} - Apresentação: {bot.apresentacao}')

    
    def escolhe_bot(self):
        while True:
            escolha = input('Digite o numero do bot desejado: ')
            try: escolha = int(escolha)
            except: escolha=-1
            if escolha > 0 and escolha <= len(self.lista_bots):
                self.bot = self.lista_bots[escolha-1]
                break
            else: print('Escolha inválida')

    def mostra_comandos_bot(self):
        print(self.bot.mostra_comandos())
        print()

    def le_envia_comando(self):
        while True:
            escolha = input('Digite o numero do comando desejado (ou -1 para sair): ')
            try: escolha = int(escolha)
            except: escolha=-2
            if escolha > 0 and escolha <= len(self.bot.comandos):
                print(self.bot.executa_comando(escolha-1))
                return False
            elif escolha == -1:
                return True
            else: print('Escolha inválida')

    def inicio(self):
        self.boas_vindas() #mostra a tela de boas vindas
        self.mostra_menu() #mostra o menu com os bots disponiveis
        self.escolhe_bot() #o usuario escolhe um bot da lista de bots
        print(self.bot.boas_vindas()) #imprime a mensagem de boas vindas do bot
        while True: #entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
            self.mostra_comandos_bot()
            if self.le_envia_comando(): break
        print(self.bot.despedida()) #ao sair mostra a mensagem de despedida do bot
    
    @property
    def empresa(self): return(self.__empresa)

    @property
    def lista_bots(self): return(self.__lista_bots)

    @property
    def bot(self): return(self.__bot)

    @bot.setter
    def bot(self, bot): self.__bot = bot
