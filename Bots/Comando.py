class Comando():
    def __init__(self, nome_comando:str, resposta_comando:str):
        self.__nome_comando = nome_comando
        self.__resposta_comando = resposta_comando

    @property
    def nome_comando(self):
        return self.__nome_comando

    @property
    def resposta_comando(self):
        return self.__resposta_comando

    @nome_comando.setter
    def nome_comando(self, nome_comando):
        self.__nome_comando = nome_comando

    @resposta_comando.setter
    def resposta_comando(self, resposta_comando):
        self.__resposta_comando = resposta_comando
