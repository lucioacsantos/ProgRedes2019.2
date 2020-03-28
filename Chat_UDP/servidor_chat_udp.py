#Um servidor UDP

# Importando a biblioteca socket
import socket
HOST = '127.0.0.1' #Definindo o IP do servidor
PORT = 12345 #Definindo a porta
# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT)) # Ligando o socket a porta
print('Recebendo Mensagens...\n\n')

while True:
    # Recebendo os dados do cliente
    msg, cliente = udp_socket.recvfrom(512) #buffer de 512 bytes
    # Imprimindo a mensagem recebida convertendo de bytes para string
    print(cliente, msg.decode('utf-8'))

# Fechando o socket
udp_socket.close()