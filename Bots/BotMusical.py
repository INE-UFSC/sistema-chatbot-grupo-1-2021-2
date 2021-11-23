from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print(f'Deixa eu me apresentar que eu acabei de chegar! Meu nome é {self.__nome}!')
 
    def mostra_comandos(self):
        print('1 - Bom dia \n2 - Qual o seu nome?')
        print('3 - Como vai ser o futuro? \n4 - Adeus')
    
    def executa_comando(self,cmd):
        if cmd == 1:
            self.boas_vindas()
        elif cmd ==2:
            self.repetir_o_nome
        elif cmd == 3:
            self.futuro
        else:
            self.despedida()

    def futuro(self):
        print('Eu vejo a vida melhor no futuro, eu vejo isso por cima de um muro\nde hipocrisia que insiste em nos rodear...')

    def boas_vindas(self):
        print('Alguma coisa acontece no meu coração... Ah, oi! Bom dia!')

    def repetir_o_nome(self):
        print(f'EU SOU O SAMBAAA! Brincadeira, meu nome é {self.__nome}!')

    def despedida(self):
        print('Deixe-me ir, preciso andar, vou por aí a procurar... Rir pra não chorar! Tchaau!')