from Bots.Bot import Bot

class BotJose(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @property
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print("Mensagem de apresentação: Olá, eu sou o José, seu bot conselheiro")
 
    def mostra_comandos(self):
        print("1 - conselho para os estudos")
        print("2 - conselho amoroso")
        print("3 - conselho para a carreira")    
        print("4 - adeus")
    def executa_comando(self,cmd):
        if self.cmd == 1:
            print("José analisa suas notas")
            print("José diz: Desistir é para os fracos, o ideal é nem tentar")
        elif self.cmd == 2:
            print("José analisa seu Tinder")
            print("José diz: Nunca é tarde para um novo fracasso")
        elif self.cmd == 3:
            print("José te entrega um guia de como se comportar numa entrevista")
            print("Regra 1: chame o empregador de 'meu parça', é contrato na certa")
            print("José diz: Vamos esquecer os erros do passado, meu amigo, e focar nos erros do futuro")
        elif self.cmd == 4:
            print("José diz: Meu amigo, espero que siga os meus conselhos. Adeus, até vista")
        else:
            print("Comando inexistente")

    def boas_vindas(self):
        print("José diz: Que bom que você me escolheu! Espero que eu possa te ajudar")

    def despedida(self):
        print("José diz: Meu amigo, espero que siga os meus conselhos. Adeus, até vista")
