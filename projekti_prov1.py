import socket
#klienti
IPADDRESS = "localhost"
PORT = 12000
COUNT=0
#REVERSE
#PALINDROME
#TIME
#GAME
#CONVERT
#GCF

'''
class BLERONA:
    def __init__(self, name, ):
'''  
clinentC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clinentC.connect((IPADDRESS,PORT))
print('Ky eshte klienti')
var = input('Operacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT)?')
clinentC.sendall(str.encode(var))
#if - in not None:
TEKSTI = ' '
while True:
    data = clinentC.recv(128)
    if len(data) >= 128 or len(data) <= 128:
         break
    TEKSTI += data.decode('utf-8')
    print('-------------------------------------')
clinentC.close()












