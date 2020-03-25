import socket
#serveri
IPADDRESS = "localhost"
PORT = 12000
serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Serveri eshte startuar ne localhost ne portin: ' + str(PORT))
serverS.bind((IPADDRESS,PORT))
#print('Serveri eshte startuar ne localhost ne portin: ' + str(PORT))
serverS.listen(5)
clientS, address = serverS.accept()
print('Serveri eshte duke pritun ndonje kerkese:')
try:
   while True:
       fjalia = clientS.recv(2048)
       print('Kerkesa nga klienti:' + str(fjalia.decode("utf-8")))
       clientS.send(fjaliaP)
       clientS.close()


except:
    pass
finally:
    pass