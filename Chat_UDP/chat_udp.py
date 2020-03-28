# Programa cliente de chat
# LucioACSantos

#
# Método import
#
import sys
import os
import datetime
import socket

#
# Limpando a tela
#

os.system('cls||clear')

#
# Configuracoes do servidor
#

HOST = '127.0.0.1'
#HOST = '10.25.1.26'
PORTA = 12345

LOGIN_SENHA = 'LucioACSantos/gbat2k'
COMP_LOGIN_SENHA = str(len(LOGIN_SENHA))

# Socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Comandos para o servidor
LOGIN = '!l'
LOGOFF = '!x'
LOGOFF_SAIDA = '!q'

# Iniciando transacao
CMD_LOGIN = '001'
MSG = CMD_LOGIN +' ' + COMP_LOGIN_SENHA + ' ' + LOGIN_SENHA
#print(MSG)
MSG = MSG.encode('utf-8')
udp_socket.sendto(MSG, (HOST, PORTA))

CMD_TEXTO = '003'
TEXTO = 'MOURAO'
TEXTO = CMD_TEXTO + ' ' + TEXTO
TEXTO = TEXTO.encode('utf-8')
udp_socket.sendto(TEXTO, (HOST, PORTA))

# Recebendo dados
#RESPOSTA = udp_socket.recvfrom(512)
#RESPOSTA = RESPOSTA.decode('utf-8')




#udp_socket.sendto(msg, (HOST, PORTA))

# Fechando socket
#udp_socket.close()
