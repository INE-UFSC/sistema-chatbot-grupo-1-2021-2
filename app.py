#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotMusical import BotMusical
from Bots.BotJose import BotJose

###construa a lista de bots disponíveis aqui
lista_bots = [BotJose('José'), BotMusical('Brook')]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
